import cv2
import numpy as np

img = cv2.imread('jurassic_world.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (15, 25), (150, 150), (0, 255, 0), 3)
cv2.rectangle(img, (15, 25), (150, 150), (0, 255, 0), 3)
cv2.circle(img, (100,63), 55, (0, 255, 0), 1)

pts = np.array([[10, 5], [20, 30], [70, 20], [500, 10]], np.int32)
cv2.polylines(img, [pts], False, (0, 255, 0), 1)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV akjnsd!', (0, 130), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
