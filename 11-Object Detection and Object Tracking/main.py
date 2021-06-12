'''
HSV-(Hue/Saturation/Value)

Hue corresponds to the color pigments, you can select any color from range 0-255
Saturation is the amount of depth of that color(dominance of the hue) 0-255
Value is the brightness of the color 0-255

RGB corresponds to the color luminiscance, we cannot separate color details based on luminiscance
therfore we use HSV for color separation

'''

# Detecting a particular color balls in the image

import cv2
import numpy as np

def trackValue(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('lh','Tracking',0,255,trackValue)
cv2.createTrackbar('ls','Tracking',0,255,trackValue)
cv2.createTrackbar('lv','Tracking',0,255,trackValue)
cv2.createTrackbar('uh','Tracking',255,255,trackValue)
cv2.createTrackbar('us','Tracking',255,255,trackValue)
cv2.createTrackbar('uv','Tracking',255,255,trackValue)

while True:
    img=cv2.imread('../Sample Images/balls.png')

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('lh','Tracking')
    ls=cv2.getTrackbarPos('ls','Tracking')
    lv=cv2.getTrackbarPos('lv','Tracking')
    uh=cv2.getTrackbarPos('uh','Tracking')
    us=cv2.getTrackbarPos('us','Tracking')
    uv=cv2.getTrackbarPos('uv','Tracking')

    # mask used to separate the coloured balls according to the hsv range values
    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,lb,ub)

    # applying the mask to the image
    res=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('Image Window',img)
    cv2.imshow('Mask Window',mask)
    cv2.imshow('Result Window',res)

    keyPressed=cv2.waitKey(1)
    if keyPressed==27:
        break

cv2.destroyAllWindows()
