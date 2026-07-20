"""
toolbar.py - Top Toolbar for Color and Tool Selection
Renders the color palette, eraser, and clear button on a dedicated strip.
"""

import cv2
import numpy as np


# ---------------------------------------------------------------------------
# Color definitions  (BGR format for OpenCV)
# ---------------------------------------------------------------------------
COLORS = {
    "Red":    (0,   0,   220),
    "Green":  (0,   200, 0  ),
    "Blue":   (230, 100, 0  ),
    "Yellow": (0,   220, 220),
    "White":  (255, 255, 255),
    "Purple": (200, 0,   200),
    "Cyan":   (220, 220, 0  ),
    "Orange": (0,   140, 255),
}

ERASER_KEY = "Eraser"
CLEAR_KEY  = "Clear"


class Toolbar:
    """
    Manages the top toolbar strip.
    Handles hit-testing so the canvas can ask which tool/color
    is under a given (x, y) coordinate.
    """

    TOOLBAR_HEIGHT = 80   # pixels
    PADDING        = 8

    def __init__(self, frame_width):
        self.frame_width     = frame_width
        self.color_names     = list(COLORS.keys())
        self.selected_color  = "Red"         # Active drawing color name
        self.selected_tool   = "draw"        # "draw" | "eraser"
        self._build_slots()

    # ------------------------------------------------------------------
    # Layout builder
    # ------------------------------------------------------------------

    def _build_slots(self):
        """Pre-compute bounding boxes for every toolbar button."""
        n_colors  = len(self.color_names)
        extras    = 2        # Eraser + Clear
        n_slots   = n_colors + extras

        slot_w    = self.frame_width // n_slots
        h         = self.TOOLBAR_HEIGHT
        p         = self.PADDING

        self.slots = {}   # name → (x1, y1, x2, y2)

        for i, name in enumerate(self.color_names):
            x1 = i * slot_w + p
            self.slots[name] = (x1, p, x1 + slot_w - 2 * p, h - p)

        # Eraser
        i = n_colors
        x1 = i * slot_w + p
        self.slots[ERASER_KEY] = (x1, p, x1 + slot_w - 2 * p, h - p)

        # Clear
        i = n_colors + 1
        x1 = i * slot_w + p
        self.slots[CLEAR_KEY] = (x1, p, x1 + slot_w - 2 * p, h - p)

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------

    def draw(self, frame):
        """Render the toolbar onto the top of *frame* (in-place)."""
        h = self.TOOLBAR_HEIGHT

        # Semi-transparent dark background
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (self.frame_width, h), (20, 20, 20), -1)
        cv2.addWeighted(overlay, 0.85, frame, 0.15, 0, frame)

        # Bottom border line
        cv2.line(frame, (0, h), (self.frame_width, h), (60, 60, 60), 1)

        # Color buttons
        for name, (x1, y1, x2, y2) in self.slots.items():
            if name == ERASER_KEY:
                self._draw_eraser_btn(frame, x1, y1, x2, y2)
            elif name == CLEAR_KEY:
                self._draw_clear_btn(frame, x1, y1, x2, y2)
            else:
                self._draw_color_btn(frame, name, x1, y1, x2, y2)

        # Label: current tool
        label = f"Tool: {self.selected_color if self.selected_tool == 'draw' else 'Eraser'}"
        cv2.putText(frame, label, (10, h + 22),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (180, 180, 180), 1, cv2.LINE_AA)

    def _draw_color_btn(self, frame, name, x1, y1, x2, y2):
        color = COLORS[name]
        is_selected = (self.selected_tool == "draw" and self.selected_color == name)

        # Fill
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)

        # Highlight border for active selection
        border_color = (255, 255, 255) if is_selected else (80, 80, 80)
        thickness    = 3 if is_selected else 1
        cv2.rectangle(frame, (x1, y1), (x2, y2), border_color, thickness)

        # Label
        font_color = (0, 0, 0) if name == "Yellow" or name == "White" else (240, 240, 240)
        cv2.putText(frame, name, (x1 + 4, y2 - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.38, font_color, 1, cv2.LINE_AA)

    def _draw_eraser_btn(self, frame, x1, y1, x2, y2):
        is_selected = self.selected_tool == "eraser"
        bg          = (70, 70, 70) if is_selected else (40, 40, 40)
        cv2.rectangle(frame, (x1, y1), (x2, y2), bg, -1)
        border = (255, 255, 255) if is_selected else (100, 100, 100)
        cv2.rectangle(frame, (x1, y1), (x2, y2), border, 2 if is_selected else 1)
        cv2.putText(frame, "Eraser", (x1 + 4, y2 - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.38, (220, 220, 220), 1, cv2.LINE_AA)

    def _draw_clear_btn(self, frame, x1, y1, x2, y2):
        cv2.rectangle(frame, (x1, y1), (x2, y2), (30, 30, 80), -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (100, 100, 180), 1)
        cv2.putText(frame, "Clear", (x1 + 6, y2 - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.38, (180, 180, 255), 1, cv2.LINE_AA)

    # ------------------------------------------------------------------
    # Hit testing
    # ------------------------------------------------------------------

    def is_in_toolbar(self, x, y):
        """Returns True if (x, y) falls inside the toolbar strip."""
        return y <= self.TOOLBAR_HEIGHT

    def handle_selection(self, x, y):
        """
        Check if (x, y) hovers over a toolbar button.
        Updates selected_color / selected_tool.
        Returns "clear" if the Clear button was hit, else None.
        """
        for name, (x1, y1, x2, y2) in self.slots.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                if name == CLEAR_KEY:
                    return "clear"
                elif name == ERASER_KEY:
                    self.selected_tool = "eraser"
                else:
                    self.selected_color = name
                    self.selected_tool  = "draw"
                return name
        return None

    # ------------------------------------------------------------------
    # Public getters
    # ------------------------------------------------------------------

    def get_draw_color(self):
        """Returns BGR color tuple for the active drawing color."""
        return COLORS[self.selected_color]

    def is_eraser(self):
        return self.selected_tool == "eraser"
