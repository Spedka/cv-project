import cv2
import sys
import os
import time

lowBar = "Low Threshold"
highBar = "High Threshold"
sigmaBar = "Sigma Value"
kernelBar = "Kernel Size"
img_color = None

sigma_value = 1.2
kernel_size = (7,7)
low_threshold = 100
high_threshold = 200

esc = 27

live_edge_window = "Edge Map Feed"
live_color_window = "Colored Feed"
still_edge_window = "Edge map"
still_color_window = "Color image"
current_edge_window = None

def create_live_windows():
    cv2.namedWindow(live_edge_window, cv2.WINDOW_NORMAL)
    cv2.namedWindow(live_color_window, cv2.WINDOW_NORMAL)

def create_still_windows():
    cv2.namedWindow(still_edge_window, cv2.WINDOW_NORMAL)
    cv2.namedWindow(still_color_window, cv2.WINDOW_NORMAL)
    

def create_trackbars(window):
    cv2.createTrackbar(sigmaBar, window, round(sigma_value * 10), 30, sigma_value_adjust)
    cv2.createTrackbar(kernelBar, window, kernel_size[0] // 2, 15, kernel_size_adjust)
    cv2.createTrackbar(lowBar, window, low_threshold, 300, low_threshold_adjust)
    cv2.createTrackbar(highBar, window, high_threshold, 600, high_threshold_adjust)

def low_threshold_adjust(val):

    global low_threshold 
    low_threshold = val

    if low_threshold > high_threshold:
        cv2.setTrackbarPos(highBar, current_edge_window, low_threshold)

    if current_edge_window == still_edge_window:
        show_canny_image(img_color, low_threshold, high_threshold, still_edge_window, kernel_size, sigma_value)

def high_threshold_adjust(val):

    global high_threshold 
    high_threshold = val

    if high_threshold < low_threshold:
        cv2.setTrackbarPos(lowBar, current_edge_window, high_threshold)

    if current_edge_window == still_edge_window:
        show_canny_image(img_color, low_threshold, high_threshold, still_edge_window, kernel_size, sigma_value)

def sigma_value_adjust(val):
    global sigma_value 

    sigma_value = val/10

    if current_edge_window == still_edge_window:
        show_canny_image(img_color, low_threshold, high_threshold, still_edge_window, kernel_size, sigma_value)

def kernel_size_adjust(val):
    global kernel_size

    value = val * 2 + 1

    kernel_size = (value, value)

    if current_edge_window == still_edge_window:
        show_canny_image(img_color, low_threshold, high_threshold, still_edge_window, kernel_size, sigma_value)

def show_canny_image(image, low, high, window, kernel_value, sigma):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, kernel_value, sigma)
    cv2.imshow(window, cv2.Canny(img_gray_blur, low, high))

def webcam_feed():
    global current_edge_window
    current_edge_window = live_edge_window

    cap = cv2.VideoCapture(0)

    prev_time = time.perf_counter()

    if not cap.isOpened():
        sys.exit("Error: could not access webcam")
    
    print("Webcam accessed successfully")
    create_live_windows()

    create_trackbars(live_edge_window)

    while True:
        if cv2.getWindowProperty(live_edge_window, cv2.WND_PROP_VISIBLE) < 1 or cv2.getWindowProperty(live_color_window, cv2.WND_PROP_VISIBLE) < 1:
            break

        ret, frame = cap.read()

        if not ret:
            print("Frame read failed")
            break

        curr_time = time.perf_counter()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        copy = frame.copy()

        cv2.putText(copy, f"FPS: {int(fps)}", (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, lineType = cv2.LINE_AA)

        cv2.imshow(live_color_window, copy)

        show_canny_image(frame, low_threshold, high_threshold, live_edge_window, kernel_size, sigma_value)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q') or key == esc:
            break

    cap.release()

def still_feed():
    global current_edge_window
    current_edge_window = still_edge_window

    target_file = sys.argv[1]

    if not os.path.isfile(target_file):
        sys.exit(f"Error: File '{target_file}' does not exist")

    global img_color
    img_color = cv2.imread(target_file, cv2.IMREAD_COLOR)

    if img_color is None:
        sys.exit("Error: Image could not be loaded")

    create_still_windows()

    create_trackbars(still_edge_window)

    cv2.imshow(still_color_window, img_color)
    show_canny_image(img_color, low_threshold, high_threshold, still_edge_window, kernel_size, sigma_value)

    while True:
        if cv2.getWindowProperty(still_edge_window, cv2.WND_PROP_VISIBLE) < 1 or cv2.getWindowProperty(still_color_window, cv2.WND_PROP_VISIBLE) < 1:
            break

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q') or key == esc:
            break

def main():
    if len(sys.argv) < 2:
        webcam_feed()
    else:
        still_feed()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
