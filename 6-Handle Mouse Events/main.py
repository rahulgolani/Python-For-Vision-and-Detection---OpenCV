#Handle Mouse Events
import cv2
import numpy as np

# grabbing all the events in cv2
events=[i for i in dir(cv2) if 'EVENT' in i]
for i in events:
    print(i)

# a callback function which is called when the mouse events are performed
# parameters-eventName,x coordinate, y coordinate, flags, param
def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        text=f"{x} , {y}"
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,text,(x,y),font,1,(0,0,255),1)
        cv2.imshow("Image Window",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        # getting the BGR channel of the image
        blue=img[y,x,0]# y,x, channel index
        green=img[y,x,1]
        red=img[y,x,2]
        text=f"{blue},{green},{red}"
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,text,(x,y),font,1,(255,0,0),1)
        cv2.imshow("Image Window",img)

# creating a black image
img=np.zeros((512,512,3),np.uint8)
# img=cv2.imread('../Sample Images/lena.jpg')
cv2.imshow('Image Window',img)

# listens to the mouse events and calls the callback function
cv2.setMouseCallback("Image Window",clickEvent)


cv2.waitKey(0)
cv2.destroyAllWindows()
