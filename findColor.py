import cv2
import numpy as np

cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

def empty(a):
    pass

cv2.namedWindow("Color Picker")
cv2.resizeWindow("Color Picker", 640, 240)
cv2.createTrackbar("hue min", "Color Picker", 0, 179, empty)
cv2.createTrackbar("sat min", "Color Picker", 0, 255, empty)
cv2.createTrackbar("val min", "Color Picker", 0, 255, empty)
cv2.createTrackbar("hue max", "Color Picker", 179, 179, empty)
cv2.createTrackbar("sat max", "Color Picker", 255, 255, empty)
cv2.createTrackbar("val max", "Color Picker", 255, 255, empty)

while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("hue min", "Color Picker")
    h_max = cv2.getTrackbarPos("hue max", "Color Picker")
    s_min = cv2.getTrackbarPos("sat min", "Color Picker")
    s_max = cv2.getTrackbarPos("sat max", "Color Picker")
    v_min = cv2.getTrackbarPos("val min", "Color Picker")
    v_max = cv2.getTrackbarPos("val max", "Color Picker")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()