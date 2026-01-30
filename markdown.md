# Zivid on macOS using the Qt Framework

It is realistically possible to build an application using the Qt Framework for Zivid. Since the Zivid SDK is C++ based, it integrates directly with Qt.

### Key Implementation Details

* **Build System**: Use **CMake** to link the Zivid SDK libraries (`Zivid::SDK`) and Qt modules (e.g., `Qt6::Widgets`, `Qt6::Gui`).
* **Concurrency**: Perform camera captures and heavy point cloud processing in a separate `QThread` or using `QtConcurrent` to prevent the UI from freezing.
* **Visualization**: Use `QOpenGLWidget` or `Qt Quick 3D` to render `.zdf` point clouds in real-time.
* **Data Conversion**: Convert Zivid point cloud buffers into a format compatible with Qt's rendering pipeline or third-party libraries like PCL (Point Cloud Library) integrated within the Qt app.

### Prerequisites

* Zivid SDK
* Qt 6.7+ (you likely already have it)
* CMake (optional but recommended)
* Optional but recommended:
  * vtk (for 3D visualization) — brew install vtk
  * Open3D (alternative) — pip install open3d
