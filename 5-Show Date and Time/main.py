# Show Current Date and Time on a live video

import cv2
import datetime

cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    if ret:

        text=str(datetime.datetime.now())
        font=cv2.FONT_HERSHEY_SIMPLEX
        # assiging means Writing
        frame=cv2.putText(frame,text,(10,100),font,1,(255,255,0),3)

        cv2.imshow('Window',frame)

        keyPressed=cv2.waitKey(1)
        if keyPressed==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
