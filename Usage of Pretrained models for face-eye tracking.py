import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
img=cv2.imread("Additional Resources/lena.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
faces = faceCascade.detectMultiScale(imgGray,None ,4)
eyes = eyeCascade.detectMultiScale(imgGray,None ,4)

webc= cv2.VideoCapture(0)
webc.set(3,640)
webc.set(4,480)

while True:
    success, img = webc.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, None, 4)
    eyes = eyeCascade.detectMultiScale(imgGray, None, 4)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for x,y,w,h in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Result",img)
    cv2.waitKey(10)