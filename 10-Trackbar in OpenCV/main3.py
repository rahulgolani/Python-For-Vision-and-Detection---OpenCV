import cv2

def trackValue(x):
    print(x)

cv2.namedWindow('Image Window')
cv2.createTrackbar("Toggle",'Image Window',0,1,trackValue)

while True:
    img=cv2.imread('../Sample Images/messi.jpg')
    
    s=cv2.getTrackbarPos("Toggle",'Image Window')

    if s==0:
        pass
    else:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Image Window',img)
    keyPressed=cv2.waitKey(1)
    if keyPressed==27:
        break

cv2.destroyAllWindows()
