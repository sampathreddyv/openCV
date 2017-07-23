import numpy as np
import cv2

img = cv2.imread('jurassic_world.jpg', cv2.IMREAD_COLOR)

img[55, 55] = [255, 255, 255]
px = img[55, 55]

img[100:150, 100:150] = [255, 255, 255]

faces = img[25:75, 25:75]

img[0:50, 0:50] = faces

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

