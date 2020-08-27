import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread("Resources/shapes.png")
img=cv2.resize(img,(540,360))
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgBlur=cv2.GaussianBlur(imgGrey,(7,7),1)
imgCanny=cv2.Canny(imgGrey,50,50)
imgBlank=np.zeros_like(img)

imgContour=img.copy()

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for ctr in contours:
        print(cv2.contourArea(ctr))
        cv2.drawContours(imgContour,ctr,-1,(255,0,0),2)
        peri=cv2.arcLength(ctr,True)
        print(peri)
        approx=cv2.approxPolyDP(ctr,0.02*peri,True)
        bruh=len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        if bruh==3:
            cv2.putText(imgContour,"Tri" , (x + (w // 2) - 10, y + (h // 2) - 10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5, (0, 0, 255), 2)


getContours(imgCanny)
imgStack=stackImages(0.6,([img,imgGrey,imgBlank],
                          [imgCanny,imgContour,imgBlank]))
cv2.imshow("Original",imgStack)
cv2.waitKey(0)