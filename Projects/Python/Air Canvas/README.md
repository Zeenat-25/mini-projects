# ✋ Air Canvas — Hand Gesture Drawing with 3D Shape Detection

Draw in the air using your hand! Air Canvas uses your webcam + Mediapipe
to track your index finger in real-time. Draw freely, pick colours from
the toolbar, and close a shape to instantly see it extruded into 3D.

---

## 📁 Project Structure

```
air_canvas/
├── main.py            ← Entry point
├── canvas.py          ← Main orchestrator (AirCanvas class)
├── hand_tracker.py    ← Mediapipe hand landmark wrapper
├── toolbar.py         ← Top toolbar UI (colours, eraser, clear)
├── drawing_engine.py  ← Stroke management + shape-close detection
├── shape_3d.py        ← PyOpenGL 3D extrusion viewer
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

| Requirement | Version |
|---|---|
| Python | 3.9 – 3.11 (recommended 3.10) |
| Webcam | Any USB or built-in camera |
| OS | Windows / macOS / Linux |

> **Note for macOS**: GLUT may require `brew install freeglut`.  
> **Note for Linux**: Run `sudo apt install freeglut3-dev` for OpenGL support.

---

## 🚀 Step-by-Step Setup

### 1 – Clone / Download the project

```bash
# Option A – clone (if using git)
git clone <repo-url> air_canvas
cd air_canvas

# Option B – just download all .py files into a folder called air_canvas/
```

### 2 – Create a virtual environment (recommended)

```bash
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3 – Install dependencies

```bash
pip install -r requirements.txt
```

If PyOpenGL gives errors on Windows, install the unofficial wheels:
```
pip install PyOpenGL PyOpenGL_accelerate
```
*(The app still works without PyOpenGL – it falls back to a 2D preview.)*

### 4 – Run

```bash
python main.py
```

---

## 🎮 Controls

| Gesture / Key | Action |
|---|---|
| ☝️ Index finger up | **Draw** on the canvas |
| ✌️ Two fingers up | **Selection mode** – hover over toolbar |
| Hover 2 fingers on colour | Select that colour (hold ~0.4 s) |
| Hover 2 fingers on Eraser | Switch to eraser |
| Hover 2 fingers on Clear | Clear the canvas |
| Close a shape (join start↔end) | **Generate 3D object** |
| `C` key | Clear canvas instantly |
| `Q` or `Esc` | Quit |

### In the 3D Viewer Window

| Action | Control |
|---|---|
| Rotate | Left-click and drag |
| Zoom | Scroll wheel |
| Close | Press `Q` or `Esc` |

---

## 🎨 Colours Available

Red · Green · Blue · Yellow · White · Purple · Cyan · Orange

---

## 🔮 How the 3D Feature Works

1. Every time you lift your finger, `DrawingEngine` checks if the
   endpoint of your stroke is within **40 px** of the start point.
2. If yes (and the stroke has ≥ 20 points), it's treated as a **closed shape**.
3. The contour is **centred**, **normalised**, and **extruded** in Z
   to create a prism mesh.
4. PyOpenGL renders it in a separate interactive window with lighting,
   blending, and a wireframe overlay.

---

## 🛠️ Customisation

Edit these constants in the relevant files:

| File | Constant | Default | Effect |
|---|---|---|---|
| `canvas.py` | `CAMERA_INDEX` | `0` | Webcam index |
| `canvas.py` | `FLIP_FRAME` | `True` | Mirror image |
| `canvas.py` | `SELECTION_HOLD` | `0.4 s` | Hover delay |
| `drawing_engine.py` | `BRUSH_THICKNESS` | `6` | Pen width |
| `drawing_engine.py` | `ERASER_THICKNESS` | `40` | Eraser size |
| `drawing_engine.py` | `CLOSE_THRESHOLD` | `40 px` | Shape-close distance |
| `drawing_engine.py` | `SMOOTHING_WINDOW` | `5` | Stroke smoothness |
| `shape_3d.py` | `depth` arg in `_build_mesh` | `1.0` | 3D extrusion depth |

---

## ❓ Troubleshooting

**Camera not found**  
→ Change `CAMERA_INDEX = 0` to `1` or `2` in `canvas.py`.

**Hand not detected**  
→ Ensure good lighting. Keep your hand within 30–80 cm of the camera.

**3D window doesn't open**  
→ Install PyOpenGL: `pip install PyOpenGL PyOpenGL_accelerate`  
→ On Linux, also: `sudo apt install freeglut3-dev`

**Low FPS**  
→ Lower camera resolution in `canvas.py`:  
  `self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)`  
  `self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)`

---

## 📦 All Libraries Used

| Library | Purpose |
|---|---|
| `opencv-python` | Camera capture, frame rendering, UI |
| `mediapipe` | Real-time hand landmark detection |
| `numpy` | Array ops, geometry, interpolation |
| `PyOpenGL` | 3D extrusion rendering |
| `PyOpenGL_accelerate` | Compiled speed boost for OpenGL |

---

*Made with ❤️ using Python, OpenCV, Mediapipe, and PyOpenGL.*
