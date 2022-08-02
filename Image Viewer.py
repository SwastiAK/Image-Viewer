# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:55:01 2022

@author: Swasti
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.geometry("600x600")
root.configure(background = "black")

label_image = Label(root, bg = "white", highlightthickness = 5)
label_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img_path = ""
def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Text File", filetypes = [("Image Files", "*jpg, *.gif *.png *.jpeg")])
    print(img_path)
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    label_image["image"] = img
    img.close()
    
btn = Button(root, text = "Open Image", font = ("Bookman Old Style",12), bg = "grey", fg = "white", command = openFile, relief = SOLID)
btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

root.mainloop()