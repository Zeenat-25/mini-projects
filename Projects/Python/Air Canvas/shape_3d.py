"""
shape_3d.py - 3D Shape Extrusion and Interactive Rendering
Takes a 2D closed contour, extrudes it, and displays an interactive
3D window using PyOpenGL + GLUT. Runs in its own thread.
"""

import threading
import numpy as np
import sys


# ---------------------------------------------------------------------------
# Safe OpenGL import – show a friendly error if not installed
# ---------------------------------------------------------------------------
try:
    from OpenGL.GL   import *
    from OpenGL.GLU  import *
    from OpenGL.GLUT import *
    _HAS_OPENGL = True
except ImportError:
    _HAS_OPENGL = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _normalise_contour(contour, target_size=2.0):
    """
    Centre and scale contour points so the shape fits inside [-1, 1] on
    the largest axis, returning an Nx2 float array.
    """
    pts   = contour.astype(float)
    cx, cy = pts[:, 0].mean(), pts[:, 1].mean()
    pts[:, 0] -= cx
    pts[:, 1] -= cy

    # Flip Y so drawing 'up' maps to OpenGL 'up'
    pts[:, 1] *= -1

    scale = target_size / max(pts[:, 0].ptp(), pts[:, 1].ptp(), 1e-6)
    pts  *= scale
    return pts


def _build_mesh(contour_2d, depth=1.0):
    """
    Extrude a 2D contour into a 3D prism.
    Returns:
        front_pts  – Nx3 numpy array (z = +depth/2)
        back_pts   – Nx3 numpy array (z = -depth/2)
        tri_front  – list of (i,j,k) index triples for the front cap (fan)
        tri_back   – list of (i,j,k) index triples for the back cap
    """
    pts   = _normalise_contour(contour_2d)
    n     = len(pts)
    front = np.column_stack([pts,  np.full(n, depth / 2)])
    back  = np.column_stack([pts, np.full(n, -depth / 2)])

    # Simple fan triangulation from centroid (works for convex-ish shapes)
    tris_f, tris_b = [], []
    for i in range(1, n - 1):
        tris_f.append((0, i, i + 1))
        tris_b.append((0, i + 1, i))   # reversed for back face

    return front, back, tris_f, tris_b


# ---------------------------------------------------------------------------
# Interactive 3D window (GLUT)
# ---------------------------------------------------------------------------

class Shape3DViewer:
    """
    Opens a GLUT window and renders an extruded 3D shape.
    Mouse drag → rotate.  Scroll → zoom.
    """

    def __init__(self, contour, color_bgr):
        self.contour   = contour
        # Convert BGR → RGB 0-1
        b, g, r        = color_bgr
        self.color_rgb = (r / 255.0, g / 255.0, b / 255.0)

        # Camera state
        self.rot_x   =  20.0
        self.rot_y   = -30.0
        self.zoom    =  -5.0
        self._last_mouse = None

        # Build geometry
        self.front, self.back, self.tris_f, self.tris_b = _build_mesh(contour)
        self.n = len(self.front)

    # ------------------------------------------------------------------
    # GLUT callbacks
    # ------------------------------------------------------------------

    def _display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Camera
        glTranslatef(0.0, 0.0, self.zoom)
        glRotatef(self.rot_x, 1, 0, 0)
        glRotatef(self.rot_y, 0, 1, 0)

        r, g, b = self.color_rgb

        # --- Front face ---
        glColor4f(r, g, b, 0.95)
        glBegin(GL_TRIANGLES)
        for i, j, k in self.tris_f:
            for idx in (i, j, k):
                glVertex3fv(self.front[idx])
        glEnd()

        # --- Back face ---
        glColor4f(r * 0.7, g * 0.7, b * 0.7, 0.95)
        glBegin(GL_TRIANGLES)
        for i, j, k in self.tris_b:
            for idx in (i, j, k):
                glVertex3fv(self.back[idx])
        glEnd()

        # --- Side walls ---
        glColor4f(r * 0.85, g * 0.85, b * 0.85, 0.95)
        glBegin(GL_QUADS)
        for i in range(self.n):
            j = (i + 1) % self.n
            glVertex3fv(self.front[i])
            glVertex3fv(self.front[j])
            glVertex3fv(self.back[j])
            glVertex3fv(self.back[i])
        glEnd()

        # --- Wireframe overlay ---
        glColor4f(1, 1, 1, 0.25)
        glLineWidth(0.8)
        glBegin(GL_LINE_LOOP)
        for pt in self.front:
            glVertex3fv(pt)
        glEnd()
        glBegin(GL_LINE_LOOP)
        for pt in self.back:
            glVertex3fv(pt)
        glEnd()

        glutSwapBuffers()

    def _reshape(self, w, h):
        if h == 0:
            h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, w / h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def _mouse_button(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            self._last_mouse = (x, y) if state == GLUT_DOWN else None
        # Scroll wheel zoom
        if button == 3:   # scroll up
            self.zoom = min(-1.0, self.zoom + 0.2)
            glutPostRedisplay()
        if button == 4:   # scroll down
            self.zoom -= 0.2
            glutPostRedisplay()

    def _mouse_motion(self, x, y):
        if self._last_mouse:
            dx = x - self._last_mouse[0]
            dy = y - self._last_mouse[1]
            self.rot_y += dx * 0.5
            self.rot_x += dy * 0.5
            self._last_mouse = (x, y)
            glutPostRedisplay()

    def _keyboard(self, key, x, y):
        if key in (b'q', b'Q', b'\x1b'):
            glutDestroyWindow(glutGetWindow())

    # ------------------------------------------------------------------
    # Launch
    # ------------------------------------------------------------------

    def _run(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_ALPHA)
        glutInitWindowSize(640, 480)
        glutCreateWindow(b"Air Canvas - 3D Shape Viewer")

        # GL setup
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_LINE_SMOOTH)
        glClearColor(0.08, 0.08, 0.12, 1.0)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [3, 3, 3, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  [1, 1, 1, 1])
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glutDisplayFunc(self._display)
        glutReshapeFunc(self._reshape)
        glutMouseFunc(self._mouse_button)
        glutMotionFunc(self._mouse_motion)
        glutKeyboardFunc(self._keyboard)

        glutMainLoop()

    def launch_in_thread(self):
        """Spin up the GLUT window in a daemon thread."""
        t = threading.Thread(target=self._run, daemon=True)
        t.start()


