import cv2
import sys
import time

cap = cv2.VideoCapture(0)
winName = "Edge feed"

if not cap.isOpened():
    sys.exit("Error: could not access webcam")
else:
    print("Webcam accessed successfully")
    cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

lowBar = "Low Threshold"
highBar = "High Threshold"

def show_canny_image(image, low, high, window):
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgGrayBlur = cv2.GaussianBlur(imgGray, (5,5), 1.2)
    cv2.imshow(window, cv2.Canny(imgGrayBlur, low, high))

low_threshold = 100
high_threshold = 200

def low_threshold_adjust(val):
    global low_threshold

    low_threshold = val

    if low_threshold > high_threshold:
        cv2.setTrackbarPos(highBar, winName, low_threshold)


def high_threshold_adjust(val):
    global high_threshold
    
    high_threshold = val

    if high_threshold < low_threshold:
        cv2.setTrackbarPos(lowBar, winName, high_threshold)

cv2.createTrackbar(lowBar, winName, 100, 300, low_threshold_adjust)
cv2.createTrackbar(highBar, winName, 200, 600, high_threshold_adjust)

esc = 27

prev_time = time.perf_counter()

while True:
    if cv2.getWindowProperty(winName, cv2.WND_PROP_VISIBLE) < 1:
        break

    ret, frame = cap.read()

    if not ret:
        print("Frame read failed")
        break

    curr_time = time.perf_counter()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    copy = frame.copy()

    cv2.putText(copy, f"FPS: {int(fps)}", (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, lineType=cv2.LINE_AA)

    cv2.imshow("Colored feed", copy)
    
    show_canny_image(frame, low_threshold, high_threshold, winName)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q') or key == esc:
        break

cap.release()
cv2.destroyAllWindows()