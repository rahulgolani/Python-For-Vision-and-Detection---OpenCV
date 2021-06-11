#Using Switch using Trackbars
# Switches act as a 0/1 value

# Example -> Change the color only when the switch is turned ON

import cv2
import numpy as np

def trackValue(x):
    print(x)

img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow('Image Window')

cv2.createTrackbar('B','Image Window',0,255,trackValue)
cv2.createTrackbar('G','Image Window',0,255,trackValue)
cv2.createTrackbar('R','Image Window',0,255,trackValue)
cv2.createTrackbar('Switch','Image Window',0,1,trackValue)

while True:
    cv2.imshow('Image Window',img)
    keyPressed=cv2.waitKey(1)
    if keyPressed==27:
        break
    b=cv2.getTrackbarPos('B','Image Window')
    g=cv2.getTrackbarPos('G','Image Window')
    r=cv2.getTrackbarPos('R','Image Window')
    s=cv2.getTrackbarPos('Switch','Image Window')

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv2.destroyAllWindows()
