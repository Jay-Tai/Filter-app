#Importing modules
import cv2
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print("""
      
      WELCOME TO THE FILTER APP
      Please enter the file name that you would like to edit. Make sure that the file is in double quotations, and is in the project folder. Make sure that the file is a JPG, or PNG file.""")
userfile=input("Enter the file name here: ")

image=cv2.imread(userfile)
cv2.imshow("your image",image)
cv2.waitKey(5000)
def mainapp():
    #Defining checkfile
    def checkfile():
        userfileok=input("""Is this the file that you would like to use?
                        Y=Yes
                        N=No
                        Your input: """)
        if userfileok=="y" or userfileok=="Y":
            print("Thank you for confirming. We will now start with the photo editing. Please give a moment to load.")
        elif userfileok=="n" or userfileok=="N":
            print("Please restart the code in order to retry.")
        else:
            print("Invalid input. Please retry. Will automatically restart in 2 seconds.")
            time.sleep(2)
            checkfile()
    checkfile()
    for i in range(0,101):
        print(Style.BRIGHT + Fore.YELLOW + f"\rProgress: {i}%",end="")
        time.sleep(0.07)
    print(Style.BRIGHT + Fore.YELLOW + "Configuring...")
    time.sleep(3)
    #Defining filter variations
    print("""Please select one of the filer options:
        1) Greyscale
        2) Inverted colors
        3) Pencil sketch
        4) Red, Green, and Blue only""")
    filteroptioninput=input("Please enter the number of your filer right here: ")
    if filteroptioninput=="1" or filteroptioninput=="2" or filteroptioninput=="3" or filteroptioninput=="4":
        print("Please give the system a little bit to process your request")
        if filteroptioninput=="1":
            filteredimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        elif filteroptioninput=="2":
            filteredimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            filteredimage=255-filteredimage
        elif filteroptioninput=="3":
            grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            inverted_image=255-grey_image
            blurredimage=cv2.GaussianBlur(inverted_image,(21,21),0)
            inverted_blurred=255-blurredimage
            pencilsketch=cv2.divide(grey_image,inverted_blurred,scale=256.0)
            filteredimage=pencilsketch
        elif filteroptioninput=="4":
            filteredimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        for x in range(0,101):
            print(Style.BRIGHT + Fore.YELLOW + f"\rProcessing ({x}%)",end="")
            time.sleep(0.1)
        print(Style.BRIGHT + Fore.LIGHTRED_EX + "Loading image...")
        time.sleep(1)
        print("Here is your photo with the filter:")
        cv2.imshow("Your filtered image",filteredimage)
        cv2.waitKey(5000)
        filteragaininput=input("Would you like to add a new filter to your original image?\nY=Yes\nN=No")
        if filteragaininput=="Y" or filteragaininput=="y" or filteragaininput=="n" or filteragaininput=="N":
            if filteragaininput=="y" or filteragaininput=="Y":
                print("Processing your request...")
                mainapp()
        else:
            print("That is not an answer. Please type Y, or N.")
            mainapp()
    else:
        print("Invalid input. Please restart the code to try again")


#Executing code
mainapp()