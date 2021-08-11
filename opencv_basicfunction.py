import cv2
import numpy as np
kernel = np.ones((3,3), np.uint8)
img = cv2.imread("data/lab_book.jpg")
img = cv2.resize(img, (360, 480))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9,9), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDilation, kernel, iterations =1)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Detected Edges", imgCanny)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Resized Output Image", img)
cv2.imshow("Dilated Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)

