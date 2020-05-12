import os
from tkinter import  *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('inkspot.ico')

image1 = ImageTk.PhotoImage(Image.open(os.path.join('pictures', 'rocks.jpg')))
image2 = ImageTk.PhotoImage(Image.open(os.path.join('pictures', 'flower.jpg')))
image3 = ImageTk.PhotoImage(Image.open(os.path.join('pictures', 'water.jpg')))
image4 = ImageTk.PhotoImage(Image.open(os.path.join('pictures', 'mountain.jpg')))
image5 = ImageTk.PhotoImage(Image.open(os.path.join('pictures', 'ocean.jpg')))

imageList = [image1, image2, image3, image4, image5]
status = Label(root, text = "Image 1 of {}".format(len(imageList)), bd=1, relief=SUNKEN, anchor=E)

label = Label(image=image1)
label.grid(row=0, column=0, columnspan=3)

def nextImg(imageNum):
    global label, backButton, nextButton 
    label.grid_forget()
    
    label = Label(image=imageList[imageNum-1])
    nextButton = Button(root, text = " > ", command=lambda: nextImg(imageNum + 1))
    backButton = Button(root, text = " < ", command=lambda: backImg(imageNum - 1))
    
    if imageNum == 5:
        nextButton = Button(root, text = " > ", state=DISABLED)
    
    label.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column = 0)
    nextButton.grid(row=1, column=2)
    
    status = Label(root, text = "Image {} of {}".format(imageNum, len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def backImg(imageNum):
    global label, backButton, nextButton
    label.grid_forget()
    
    label = Label(image=imageList[imageNum-1])
    nextButton = Button(root, text = " > ", command=lambda: nextImg(imageNum + 1))
    backButton = Button(root, text = " < ", command=lambda: backImg(imageNum - 1))
    
    if imageNum == 1:
        backButton = Button(root, text = " < ", state=DISABLED)
    
    label.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column = 0)
    nextButton.grid(row=1, column=2) 
    
    status = Label(root, text = "Image {} of {}".format(imageNum, len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

quitButton = Button(root, text = "Quit Program", command=root.quit)
backButton = Button(root, text = " < ", command=backImg, state=DISABLED)
nextButton = Button(root, text = " > ", command=lambda: nextImg(2))

backButton.grid(row=1, column = 0)
quitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()