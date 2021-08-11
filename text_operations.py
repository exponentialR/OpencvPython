import cv2
import numpy as np
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
#img[200:300, 100:300] = (255, 120, 111)
cv2.line(img, (100, 0), (img.shape[1], img.shape[0]), (0, 0, 255),4)
cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 0), cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255, 0, 0), cv2.FILLED)
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 100, 100), 2)
cv2.imshow("Kernel Image", img)





cv2.waitKey(0)