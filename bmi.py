import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import time
from PIL import Image, ImageTk
from tkinter import messagebox
import time

#define all necessary functions
def goto_home():
    pass

def reset():
    h.set("")
    m.set("")
    bmi_str.set("")
    compliment_str.set("")

def result():
    compliment=["Warning!!!, You are very Underweight or possibly Malnourished","Congratulation, You have a Healthy Weight","You are Overweight","Warning!!!, You are Obese","Warning!!!, Please Input Valid data"]
    try:
        weight=float(m.get())
        height=float(h.get())
        if weight<=0 and height<=0:
            messagebox.showwarning("Invalid Input", "Weight and height must have positive values.")
        elif weight<=0 and height>=0:
            messagebox.showwarning("Invalid Input", "Weight must have positive values.")
        elif weight>=0 and height<=0:
            messagebox.showwarning("Invalid Input", "Height must have positive values.")
        else:
            bmi_calculation=round((weight/(height**2)),2)
            if(bmi_calculation<18.5):
                compliment_str.set(compliment[0])  
            elif bmi_calculation>=18.5 and bmi_calculation<25:
                compliment_str.set(compliment[1])  
            elif bmi_calculation>=25 and bmi_calculation<30:
                compliment_str.set(compliment[2])    
            elif bmi_calculation>=30:
                compliment_str.set(compliment[3])    
            else:
                compliment_str.set(compliment[4])    
            bmi_str.set(str(bmi_calculation))
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid numerical values for weight and height.")
    
def update1_label():
    global current_index
    current_letter = sentence[current_index]
    heading_label.config(text=heading_label.cget("text") + current_letter)
    current_index += 1
    
    if current_index >= len(sentence):
        current_index = 0
        # Pause for 3 seconds when the entire string is displayed
        win.after(500, clear_label)
    else:
        win.after(50, update1_label)  # Schedule the update after 100 milliseconds (0.1 second)

# Function to clear the label text
def clear_label():
    heading_label.config(text="")
    win.after(100, update1_label)
current_index=0

#make window
win=tk.Tk()
win.title("BMI Calculator")
win.geometry("800x600")
win.resizable(False,False)

#setting background image
original_bmibg_image= Image.open("bmi_bg.webp")
resized_bmibg_image= original_bmibg_image.resize((800,600))
# Convert the resized image to PhotoImage format
bmibg_img= ImageTk.PhotoImage(resized_bmibg_image)
bmibg_widget= tk.Label(master=win,image=bmibg_img)
bmibg_widget.image=bmibg_img # This line is important to prevent the image from being garbage collected
bmibg_widget.place(x=0,y=0)

home_button=tk.Button(master=win, text="HOME", font="verdana 10 bold", bg="white", fg="black", border="3", command=goto_home).place(anchor=NW)

title_label=tk.Label(master=win, text="BMI Calculator", font="verdana 30 bold", bg="black", fg="green", highlightbackground="green", highlightthickness=3).pack(pady=20)
heading_label=tk.Label(master=win, text="", font="verdana 20", bg="black", fg="white")
sentence ="Get Your Body Mass Index"
heading_label.pack(pady=10)

frame1=tk.Frame(master=win,highlightbackground="yellow", highlightthickness=5)
frame1.configure(background="white")
frame1.pack(pady=20)

#take weight and height from the user
mass_label=tk.Label(master=frame1,text="Enter your Weight in Kilograms : ", font="verdana 14 bold").grid(row=0,column=0,padx=20,pady=20)
m=tk.StringVar()
mass_entry=tk.Entry(master=frame1,textvariable=m, font="verdana 14 bold", border=3).grid(row=0,column=1,pady=20,padx=50)
height_label=tk.Label(master=frame1,text="Enter your Height in Meters : ", font="verdana 14 bold").grid(row=1,column=0,pady=20)
h=tk.StringVar()
height_entry=tk.Entry(master=frame1,textvariable=h, font="verdana 14 bold", border=3).grid(row=1,column=1,pady=20,padx=50)

#reset and submit button
result_button=tk.Button(master=frame1,text="Reset", font="verdana 14", bg="red", command=reset).grid(row=2,column=0,pady=40)
result_button=tk.Button(master=frame1,text="Submit", font="verdana 14", bg="green" , command=result).grid(row=2,column=1,pady=40)

#getting output BMI
bmi_str=StringVar()
output_label=tk.Label(master=win, text="", textvariable=bmi_str, font="verdana 20 bold", fg="blue", bg="black", highlightbackground="black", highlightthickness=3).pack()
compliment_str=StringVar()
compliment_label=tk.Label(master=win, text="", textvariable=compliment_str, font="verdana 14 bold", fg="white", bg="black").pack()
update1_label()

#run event loop
win.mainloop()
