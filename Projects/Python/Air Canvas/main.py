"""
Air Canvas - Main Entry Point
Launches the Air Canvas application with hand tracking and 3D shape detection.
"""

import sys
import cv2
from canvas import AirCanvas

def main():
    print("=" * 50)
    print("   AIR CANVAS - Hand Gesture Drawing App")
    print("=" * 50)
    print("\nControls:")
    print("  ✋ Index finger UP       → Draw mode")
    print("  ✌  Two fingers UP        → Selection mode")
    print("  🎨 Hover over toolbar    → Select color/eraser")
    print("  🔄 Close a shape         → Generate 3D object")
    print("  [C] Clear canvas")
    print("  [Q] Quit\n")

    try:
        app = AirCanvas()
        app.run()
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user.")
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    finally:
        cv2.destroyAllWindows()
        print("[INFO] Application closed.")

if __name__ == "__main__":
    main()
