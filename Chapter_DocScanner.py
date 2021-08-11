import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
width_img = 400
height_img = 640



cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)



def preProcessing(img ):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 50,50)
    kernel = np.ones((3,3))
    imgDila = cv2.dilate(imgCanny, kernel, iterations = 2)
    imagThresh = cv2.erode(imgDila, kernel, iterations = 1)

    return imagThresh





def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        area = cv2.contourArea(cont)
        #print(area)
        if area > 5000:
            #cv2.drawContours(Contour_img, cont, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cont, True)
            approx = cv2.approxPolyDP(cont, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(Contour_img, biggest, -1, (255, 0, 0), 20)

    return biggest




def reorder(mypoints):
    mypoints = mypoints.reshape((4,2))
    newpoints = np.zeros((4,1,2), np.int32)
    wi = mypoints.sum(1)
    #print('added', wi)

    newpoints[0] = mypoints[np.argmin(wi)]
    newpoints[3] = mypoints[np.argmax(wi)]
    #print('newpoints', newpoints)
    diff = np.diff(mypoints, axis =1)
    newpoints[1] = mypoints[np.argmin(diff)]
    newpoints[2] = mypoints[np.argmax(diff)]

    #print('New points', newpoints)
    return newpoints





def getWarp(img, biggest):
    reorder(biggest)
    print(biggest.shape)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width_img, 0], [0, height_img], [width_img, height_img]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width_img, height_img))
    img_to_crop = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
    cropped_image = cv2.resize((imgCropped, (width_img, height_img)))
    return cropped_image



while True:
    success, img = cap.read()
    cv2.resize(img, (width_img, height_img))
    Contour_img = img.copy()
    imagThres = preProcessing(img)
    biggest = getContours(imagThres)
    print(biggest)
    imag_warped = getWarp(img, biggest)
    cv2.imshow("Output frame", imag_warped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break