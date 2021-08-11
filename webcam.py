import cv2
print("Package Imported")

#img = cv2.imread("Resources/at_the_park.jpg")
#cv2.imshow("Image display", img)
#cv2.waitKey(0)

#cap = cv2.VideoCapture("Resources/lane_video.mp4")

cap =  cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Output Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



