import cv2

image = cv2.imread('auto_2026-06-29_20-14-56.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imwrite('edges.jpg', edges)

cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()