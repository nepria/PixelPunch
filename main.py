import cv2
from FindingBallons import *
from detectHit import detectHit

img = cv2.imread('test.png')
print('Shape', img.shape)
imgBallons = findBallons(img)
# print('hehe', imgBallons)
img = detectHit(img, imgBallons)

imgBallons = cv2.resize(img, (0,0), None, 0.5, 0.5)

cv2.imshow("Output", imgBallons)
cv2.waitKey(0)