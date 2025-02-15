#Importing modules
import cv2

image=cv2.imread("shrek.png")
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR5552RGBA)
cv2.imshow("mr shrek",grey_image)
cv2.waitKey(0)