import cv2

img=cv2.imread('../Sample Images/lena.jpg',1)

# draw line
# cv2.line(image variable,starting coordinates, ending coordinates, color of line (BGR), thickness)
img=cv2.line(img,(0,0),(250,250),(0,0,255),5)

# arrowedLine
img=cv2.arrowedLine(img,(100,100),(500,100),(0,255,0),5)

# rectangle
# if thickness value is -1 then the color fills the rectangle
# image variable,left top, right bottom, color,thickness
img=cv2.rectangle(img,(100,200),(500,400),(0,0,255),5)

# circle
# image variable,center, radius,color, thickness
img=cv2.circle(img,(240,240),200,(255,0,0),5)

# text
font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(image variable,text,starting point,fontface, font size,color, thickness)
img=cv2.putText(img,'Rahul',(100,500),font,3,(0,255,255),10)

cv2.imshow('Image Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
