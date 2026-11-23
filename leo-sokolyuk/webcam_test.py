import cv2
import sys
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: could not access webcam")
else:
    print("Webcam accessed successfully")

ret, frame = cap.read()

print(frame)

if ret:
    cv2.imshow("Captured frame", frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
else:
    print("Could not capture frame")

