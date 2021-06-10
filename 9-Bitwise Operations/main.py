# Bitwise Operations are useful when working with masks

import cv2

img1=cv2.imread('../Sample Images/messi.jpg')
img2=cv2.imread('../Sample Images/lena.jpg')

print(img1.shape)
print(img2.shape)

img1=cv2.resize(img1,(512,512))
print(img1.shape)
print(img2.shape)

cv2.imshow('Image 1',img1)
cv2.imshow('Image 2',img2)

# sizes of both the images should be same
# bitwise_and works same as logical and
bitAnd=cv2.bitwise_and(img1,img2)
cv2.imshow('And Image',bitAnd)

# bitwise_or
bitOr=cv2.bitwise_or(img1,img2)
cv2.imshow('Or Image',bitOr)

bitNot1=cv2.bitwise_not(img1)
cv2.imshow('Not Image1',bitNot1)

bitNot2=cv2.bitwise_not(img2)
cv2.imshow('Not Image2',bitNot2)

bitXor=cv2.bitwise_xor(img1,img2)
cv2.imshow('XOR Image',bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()
