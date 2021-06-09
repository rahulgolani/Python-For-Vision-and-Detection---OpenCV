# Using mouse clicks create a line connecting current and last point

import cv2
import numpy as np

prevCoordinate=None

# event=[i for i in dir(cv2) if 'EVENT' in i]
# for i in event:
#     print(i)

def clickEvent(event,x,y,flags,param):
    global prevCoordinate
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        if prevCoordinate!=None:
            cv2.line(img,prevCoordinate,(x,y),(0,255,255),1)
        prevCoordinate=(x,y)
        cv2.imshow("Image Window",img)

img=np.zeros((512,512,3),np.uint8)
cv2.imshow("Image Window",img)

cv2.setMouseCallback("Image Window",clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
