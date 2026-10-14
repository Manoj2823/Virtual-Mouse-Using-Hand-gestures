# 🖱️ Virtual Mouse Using Hand Gesture Recognition

A computer vision-based Virtual Mouse application that allows users to control their computer cursor using hand gestures through a webcam. Built using Python, OpenCV, MediaPipe, and PyAutoGUI, this project provides a touch-free way to interact with a computer.

## 📌 Project Overview

The Virtual Mouse system detects and tracks hand landmarks in real time using a webcam. It interprets specific finger and hand gestures to perform mouse operations, reducing the need for a physical mouse.

The project combines computer vision and hand gesture recognition to create an interactive, touchless computer control system.

## ✨ Features

- 🖐️ **Real-Time Hand Tracking** — Detects and tracks hand landmarks using MediaPipe.
- 🖱️ **Cursor Movement** — Controls mouse cursor movement using hand gestures.
- 👆 **Left Click** — Performs left-click operations using supported gestures.
- 👉 **Right Click** — Performs right-click operations using supported gestures.
- 🎯 **Gesture Recognition** — Identifies hand positions and landmark distances to recognize supported gestures.
- ⚡ **Smooth Cursor Movement** — Uses smoothing techniques to help reduce cursor jitter.
- 📷 **Webcam Integration** — Uses a webcam to capture live video for hand tracking.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand landmark detection and tracking |
| PyAutoGUI | Mouse cursor movement and click control |
| NumPy | Numerical operations, if used in the implementation |

## ⚙️ How It Works

1. The webcam captures live video frames.
2. OpenCV processes the frames.
3. MediaPipe detects the hand and identifies its landmarks.
4. The application analyzes landmark positions and distances to recognize gestures.
5. Recognized gestures are mapped to mouse actions.
6. PyAutoGUI executes the corresponding cursor movement or click.

## 📋 Requirements

- Python 3.x
- A working webcam
- A computer running a supported operating system
- The Python libraries used by the project

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Navigate to the project directory

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Install dependencies

```bash
pip install opencv-python mediapipe pyautogui numpy
```

If your project includes a `requirements.txt` file, use:

```bash
pip install -r requirements.txt
```

### 4. Run the application

Run the main Python file:

```bash
python main.py
```

Replace `main.py` with your actual entry-point filename if it is different.

## 🎮 Usage

1. Connect or enable your webcam.
2. Run the Python application.
3. Position your hand within the camera frame.
4. Move your hand to control the cursor.
5. Use the supported gestures to perform left-click and right-click operations.

The exact gestures depend on the implementation in your source code.

## 🎯 Learning Outcomes

- Practical experience with computer vision.
- Real-time hand tracking using MediaPipe.
- Hand landmark detection and distance calculations.
- Gesture-based human-computer interaction.
- Integration of Python libraries with desktop mouse controls.
- Cursor smoothing and gesture recognition logic.

## 🔮 Future Enhancements

- Add scroll control using hand gestures.
- Implement drag-and-drop functionality.
- Add configurable gesture mappings.
- Improve gesture recognition accuracy under different lighting conditions.
- Introduce a graphical user interface for adjusting sensitivity and settings.
- Add support for additional mouse operations.

## 👨‍💻 Author

**Manoj Ramesh**

- GitHub: [Manoj2823](https://github.com/Manoj2823)
- LinkedIn: [manojramesh](https://linkedin.com/in/manojramesh28)

## 📄 License

This project is available for learning and educational purposes. Add a suitable open-source license if you intend to distribute or reuse the project publicly.
