import cv2

# VideoCapture object is used to work with videos
# in argument it takes either the video file name or the device index of the computer's camera which is mostly 0
cap=cv2.VideoCapture(0)

# VideoWriter is used to save the video,arguments -> filename,fourcc code, frames per second and size of the frame
fourcc=cv2.VideoWriter_fourcc(*'XVID') #check more on fourcc codec codes
out=cv2.VideoWriter('../Sample Images/output.mp4',fourcc,20,(640,480))

# Some Properties->

# cap.isOpened() -> checks if the device index is correct or the path of the video is correct
# if isOpened() return false then you can manually open the source using cap.open()
# other properties can be fetched using cap.get(property_code) property_code available in documentation

while cap.isOpened():
    # read reads the frame
    ret,frame=cap.read()

    if ret:
        # if frame avaiable, write

        out.write(frame)

        # cap.read returns true if the frame is available and boolean value is stored in ret and frame is stored in frame

        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # to convert the frame in other color codes use cvtColor(inputSource,conversion_code)
        grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # cv2.imshow('Frame Window',frame)
        cv2.imshow('Frame Window',grayFrame)

        keyPressed=cv2.waitKey(1)
        if keyPressed==ord('q'):
            break
    else:
        break

cap.release()
# important to release the VideoCapture Object once used

out.release()

# destroy all the windows
cv2.destroyAllWindows()
