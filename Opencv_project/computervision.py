import cv2

img = cv2.imread("C:/Users/Zeus/Documents/quarantineplaybook/Opencv_project/cv2.jpeg")
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
cv2.waitKey(0)