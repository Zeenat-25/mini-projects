"""
canvas.py - AirCanvas Orchestrator (no 3D)
"""

import cv2
import numpy as np
import time

from hand_tracker   import HandTracker
from toolbar        import Toolbar
from drawing_engine import DrawingEngine, BRUSH_THICKNESS, ERASER_THICKNESS

CAMERA_INDEX   = 0
FLIP_FRAME     = True
TARGET_FPS     = 30
SELECTION_HOLD = 0.4


class AirCanvas:
    STATE_IDLE      = "idle"
    STATE_DRAWING   = "drawing"
    STATE_SELECTING = "selecting"

    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cap.set(cv2.CAP_PROP_FPS, TARGET_FPS)

        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Cannot open webcam. Check CAMERA_INDEX in canvas.py.")

        if FLIP_FRAME:
            frame = cv2.flip(frame, 1)
        self.h, self.w = frame.shape[:2]

        self.tracker  = HandTracker()
        self.toolbar  = Toolbar(self.w)
        self.engine   = DrawingEngine(self.w, self.h)

        self.state         = self.STATE_IDLE
        self._hover_start  = None
        self._hover_slot   = None
        self._last_draw_pt = None

    def run(self):
        cv2.namedWindow("Air Canvas", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Air Canvas", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        prev_time = time.time()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if FLIP_FRAME:
                frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            hand_detected = self.tracker.process(rgb)

            if hand_detected:
                self._handle_gestures(frame)
            else:
                if self.state == self.STATE_DRAWING:
                    self.engine.pen_up()
                self.state         = self.STATE_IDLE
                self._last_draw_pt = None
                self._hover_start  = None

            display = self._compose(frame)

            now       = time.time()
            fps       = 1.0 / max(now - prev_time, 1e-6)
            prev_time = now
            cv2.putText(display, f"FPS: {fps:.0f}",
                        (self.w - 90, self.h - 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (80, 80, 80), 1)

            cv2.imshow("Air Canvas", display)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                break
            if key == ord('c') or key == ord('C'):
                self.engine.clear()

        self.cap.release()
        cv2.destroyAllWindows()

    def _handle_gestures(self, frame):
        index_tip  = self.tracker.get_index_tip()
        two_up     = self.tracker.two_fingers_up()
        index_only = self.tracker.index_up_only()

        if index_tip is None:
            return

        x, y = index_tip

        if two_up:
            if self.state == self.STATE_DRAWING:
                self.engine.pen_up()
            self.state         = self.STATE_SELECTING
            self._last_draw_pt = None

            if self.toolbar.is_in_toolbar(x, y):
                self._do_hover_selection(x, y)
            else:
                self._hover_start = None
                self._hover_slot  = None

            cv2.circle(frame, (x, y), 12, (200, 200, 200), 2)
            cv2.circle(frame, (x, y),  3, (255, 255, 255), -1)
            return

        if index_only and not self.toolbar.is_in_toolbar(x, y):
            self._hover_start = None
            color     = self.toolbar.get_draw_color()
            thickness = ERASER_THICKNESS if self.toolbar.is_eraser() else BRUSH_THICKNESS

            if self.toolbar.is_eraser():
                self.engine.erase((x, y))
                self.state = self.STATE_DRAWING
            else:
                if self.state != self.STATE_DRAWING or self._last_draw_pt is None:
                    self.engine.pen_down((x, y), color, thickness)
                    self.state = self.STATE_DRAWING
                else:
                    self.engine.pen_move((x, y))

            self._last_draw_pt = (x, y)
            cv2.circle(frame, (x, y), thickness // 2 + 2, color, -1)
            return

        if self.state == self.STATE_DRAWING:
            self.engine.pen_up()
        self.state         = self.STATE_IDLE
        self._last_draw_pt = None

    def _do_hover_selection(self, x, y):
        slot = self._get_hovered_slot(x, y)
        if slot != self._hover_slot:
            self._hover_slot  = slot
            self._hover_start = time.time() if slot else None
            return
        if self._hover_start and slot:
            elapsed = time.time() - self._hover_start
            if elapsed >= SELECTION_HOLD:
                result = self.toolbar.handle_selection(x, y)
                if result == "clear":
                    self.engine.clear()
                self._hover_start = None

    def _get_hovered_slot(self, x, y):
        for name, (x1, y1, x2, y2) in self.toolbar.slots.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                return name
        return None

    def _compose(self, camera_frame):
        bg     = (camera_frame * 0.30).astype(np.uint8)
        canvas = self.engine.get_canvas()
        mask   = canvas.sum(axis=2) > 0
        bg[mask] = canvas[mask]

        self.tracker.draw_landmarks(bg)
        self.toolbar.draw(bg)

        hints = "[Index] Draw   [2 Fingers] Select   [C] Clear   [Q] Quit"
        cv2.putText(bg, hints, (10, self.h - 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, (90, 90, 90), 1, cv2.LINE_AA)
        return bg