import cv2
import numpy as np

cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

myColors = [[99, 69, 172, 127, 180, 255]] #in HSV
myColorvalues = [[255, 255, 0]] #in BGR
mypoints = [] #[x, y, colorID]
def findColor(img, myColors, myColorvalues):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHsv, lower, upper)
    x, y = getContours(mask)
    cv2.circle(imgResult, (x, y), 10, myColorvalues[count], cv2.FILLED)
    if x!=0 and y!=0:
        newPoints.append([x, y, count])
    count +=1
    #cv2.imshow("img", mask)
    return newPoints


def getContours(imgcont):
    contours, hierarchy = cv2.findContours(imgcont, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cont in contours:
        area = cv2.contourArea(cont)
        if area>500:
            #cv2.drawContours(imgResult, cont, -1, (255, 0, 0), 3)
            peri= cv2.arcLength(cont, True)
            approx = cv2.approxPolyDP(cont, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x +w//2, y

def drawoncanvas(mypoints, myColorvalues):
    for point in mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorvalues[point[2]], cv2.FILLED)
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorvalues)
    if len(newPoints) !=0:
        for newp in newPoints:
            mypoints.append(newp)
    if len(mypoints) !=0:
        drawoncanvas(mypoints, myColorvalues)

    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break