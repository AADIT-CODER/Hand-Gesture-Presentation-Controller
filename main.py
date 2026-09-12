from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import time

# Parameters
width, height = 1280, 720  # Screen resolution
gestureThreshold = 300
folderPath = "Presentation"

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.9, maxHands=1)

# Variables
buttonPressed = False
gestureControl = False
imgNumber = 0
annotations = [[]]
annotationNumber = -1
annotationStart = False
hs, ws = 120, 213
zoomLevel = 1
lastGestureTime = 0
gestureCooldown = 1

# Toggle message variables
toggleMessage = ""
toggleMessageTime = 0
toggleMessageDuration = 3  # Seconds

# Load images
pathImages = sorted(os.listdir(folderPath), key=len)
imgList = [cv2.resize(cv2.imread(os.path.join(folderPath, img)), (width, height)) for img in pathImages]

# Fullscreen window
cv2.namedWindow("Slides", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Slides", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Get frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgCurrent = imgList[imgNumber].copy()

    # Zoom
    if zoomLevel != 1:
        h, w, _ = imgCurrent.shape
        newH, newW = int(h * zoomLevel), int(w * zoomLevel)
        imgCurrent = cv2.resize(imgCurrent, (newW, newH))
        startX, startY = (newW - width) // 2, (newH - height) // 2
        imgCurrent = imgCurrent[startY:startY + height, startX:startX + width]

    # Find hand
    hands, img = detectorHand.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    currentTime = time.time()

    if hands:
        hand = hands[0]
        cx, cy = hand["center"]
        fingers = detectorHand.fingersUp(hand)

        # Enable Gesture Control → (0,1,1,1,1)
        if fingers == [0, 1, 1, 1, 1] and currentTime - lastGestureTime >= gestureCooldown:
            gestureControl = True
            toggleMessage = "Toggle ON"
            toggleMessageTime = currentTime
            lastGestureTime = currentTime
            print(toggleMessage)

        # Disable Gesture Control → (1,1,1,1,1)
        if fingers == [1, 1, 1, 1, 1] and currentTime - lastGestureTime >= gestureCooldown:
            gestureControl = False
            toggleMessage = "Toggle OFF"
            toggleMessageTime = currentTime
            lastGestureTime = currentTime
            print(toggleMessage)

        if gestureControl and not buttonPressed and (currentTime - lastGestureTime >= gestureCooldown):
            # Left → [1, 0, 0, 0, 0]
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")
                buttonPressed = True
                if imgNumber > 0:
                    imgNumber -= 1
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                lastGestureTime = currentTime

            # Right → [0, 0, 0, 0, 1]
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                buttonPressed = True
                if imgNumber < len(imgList) - 1:
                    imgNumber += 1
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                lastGestureTime = currentTime

            # Draw Mode → [0, 1, 1, 0, 0]
            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(imgCurrent, (cx, cy), 12, (0, 0, 255), cv2.FILLED)

            # Annotation Start → [0, 1, 0, 0, 0]
            if fingers == [0, 1, 0, 0, 0]:
                if not annotationStart:
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                annotations[annotationNumber].append((cx, cy))
                cv2.circle(imgCurrent, (cx, cy), 12, (0, 0, 255), cv2.FILLED)
            else:
                annotationStart = False

            # Undo → [0, 1, 1, 1, 0]
            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True
                lastGestureTime = currentTime

            # Clear All → [1, 1, 0, 0, 0]
            if fingers == [1, 1, 0, 0, 0]:
                annotations = [[]]
                annotationNumber = -1
                print("Clear All Annotations")
                lastGestureTime = currentTime

            # Zoom In → [0, 0, 0, 0, 0]
            if fingers == [0, 0, 0, 0, 0]:
                zoomLevel = min(zoomLevel + 0.1, 2)
                print(f"Zoom In: {zoomLevel}")
                lastGestureTime = currentTime

            # Zoom Out → [1, 0, 0, 0, 1]
            if fingers == [1, 0, 0, 0, 1]:
                zoomLevel = max(zoomLevel - 0.1, 1)
                print(f"Zoom Out: {zoomLevel}")
                lastGestureTime = currentTime

    if buttonPressed:
        buttonPressed = False

    # Draw Annotations
    for annotation in annotations:
        for j in range(len(annotation)):
            if j != 0:
                cv2.line(imgCurrent, annotation[j - 1], annotation[j], (0, 0, 200), 12)

    # Draw toggle message (Top-left corner, green text)
    if toggleMessage and time.time() - toggleMessageTime <= toggleMessageDuration:
        cv2.putText(imgCurrent, toggleMessage, (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    elif time.time() - toggleMessageTime > toggleMessageDuration:
        toggleMessage = ""

    # Overlay camera
    imgSmall = cv2.resize(img, (ws, hs))
    imgCurrent[0:hs, width - ws: width] = imgSmall

    # Show
    cv2.imshow("Slides", imgCurrent)
    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()