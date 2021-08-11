import cv2
path_casacade = 'Resources/haarcascade_frontalface_default.xml'
path_eye = 'Resources/haarcascade_eye_tree_eyeglasses.xml.xml'
faceCascade = cv2.CascadeClassifier(path_casacade)
eyeCascade = cv2.CascadeClassifier(path_eye)




cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Tracking Video', img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    cv2.waitKey(1)
    #cv2.waitKey(0)


