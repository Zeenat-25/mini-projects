"""
hand_tracker.py - Hand Detection and Landmark Tracking
Works with mediapipe 0.10.x using the Tasks API.
Does NOT use mediapipe.framework.formats (avoids import errors).
"""

import cv2
import numpy as np
import mediapipe as mp
import urllib.request
import os


# ---------------------------------------------------------------------------
# Model download
# ---------------------------------------------------------------------------
MODEL_PATH = "hand_landmarker.task"
MODEL_URL  = (
    "https://storage.googleapis.com/mediapipe-models/"
    "hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
)

def _ensure_model():
    if not os.path.exists(MODEL_PATH):
        print(f"[INFO] Downloading hand landmark model (~25 MB)...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("[INFO] Model downloaded successfully.")


# ---------------------------------------------------------------------------
# Drawing helper (no mp.solutions needed)
# ---------------------------------------------------------------------------

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (0,9),(9,10),(10,11),(11,12),
    (0,13),(13,14),(14,15),(15,16),
    (0,17),(17,18),(18,19),(19,20),
    (5,9),(9,13),(13,17),
]

def _draw_hand(frame_bgr, landmarks_px):
    for a, b in HAND_CONNECTIONS:
        cv2.line(frame_bgr, landmarks_px[a], landmarks_px[b], (0, 200, 100), 2, cv2.LINE_AA)
    for pt in landmarks_px:
        cv2.circle(frame_bgr, pt, 4, (255, 255, 255), -1)
        cv2.circle(frame_bgr, pt, 4, (0, 150, 80), 1)


# ===========================================================================
# HandTracker
# ===========================================================================

class HandTracker:
    FINGERTIP_IDS = [4, 8, 12, 16, 20]
    PIP_IDS       = [3, 6, 10, 14, 18]

    def __init__(self, max_hands=1, detection_confidence=0.75, tracking_confidence=0.75):
        self.landmarks = []
        self._h = self._w = 1

        try:
            from mediapipe.tasks import python as _mp_tasks
            from mediapipe.tasks.python import vision as _mp_vision

            _ensure_model()

            base_opts = _mp_tasks.BaseOptions(model_asset_path=MODEL_PATH)
            opts = _mp_vision.HandLandmarkerOptions(
                base_options=base_opts,
                num_hands=max_hands,
                min_hand_detection_confidence=detection_confidence,
                min_hand_presence_confidence=detection_confidence,
                min_tracking_confidence=tracking_confidence,
                running_mode=_mp_vision.RunningMode.IMAGE,
            )
            self._landmarker = _mp_vision.HandLandmarker.create_from_options(opts)
            self._last_result = None
            self._mode = "tasks"
            print(f"[INFO] Mediapipe {mp.__version__} — using Tasks API")

        except Exception as e:
            print(f"[INFO] Tasks API unavailable ({e}), falling back to mp.solutions")
            self._mp_hands  = mp.solutions.hands
            self._mp_draw   = mp.solutions.drawing_utils
            self._mp_styles = mp.solutions.drawing_styles
            self._hands = self._mp_hands.Hands(
                max_num_hands=max_hands,
                min_detection_confidence=detection_confidence,
                min_tracking_confidence=tracking_confidence,
            )
            self._results = None
            self._mode = "solutions"

    def process(self, frame_rgb):
        self._h, self._w = frame_rgb.shape[:2]
        self.landmarks = []
        if self._mode == "tasks":
            return self._process_tasks(frame_rgb)
        else:
            return self._process_solutions(frame_rgb)

    def _process_tasks(self, frame_rgb):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        self._last_result = self._landmarker.detect(mp_image)
        if self._last_result.hand_landmarks:
            for lm in self._last_result.hand_landmarks[0]:
                self.landmarks.append((int(lm.x * self._w), int(lm.y * self._h)))
            return True
        return False

    def _process_solutions(self, frame_rgb):
        self._results = self._hands.process(frame_rgb)
        if self._results.multi_hand_landmarks:
            for lm in self._results.multi_hand_landmarks[0].landmark:
                self.landmarks.append((int(lm.x * self._w), int(lm.y * self._h)))
            return True
        return False

    def draw_landmarks(self, frame_bgr):
        if not self.landmarks:
            return
        if self._mode == "tasks":
            _draw_hand(frame_bgr, self.landmarks)
        else:
            if self._results and self._results.multi_hand_landmarks:
                for hand_lm in self._results.multi_hand_landmarks:
                    self._mp_draw.draw_landmarks(
                        frame_bgr, hand_lm,
                        self._mp_hands.HAND_CONNECTIONS,
                        self._mp_styles.get_default_hand_landmarks_style(),
                        self._mp_styles.get_default_hand_connections_style(),
                    )

    def fingers_up(self):
        if not self.landmarks:
            return [False] * 5
        up = []
        for tip_id, pip_id in zip(self.FINGERTIP_IDS, self.PIP_IDS):
            up.append(self.landmarks[tip_id][1] < self.landmarks[pip_id][1])
        return up

    def index_up_only(self):
        f = self.fingers_up()
        return f[1] and not f[2]

    def two_fingers_up(self):
        f = self.fingers_up()
        return f[1] and f[2]

    def get_index_tip(self):
        return self.landmarks[8] if self.landmarks else None

    def get_middle_tip(self):
        return self.landmarks[12] if self.landmarks else None