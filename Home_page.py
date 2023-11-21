import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import time
from PIL import Image, ImageTk

# defining Functions
def BMI():
   pass
def unit_convertor():
    # Implement Unit Converter functionality here
    pass

def calculator():
    # Implement Basic Calculator functionality here
    pass

def playWithText():
    # Implement Text Manipulation functionality here
    pass

def update_label():
    global current_index
    current_letter = sentence[current_index]
    welcome_label.config(text=welcome_label.cget("text") + current_letter)
    current_index += 1
    
    if current_index >= len(sentence):
        current_index = 0
        # Pause for 3 seconds when the entire string is displayed
        win.after(500, clear_label)
    else:
        win.after(50, update_label)  # Schedule the update after 100 milliseconds (0.1 second)

# Function to clear the label text
def clear_label():
    welcome_label.config(text="")
    win.after(100, update_label)
current_index=0

# make home window
win = tk.Tk()
win.title("Fun Zone")
win.geometry("800x800")
win.resizable(False,False)

#setting background image
original_home_image= Image.open("background_img.png")
resized_home_image= original_home_image.resize((800,800))
# Convert the resized image to PhotoImage format
home_img= ImageTk.PhotoImage(resized_home_image)
background_widget= tk.Label(master=win,image=home_img)
background_widget.image=home_img # This line is important to prevent the image from being garbage collected
background_widget.grid(row=0,column=0)

welcome_label = tk.Label(master=win, text="", fg="white", bg="black", font="verdana 26 bold")
sentence ="HEY!!, Welcome into  the  Fun  Zone"
welcome_label.place(x=50,y=30)

# Open and resize all the images using PIL
original_bmi_image = Image.open("bmi_img.png")
resized_bmi_image = original_bmi_image.resize((150, 150))
original_convertor_image = Image.open("Convertor.png")
resized_convertor_image = original_convertor_image.resize((150,150))
original_calculator_image = Image.open("Calculator.png")
resized_calculator_image = original_calculator_image.resize((150,150))
original_textUtils_image = Image.open("text_utils.png")
resized_textUtils_image = original_textUtils_image.resize((150,150))

bmi_img = ImageTk.PhotoImage(resized_bmi_image)
bmi = tk.Button(master=win, image=bmi_img, bg="black", fg="white", width="150", height="150",border="3", command=BMI)
bmi.image = bmi_img  # This line is important to prevent the image from being garbage collected
bmi_label=tk.Button(master=win, text="BMI Calculator", border=3, font="verdana 10 bold", command=BMI).place(x=120,y=320)
bmi.place(x=100,y=150)

convertor_img=ImageTk.PhotoImage(resized_convertor_image)
convertor = tk.Button(master=win,image=convertor_img, bg="black", fg="white", width="150", height="150",border="3", command=unit_convertor)
convertor.image = bmi_img  # This line is important to prevent the image from being garbage collected
convertor_label=tk.Button(master=win, text="Unit Convertor", border=3, font="verdana 10 bold", command=unit_convertor).place(x=520,y=320)
convertor.place(x=500,y=150)

calculator_img=ImageTk.PhotoImage(resized_calculator_image)
basic_calculator = tk.Button(master=win, image=calculator_img, bg="black", fg="white", width="150", height="150",border="3", command=calculator)
basic_calculator.image = bmi_img  # This line is important to prevent the image from being garbage collected
calculator_label=tk.Button(master=win, text="Basic Calculator", border=3, font="verdana 10 bold", command=calculator).place(x=115,y=620)
basic_calculator.place(x=100,y=450)

textUtils_img=ImageTk.PhotoImage(resized_textUtils_image)
text_utils = tk.Button(master=win, image=textUtils_img, bg="black", fg="white", width="150", height="150",border="3", command=playWithText)
text_utils.image = bmi_img  # This line is important to prevent the image from being garbage collected
textUtils_label=tk.Button(master=win, text="Text Utils", border=3, font="verdana 10 bold", command=playWithText).place(x=540,y=620)
text_utils.place(x=500,y=450)
update_label()

# run event loop
win.mainloop()
