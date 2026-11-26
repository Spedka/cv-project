import cv2
import os
import numpy as np

template_path = os.path.join("data", "template1.png")
target_path = os.path.join("data", "target.jpeg")
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
target_gray = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE)
target_color = cv2.cvtColor(target_gray, cv2.COLOR_GRAY2BGR)

result = cv2.matchTemplate(target_gray, template, cv2.TM_CCOEFF_NORMED)

print(result.shape)
print(target_gray.shape)
print(template.shape)
print(result.min())
print(result.max())

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(max_val)

h, w = template.shape

threshold = 0.8

locations = np.where(result >= threshold)

print(locations)

pt1 = max_loc
pt2 = (max_loc[0] + w, max_loc[1] + h)
color = (0, 255, 0)
thickness = 2

target_color = cv2.rectangle(target_color, pt1, pt2, color, thickness)

cv2.namedWindow("Window", cv2.WINDOW_NORMAL)

for pt in zip(*locations[::-1]):
    cv2.rectangle(target_color, pt, (pt[0] + w, pt[1] + h), color, thickness)

cv2.imshow("Window", target_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
