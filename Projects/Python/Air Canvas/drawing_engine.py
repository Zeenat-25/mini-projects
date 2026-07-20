"""
drawing_engine.py - Stroke Management and Smoothing
"""

import cv2
import numpy as np

BRUSH_THICKNESS  = 6
ERASER_THICKNESS = 40
SMOOTHING_WINDOW = 5


class Stroke:
    def __init__(self, color, thickness):
        self.color      = color
        self.thickness  = thickness
        self.points     = []
        self.smooth_pts = []

    def add_point(self, pt):
        self.points.append(pt)
        n = len(self.points)
        w = min(SMOOTHING_WINDOW, n)
        recent = self.points[max(0, n - w):]
        avg_x  = int(np.mean([p[0] for p in recent]))
        avg_y  = int(np.mean([p[1] for p in recent]))
        self.smooth_pts.append((avg_x, avg_y))

    def render(self, canvas):
        if len(self.smooth_pts) < 2:
            return
        for i in range(1, len(self.smooth_pts)):
            cv2.line(canvas, self.smooth_pts[i-1], self.smooth_pts[i],
                     self.color, self.thickness, cv2.LINE_AA)


class DrawingEngine:
    def __init__(self, width, height):
        self.width   = width
        self.height  = height
        self.canvas  = np.zeros((height, width, 3), dtype=np.uint8)
        self.strokes = []
        self.current_stroke = None

    def pen_down(self, pt, color, thickness):
        self.current_stroke = Stroke(color, thickness)
        self.current_stroke.add_point(pt)

    def pen_move(self, pt):
        if self.current_stroke:
            self.current_stroke.add_point(pt)
            pts = self.current_stroke.smooth_pts
            if len(pts) >= 2:
                cv2.line(self.canvas, pts[-2], pts[-1],
                         self.current_stroke.color,
                         self.current_stroke.thickness, cv2.LINE_AA)

    def pen_up(self):
        if self.current_stroke and len(self.current_stroke.points) > 1:
            self.strokes.append(self.current_stroke)
        self.current_stroke = None

    def erase(self, pt):
        cv2.circle(self.canvas, pt, ERASER_THICKNESS // 2, (0, 0, 0), -1)

    def clear(self):
        self.strokes.clear()
        self.current_stroke = None
        self.canvas[:] = 0

    def get_canvas(self):
        return self.canvas