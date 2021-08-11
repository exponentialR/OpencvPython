import cv2

#############################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("cascades/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255, 0, 255)
###############################################

cap = cv2.VideoCapture("data/lane_video.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1





# import cv2
#
# import numpy as n
# # fh = 480
# # fw = 640
# #cap = cv2.VideoCapture(0)
# # cap.set(3, fw)
# # cap.set(4, fh)
# # cap.set(10, 100)
# cas_path = 'cascades/haarcascade_russian_plate_number.xml'
# pci = 'data/platenumber.jpg'
# mA = 500
#
#
# # while True:
# #     _, img = cap.read()
# pc = cv2.CascadeClassifier(cas_path)
# img = cv2.imread(pci)
# imgtoGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# pn = pc.detectMultiScale(imgtoGray, 1.1, 4)
# for (x, y, w, h) in pn:
#     area = w*h
#     if area > mA:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
#         cv2.putText(img, "Plate Number", (x, y-5), cv2.FONT_HERSHEY_DUPLEX, 1,(255, 0, 0))
#         Aoi = img[y:y+h, x:x+w]
#         cv2.imshow('Area of Interest', Aoi)
#
# cv2.imshow('Result', img)
# cv2.waitKey(0)
#     #if cv2.waitKey(1) & 0xFF ==ord ('q'):
#         #break
