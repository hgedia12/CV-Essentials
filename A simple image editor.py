import cv2
import numpy as np

def empty(a):
    print(a)


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

cv2.createTrackbar("Hue min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat max","Trackbars",255,255,empty)
cv2.createTrackbar("Val min","Trackbars",0,255,empty)
cv2.createTrackbar("Val max","Trackbars",255,255,empty)



while True:
    img = cv2.imread("Resources/lambo.jpg")
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min","Trackbars")
    s_min = cv2.getTrackbarPos("Sat min","Trackbars")
    v_min = cv2.getTrackbarPos("Val min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue max","Trackbars")
    s_max = cv2.getTrackbarPos("Sat max","Trackbars")
    v_max = cv2.getTrackbarPos("Val max","Trackbars")
    lower =np.array([h_min,s_min,v_min])
    upper =np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imghsv,lower,upper)

    imgresult = cv2.bitwise_and(img,imghsv,mask=mask)
    cv2.imshow("Original", img)
    cv2.imshow("hi",imghsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("imgres",imgresult)
    cv2.waitKey(1)