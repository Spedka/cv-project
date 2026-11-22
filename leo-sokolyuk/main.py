import cv2
import sys
import os

if len(sys.argv) < 2:
    sys.exit("Error: No file path \nUsage: python main.py <image file path>")

target_file = sys.argv[1] 

if not os.path.isfile(target_file):
    sys.exit(f"Error: File '{target_file}' does not exist.")

imgColor = cv2.imread(target_file, cv2.IMREAD_COLOR)

if imgColor is None:
    sys.exit("Error: Image could not be loaded")

imgGray = cv2.cvtColor(imgColor, cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (5,5), 1.2)
imgGrayBlurEdge = cv2.Canny(imgGrayBlur, 100, 200)

edgeMap = "Grayscale Blurred Edge Map"

cv2.imshow("Colored Image", imgColor)
cv2.imshow("Grayscale Image", imgGray)
cv2.imshow("Grayscale Blurred", imgGrayBlur)
cv2.imshow(edgeMap, imgGrayBlurEdge)

low_threshold = 100
high_threshold = 200

def show_canny_image(image, low, high, window):
    cv2.imshow(window, cv2.Canny(image, low, high))

def low_threshold_adjust(val):
    global low_threshold

    low_threshold = val

    if low_threshold > high_threshold:
        cv2.setTrackbarPos(highBar, edgeMap, low_threshold)

    show_canny_image(imgGrayBlur, low_threshold, high_threshold, edgeMap)

    

def high_threshold_adjust(val):
    global high_threshold
    
    high_threshold = val

    if high_threshold < low_threshold:
        cv2.setTrackbarPos(lowBar, edgeMap, high_threshold)

    show_canny_image(imgGrayBlur, low_threshold, high_threshold, edgeMap)

lowBar = "Low Threshold"
highBar = "High Threshold"

cv2.createTrackbar(lowBar, edgeMap, 100, 300, low_threshold_adjust)
cv2.createTrackbar(highBar, edgeMap, 200, 600, high_threshold_adjust)

while True:
    if cv2.getWindowProperty(edgeMap, cv2.WND_PROP_VISIBLE) < 1:
        break
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        break


cv2.destroyAllWindows()