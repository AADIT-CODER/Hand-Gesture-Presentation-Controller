# Hand Gesture Presentation Controller

## 📌 Project Overview

Hand Gesture Presentation Controller is a computer vision-based project that allows users to control PowerPoint presentations using hand gestures.

The system uses a webcam to detect hand movements in real time and performs presentation actions such as moving to the next slide, going back to the previous slide, and controlling the presentation without using a keyboard or mouse.

This project is developed using Python, OpenCV, CVZone, and computer vision techniques.

## 🎯 Objectives

* Control PowerPoint presentations using hand gestures.
* Detect hand movements through a webcam.
* Navigate between presentation slides without a keyboard.
* Provide a touchless and interactive presentation experience.
* Use computer vision for real-time gesture recognition.
* Improve presentation convenience and user interaction.

## 🛠️ Technologies Used

* Python
* OpenCV
* CVZone
* MediaPipe
* PyAutoGUI
* Computer Vision
* Hand Tracking
* PowerPoint Presentation

## ⚙️ How It Works

1. The webcam captures the user's live video.
2. OpenCV processes the video frames.
3. CVZone detects and tracks the user's hand.
4. The system identifies hand gestures and movements.
5. The detected gesture is converted into a presentation command.
6. The presentation is controlled using keyboard automation.
7. The user can navigate through slides without touching the keyboard or mouse.

## ✨ Features

* Real-time hand tracking.
* Webcam-based gesture detection.
* Touchless PowerPoint control.
* Next-slide and previous-slide navigation.
* Easy-to-use interface.
* Interactive computer vision application.
* Supports presentation slides stored in a separate folder.

## 📊 Project Results

The project successfully demonstrates the use of hand gestures to control presentation slides.

The system detects hand movements through the webcam and performs presentation navigation commands in real time.

### Output Screenshots

Add project screenshots or demo images here.

Example:

* Webcam hand tracking output.
* PowerPoint presentation control.
* Gesture detection results.
* Project execution screenshot.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Hand-Gesture-Presentation-Controller
```

### 3. Install Required Libraries

```bash
pip install opencv-python cvzone mediapipe pyautogui
```

### 4. Check the Project Structure

Make sure the project contains the `Presentation` folder with all the presentation slides.

```text
Hand-Gesture-Presentation-Controller/
│
├── main.py
├── Presentation/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   ├── 8.png
│   ├── 9.png
│   ├── 10.png
│   ├── 11.png
│   └── 12.png
│
└── README.md
```

### 5. Run the Project

```bash
python main.py
```

### 6. Start the Presentation

1. Open your PowerPoint presentation.
2. Start the slideshow.
3. Allow webcam access if requested.
4. Show your hand gestures in front of the webcam.
5. Use the detected gestures to navigate through the slides.

## 📁 Project Structure

```text
Hand-Gesture-Presentation-Controller/
│
├── main.py
├── Presentation/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── ...
│   └── 12.png
│
└── README.md
```

## 💡 Applications

* College presentations.
* Business presentations.
* Online teaching.
* Smart classrooms.
* Interactive demonstrations.
* Touchless computer interaction.
* Human-computer interaction projects.

## 🔮 Future Scope

* Add more hand gestures for additional controls.
* Add pause and resume presentation functionality.
* Add gesture-based laser pointer control.
* Add slide-selection functionality.
* Improve gesture recognition accuracy.
* Add voice command integration.
* Add support for multiple presentation software.
* Develop a graphical user interface.
* Add gesture customization options.

## ⚠️ Important Notes

* A working webcam is required.
* The `Presentation` folder must be present in the same directory as `main.py`.
* Presentation slide images should be stored inside the `Presentation` folder.
* Required Python libraries must be installed before running the project.
* The project works best in a well-lit environment.
* Make sure the presentation window is active while controlling slides.

## 👨‍💻 Author

**Aditya Chaurasiya**

## 📌 Project Type

College Major Project / Computer Vision Project / Artificial Intelligence Project

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a star on GitHub.
