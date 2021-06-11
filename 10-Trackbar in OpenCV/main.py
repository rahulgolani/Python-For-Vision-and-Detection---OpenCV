# Trackbars are used when you want to dynamically perform changes on the image at runtime

# Example 1-> Create A Color Picker
import cv2
import numpy as np

# callback function which is called when trackbar values are changed
def trackValue(x):
    print(x)

img=np.zeros((512,512,3),np.uint8)

# named window used to specify on which the trackbars are used
cv2.namedWindow('Image Window')

# (nameoftrakbar,window name, initial value, final value,callback function)
cv2.createTrackbar('B','Image Window',0,255,trackValue)
cv2.createTrackbar('G','Image Window',0,255,trackValue)
cv2.createTrackbar('R','Image Window',0,255,trackValue)

while True:
    cv2.imshow('Image Window',img)
    keyPressed=cv2.waitKey(1)
    if keyPressed==27:
        break

    # getting the values of the trackbar
    b=cv2.getTrackbarPos('B','Image Window')
    g=cv2.getTrackbarPos('G','Image Window')
    r=cv2.getTrackbarPos('R','Image Window')

    # changing the values of the pixels
    img[:]=[b,g,r]

cv2.destroyAllWindows()
