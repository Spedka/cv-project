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

print(imgColor.shape)
print(imgGray.shape)

cv2.imshow("Colored Image", imgColor)
cv2.imshow("Grayscale Image", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()

