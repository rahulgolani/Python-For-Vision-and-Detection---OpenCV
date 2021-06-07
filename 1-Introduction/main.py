# Read, Write and Show Images

import cv2
# cv2.imread(filename,flags)
# flags= 0-grayscale|1-color|-1-as it is including the alpha channel
img=cv2.imread('..\Sample Images\lena.jpg',0)
# img=cv2.imread('..\Sample Images\lena.jpg',1) #color image
# img=cv2.imread('..\Sample Images\lena.jpg',-1) #as it is including alpha channels
# prints the image in matrix form
print(img)

# cv2.imshow(name of window,image variable)
cv2.imshow('image_window',img)
# to hold the window for sometime use waitKey(milliseconds)
# cv2.waitKey(1000) #keybinding function
keyPressed = cv2.waitKey(0)  #now the window will not automatically disappear and it will wait for the user to close the window manually
# cv2.destroyAllWindows() or destroyWindow(window_name)
# compare against ASCII value of the key, 27 is for escape
if keyPressed==27:
    cv2.destroyAllWindows()
elif keyPressed == ord('s'):
    cv2.imwrite('../Sample Images/lena_copy.jpg',img)
    cv2.destroyAllWindows()

#Writing the image

# cv2.imwrite(filename,image variable)
# cv2.imwrite('../Sample Images/lena_copy.jpg',img)
