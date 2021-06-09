# Get the color of a particluar pixel in a separate window

import cv2
import numpy as np

def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        myColorImage=np.zeros((512,512,3),np.uint8)
        myColorImage[:]=[blue,green,red]
        cv2.imshow("Color",myColorImage)

img=cv2.imread('../Sample Images/lena.jpg',1)
cv2.imshow('Image Window',img)
cv2.setMouseCallback('Image Window',clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
