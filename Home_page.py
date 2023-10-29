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
win.configure(background="black",border=2)
win.resizable(False,False)

welcome_label = tk.Label(master=win, text="", fg="white", bg="black", font="verdana 26 bold")
sentence ="HEY!!, Welcome into  the  Fun  Zone"
welcome_label.pack(pady=30)
frame = tk.Frame(master=win,highlightbackground="white", highlightthickness=5, background="pink")
frame.pack(pady=30)


# Open and resize all the images using PIL
original_bmi_image = Image.open("bmi_img.png")
resized_bmi_image = original_bmi_image.resize((150, 150))
original_convertor_image = Image.open("Convertor.png")
resized_convertor_image = original_convertor_image.resize((150,150))
original_calculator_image = Image.open("Calculator.png")
resized_calculator_image = original_calculator_image.resize((150,150))
original_textUtils_image = Image.open("text_utils.png")
resized_textUtils_image = original_textUtils_image.resize((150,150))

# Convert the resized image to PhotoImage format
bmi_img = ImageTk.PhotoImage(resized_bmi_image)
bmi = tk.Button(master=frame, image=bmi_img, bg="black", fg="white", width="150", height="150",border="3", command=BMI)
bmi.image = bmi_img  # This line is important to prevent the image from being garbage collected
bmi_label=tk.Button(master=frame, text="BMI Calculator", border=3, font="verdana 10 bold", command=BMI).place(x=120,y=220)
bmi.grid(row=0, column=0, pady=50, padx=100)

convertor_img=ImageTk.PhotoImage(resized_convertor_image)
convertor = tk.Button(master=frame,image=convertor_img, bg="black", fg="white", width="150", height="150",border="3", command=unit_convertor)
convertor.image = bmi_img  # This line is important to prevent the image from being garbage collected
convertor_label=tk.Button(master=frame, text="Unit Convertor", border=3, font="verdana 10 bold", command=unit_convertor).place(x=480,y=220)
convertor.grid(row=0, column=1, pady=2, padx=100)

calculator_img=ImageTk.PhotoImage(resized_calculator_image)
basic_calculator = tk.Button(master=frame, image=calculator_img, bg="black", fg="white", width="150", height="150",border="3", command=calculator)
basic_calculator.image = bmi_img  # This line is important to prevent the image from being garbage collected
calculator_label=tk.Button(master=frame, text="Basic Calculator", border=3, font="verdana 10 bold", command=calculator).place(x=120,y=480)
basic_calculator.grid(row=2, column=0, pady=50)

textUtils_img=ImageTk.PhotoImage(resized_textUtils_image)
text_utils = tk.Button(master=frame, image=textUtils_img, bg="black", fg="white", width="150", height="150",border="3", command=playWithText)
text_utils.image = bmi_img  # This line is important to prevent the image from being garbage collected
textUtils_label=tk.Button(master=frame, text="Text Utils", border=3, font="verdana 10 bold", command=playWithText).place(x=500,y=480)
text_utils.grid(row=2, column=1, pady=2)
update_label()

# run event loop
win.mainloop()
