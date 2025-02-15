#Importing modules
import cv2

image=cv2.imread("image.png")
cv2.imshow("studio",image)

#Creating a greyscale
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Showing the greyscale image
cv2.imshow("grey studio",grey_image)

#Creating an inverted image
inverted_image=255-grey_image

#Showing the inverted image
cv2.imshow("Inverted colors cause why not",inverted_image)

#Blurring using gaussian
blurredimage=cv2.GaussianBlur(inverted_image,(21,21),0)
cv2.imshow("Sehaj with no glasses",blurredimage)


#Inverting the blurred image
inverted_blurred=255-blurredimage
pencilsketch=cv2.divide(grey_image,inverted_blurred,scale=256.0)
cv2.imshow("Pencil sketch",pencilsketch)
cv2.waitKey(0)