# ---------------------------------------------------------------------------
# Public helper called by AirCanvas
# ---------------------------------------------------------------------------

def show_3d_shape(contour, color_bgr=(0, 200, 255)):
    """
    Entry-point: launch the 3D viewer for a closed contour.
    If PyOpenGL is not installed, prints a warning instead.
    """
    if not _HAS_OPENGL:
        print("[3D] PyOpenGL is not installed. "
              "Run:  pip install PyOpenGL PyOpenGL_accelerate --break-system-packages")
        _show_fallback_window(contour, color_bgr)
        return

    try:
        viewer = Shape3DViewer(contour, color_bgr)
        viewer.launch_in_thread()
    except Exception as e:
        print(f"[3D] Could not open 3D viewer: {e}")
        _show_fallback_window(contour, color_bgr)


# ---------------------------------------------------------------------------
# Fallback: plain OpenCV preview when PyOpenGL is unavailable
# ---------------------------------------------------------------------------

def _show_fallback_window(contour, color_bgr):
    """Display a simple 2D contour preview as a fallback."""
    import cv2
    import numpy as np

    size  = 400
    img   = np.zeros((size, size, 3), dtype=np.uint8)

    pts   = contour.astype(float)
    cx, cy = pts[:, 0].mean(), pts[:, 1].mean()
    pts[:, 0] -= cx
    pts[:, 1] -= cy
    scale = (size * 0.7) / max(pts[:, 0].ptp(), pts[:, 1].ptp(), 1)
    pts  *= scale
    pts[:, 0] += size // 2
    pts[:, 1] += size // 2
    pts_int = pts.astype(np.int32)

    cv2.polylines(img, [pts_int], True, color_bgr, 2, cv2.LINE_AA)
    cv2.fillPoly(img, [pts_int],
                 tuple(int(c * 0.35) for c in color_bgr))

    # Simulate "3D" with a subtle offset copy
    offset = pts_int + np.array([12, -12])
    cv2.polylines(img, [offset], True,
                  tuple(int(c * 0.6) for c in color_bgr), 1, cv2.LINE_AA)
    for a, b in zip(pts_int, offset):
        cv2.line(img, tuple(a), tuple(b),
                 tuple(int(c * 0.5) for c in color_bgr), 1)

    cv2.putText(img, "Shape Preview (install PyOpenGL for true 3D)",
                (10, size - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.32,
                (150, 150, 150), 1, cv2.LINE_AA)

    def _show():
        import cv2 as _cv2
        _cv2.imshow("3D Shape (fallback)", img)
        _cv2.waitKey(0)
        _cv2.destroyWindow("3D Shape (fallback)")

    t = threading.Thread(target=_show, daemon=True)
    t.start()
