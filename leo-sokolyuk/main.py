import cv2

imgColor = cv2.imread("./data/image1.jpg", cv2.IMREAD_COLOR)
imgGray = cv2.imread("./data/image1.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("image1", imgColor)
cv2.imshow("image2", imgGray)

cv2.waitKey(0)
