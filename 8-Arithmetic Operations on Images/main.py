import cv2

img=cv2.imread('../Sample Images/messi.jpg',1)

print(img.shape)#gives the shape of the image in tuple (row,col,channels)
print(img.size) #row*column*channels
print(img.dtype) #datatype

#splitting the image in 3 channels
# b,g,r=cv2.split(img)

# if you have the bgr channels so you can merge the channels
# img=cv2.merge((b,g,r))
'''
# region of interest
# getting the coordinates of the ball and placing the ball somewhere else
# [y:x,y:x] upperleft, bottomright
ball=img[290:331,339:396]
# cv2.imshow('Ball',ball)
img[275:45,322:135]=ball

def clickEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        # 326 285
        # 403 335
        # target -> 61 284
                    # 139 318
'''

# Adding two images
#make sure the size of both the images are same

img2=cv2.imread('../Sample Images/lena.jpg')

# source,size
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

# image1, image2
finalImage=cv2.add(img,img2)

# Weighted Add - if you want to give weight to the images
# source1,alpha-weight of source1,source2,beta=weight of source2,gamma
weightedFinalImage=cv2.addWeighted(img, 0.6, img2, 0.4, 0)
cv2.imshow('Weighted Image',weightedFinalImage)

cv2.imshow('Final Image',finalImage)

cv2.imshow('Image Window',img)

# cv2.setMouseCallback('Image Window',clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
