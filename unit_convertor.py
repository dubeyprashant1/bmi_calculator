import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import time
from PIL import Image, ImageTk
from tkinter import messagebox
import time

#defining all Global Variables
global fromUnit_options
global toUnit_options
global val
global fromUnit_clicked
global toUnit_clicked
global final_result

#defining all functions
def update2_label():
    global current_index
    current_letter = sentence[current_index]
    heading_label.config(text=heading_label.cget("text") + current_letter)
    current_index += 1
    
    if current_index >= len(sentence):
        current_index = 0
        # Pause for 3 seconds when the entire string is displayed
        win.after(500, clear_label)
    else:
        win.after(50, update2_label)  # Schedule the update after 100 milliseconds (0.1 second)

# Function to clear the label text
def clear_label():
    heading_label.config(text="")
    win.after(100, update2_label)
current_index=0

def set_measurement():
    global fromUnit_options
    global toUnit_options
    global val
    global fromUnit_clicked
    global toUnit_clicked
    set_label.config( text = measurement_clicked.get() )
    if(set_label.cget("text")=="Select Unit Category"):
        messagebox.showwarning("Invalid Selection","Please select any Category of Unit")
    else:
        if(set_label.cget("text")=="Mass"):
            #selecting which From_Convertor drop down option appears
            fromUnit_options=["select From unit","Kilograms","grams","milligram"]
            # datatype of menu text and initializing
            fromUnit_clicked = StringVar() 
            fromUnit_clicked.set( "select From unit" ) 

            # Create Dropdown menu 
            fromUnit_drop = OptionMenu( frame1 , fromUnit_clicked , *fromUnit_options ) 
            fromUnit_drop.grid(row=1,column=0,padx=10,pady=10) 
            
            #create Interchange Button
            rev_button=tk.Button(frame1,text="reverse", font="verdana 10 bold",border=3,bg="blue", command=reverse).place(x=180,y=100)
            
            #selecting which to_Convertor drop down option appears
            toUnit_options=["select To unit","Kilograms","grams","milligram"]
            # datatype of menu text and initializing
            toUnit_clicked = StringVar() 
            toUnit_clicked.set( "select To unit" ) 

            # Create Dropdown menu 
            toUnit_drop = OptionMenu( frame1 , toUnit_clicked , *toUnit_options ) 
            toUnit_drop.grid(row=1,column=1,padx=20) 
            
            #input integer/float value 
            val_label=tk.Label(master=frame1,text="Enter Value : ", fg="black",bg="white",font="verdana 14 bold").grid(row=2,column=0,padx=10,pady=20)
            val=tk.StringVar()
            val_entry=tk.Entry(master=frame1, textvariable=val, font="verdana 14 bold", border=3).grid(row=2,column=1,pady=10,padx=20)   
        
        elif(set_label.cget("text")=="Volume"):
            #selecting which From_Convertor drop down option appears
            fromUnit_options=["select From unit","Litre","Mililitre","Gallon"] 
            # datatype of menu text and initializing
            fromUnit_clicked = StringVar() 
            fromUnit_clicked.set( "select From unit" ) 

            # Create Dropdown menu 
            fromUnit_drop = OptionMenu( frame1 , fromUnit_clicked , *fromUnit_options ) 
            fromUnit_drop.grid(row=1,column=0,padx=10,pady=10)   

            #create Interchange Button
            rev_button=tk.Button(frame1,text="reverse", font="verdana 10 bold",border=3,bg="blue", command=reverse).place(x=180,y=100)
            
            #selecting which to_Convertor drop down option appears
            toUnit_options=["select To unit","Litre","Mililitre","Gallon"]
            # datatype of menu text and initializing
            toUnit_clicked = StringVar() 
            toUnit_clicked.set( "select To unit" ) 

            # Create Dropdown menu 
            toUnit_drop = OptionMenu( frame1 , toUnit_clicked , *toUnit_options ) 
            toUnit_drop.grid(row=1,column=1,padx=20)
            
            #input integer/float value 
            val_label=tk.Label(master=frame1,text="Enter Value : ",fg="black",bg="white", font="verdana 14 bold").grid(row=2,column=0,padx=10,pady=20)
            val=tk.StringVar()
            val_entry=tk.Entry(master=frame1, textvariable=val, font="verdana 14 bold", border=3).grid(row=2,column=1,pady=10,padx=20)
            
        elif(set_label.cget("text")=="Length"):
            #selecting which From_Convertor drop down option appears
            fromUnit_options=["select From unit","meter","centimeter","kilometer","feet","inches","miles"]
            # datatype of menu text and initializing
            fromUnit_clicked = StringVar() 
            fromUnit_clicked.set( "select From unit" ) 

            # Create Dropdown menu 
            fromUnit_drop = OptionMenu( frame1 , fromUnit_clicked , *fromUnit_options ) 
            fromUnit_drop.grid(row=1,column=0,padx=10,pady=10)
            
            #create Interchange Button
            rev_button=tk.Button(frame1,text="reverse", font="verdana 10 bold",border=3,bg="blue", command=reverse).place(x=180,y=100)
            
            #selecting which to_Convertor drop down option appears
            toUnit_options=["select To unit","meter","centimeter","kilometer","feet","inches","miles"]
            # datatype of menu text and initializing
            toUnit_clicked = StringVar() 
            toUnit_clicked.set( "select To unit" ) 

            # Create Dropdown menu 
            toUnit_drop = OptionMenu( frame1 , toUnit_clicked , *toUnit_options ) 
            toUnit_drop.grid(row=1,column=1,padx=20)
            
            #input integer/float value
            val_label=tk.Label(master=frame1,text="Enter Value : ",fg="black",bg="white", font="verdana 14 bold").grid(row=2,column=0,padx=10,pady=20) 
            val=tk.StringVar()
            val_entry=tk.Entry(master=frame1, textvariable=val, font="verdana 14 bold", border=3).grid(row=2,column=1,pady=10,padx=20) 
            
        elif(set_label.cget("text")=="Time"):
            #selecting which From_Convertor drop down option appears
            fromUnit_options=["select From unit","second","minute","hour","day","week","normal year","leap year"]
            # datatype of menu text and initializing
            fromUnit_clicked = StringVar() 
            fromUnit_clicked.set( "select From unit" ) 

            # Create Dropdown menu 
            fromUnit_drop = OptionMenu( frame1 , fromUnit_clicked , *fromUnit_options ) 
            fromUnit_drop.grid(row=1,column=0,padx=10,pady=10)
            
            #create Interchange Button
            rev_button=tk.Button(frame1,text="reverse", font="verdana 10 bold",border=3,bg="blue", command=reverse).place(x=180,y=100)
            
            #selecting which to_Convertor drop down option appears
            toUnit_options=["select To unit","second","minute","hour","day","week","normal year","leap year"]
            # datatype of menu text and initializing
            toUnit_clicked = StringVar() 
            toUnit_clicked.set( "select To unit" ) 
            
            #selecting which to_Convertor drop down option appears    
            # Create Dropdown menu 
            toUnit_drop = OptionMenu( frame1 , toUnit_clicked , *toUnit_options ) 
            toUnit_drop.grid(row=1,column=1,padx=20)
            
            #input integer/float value 
            val_label=tk.Label(master=frame1,text="Enter Value : ",fg="black",bg="white", font="verdana 14 bold").grid(row=2,column=0,padx=10,pady=20)
            val=tk.StringVar()
            val_entry=tk.Entry(master=frame1, textvariable=val, font="verdana 14 bold", border=3).grid(row=2,column=1,pady=10,padx=20)
            
        elif(set_label.cget("text")=="Temperature"):
            #selecting which From_Convertor drop down option appears
            fromUnit_options=["select From unit","fahrenheit","celsius","kelvin"]
            # datatype of menu text and initializing
            fromUnit_clicked = StringVar() 
            fromUnit_clicked.set( "select From unit" ) 

            # Create Dropdown menu 
            fromUnit_drop = OptionMenu( frame1 , fromUnit_clicked , *fromUnit_options ) 
            fromUnit_drop.grid(row=1,column=0,padx=10,pady=10)
            
            #create Interchange Button
            rev_button=tk.Button(frame1,text="reverse", font="verdana 10 bold",border=3,bg="blue", command=reverse).place(x=180,y=100)
            
            #selecting which to_Convertor drop down option appears
            toUnit_options=["select To unit","fahrenheit","celsius","kelvin"]
            # datatype of menu text and initializing
            toUnit_clicked = StringVar() 
            toUnit_clicked.set( "select To unit" ) 

            # Create Dropdown menu 
            toUnit_drop = OptionMenu( frame1 , toUnit_clicked , *toUnit_options ) 
            toUnit_drop.grid(row=1,column=1,padx=20)
            
            #input integer/float value 
            val_label=tk.Label(master=frame1,text="Enter Value : ",fg="black",bg="white", font="verdana 14 bold").grid(row=2,column=0,padx=10,pady=20)
            val=tk.StringVar()
            val_entry=tk.Entry(master=frame1, textvariable=val, font="verdana 14 bold", border=3).grid(row=2,column=1,pady=10,padx=20)

        elif(set_label.cget("text")=="Currency"):
            #selecting which From_Convertor drop down option appears
            fromUnit_options=["select From unit","Indian Rupees","USDollar","Dinar","Euro","Pound","Ruble","Dirham","Yen","Taka"]
            # datatype of menu text and initializing
            fromUnit_clicked = StringVar() 
            fromUnit_clicked.set( "select From unit" ) 

            # Create Dropdown menu 
            fromUnit_drop = OptionMenu( frame1 , fromUnit_clicked , *fromUnit_options ) 
            fromUnit_drop.grid(row=1,column=0,padx=10,pady=10)
            
            #create Interchange Button
            rev_button=tk.Button(frame1,text="reverse", font="verdana 10 bold",border=3,bg="blue", command=reverse).place(x=180,y=100)
            
            #selecting which to_Convertor drop down option appears
            toUnit_options=["select To unit","Indian Rupees","USDollar","Dinar","Euro","Pound","Rubel","Canadian Dollar","Dhiram","Yen","Taka"]
            # datatype of menu text and initializing
            toUnit_clicked = StringVar() 
            toUnit_clicked.set( "select To unit" ) 

            # Create Dropdown menu 
            toUnit_drop = OptionMenu( frame1 , toUnit_clicked , *toUnit_options ) 
            toUnit_drop.grid(row=1,column=1,padx=20)
            
            #input integer/float value
            val_label=tk.Label(master=frame1,text="Enter Value : ",fg="black",bg="white", font="verdana 14 bold").grid(row=2,column=0,padx=10,pady=20) 
            val=tk.StringVar()
            val_entry=tk.Entry(master=frame1, textvariable=val, font="verdana 14 bold", border=3).grid(row=2,column=1,pady=10,padx=20)

def reverse():
    global x
    global y
    x=fromUnit_clicked.get()
    y=toUnit_clicked.get()
    fromUnit_clicked.set(y)
    toUnit_clicked.set(x)
    
    
def convert_unit():
    global fromUnit_options
    global toUnit_options
    global val
    global fromUnit_clicked
    global toUnit_clicked
    global final_result
    set_label = Label( frame1 , text = " " ,bg="white" ,fg="black" ) 
    set_label.config( text = measurement_clicked.get() )
    from_label = Label( frame1 , text = " " ,bg="white" ,fg="black" ) 
    to_label = Label( frame1 , text = " " ,bg="white" ,fg="black" ) 
    from_label.config( text = fromUnit_clicked.get() ) 
    to_label.config( text = toUnit_clicked.get() ) 
    processed_val=float(val.get())
    
    #Checking and Displaying Errors
    if(set_label.cget("text")=="Select Unit Category"):
        messagebox.showwarning("Invalid Selection","Please select any unit Category")
    elif(processed_val<0 and set_label.cget("text")!="Temperature"and from_label.cget("text")!="select From unit" and to_label.cget("text")!="select To unit"):
            messagebox.showwarning("Invalid Input","Please enter a Positive Value")
    elif(from_label.cget("text")=="select From unit" and to_label.cget("text")!="select To unit" and processed_val>=0 ):
        messagebox.showwarning("Invalid Selection","Please select any From Unit")
    elif(from_label.cget("text")!="select From unit" and to_label.cget("text")=="select To unit" and processed_val>=0):
            messagebox.showwarning("Invalid Selection","Please select any To Unit")
    elif(from_label.cget("text")=="select From unit" and to_label.cget("text")=="select To unit" and processed_val>=0 ):
        messagebox.showwarning("Invalid Selection","Please select any From and To Units")
    elif(from_label.cget("text")=="select From unit" and to_label.cget("text")!="select To unit" and processed_val<0 and set_label.cget("text")!="Temperature"):
        messagebox.showwarning("Invalid Selection and Input","Please select any From Unit and also input positive value")
    elif(from_label.cget("text")!="select From unit" and to_label.cget("text")=="select To unit" and processed_val<0 and set_label.cget("text")!="Temperature"):
        messagebox.showwarning("Invalid Selection and Input","Please select any To Unit and also input positive value")
    elif(from_label.cget("text")=="select From unit" and to_label.cget("text")=="select To unit" and processed_val<0 and set_label.cget("text")!="Temperature" ):
        messagebox.showwarning("Invalid Selection and Input","Please select any From and To Units and also input positive value")
    elif(from_label.cget("text")=="select To unit" and to_label.cget("text")=="select From unit" and processed_val<0 and set_label.cget("text")!="Temperature" ):
        messagebox.showwarning("Invalid Selection and Input","Please select any From and To Units and also input positive value")
    elif(from_label.cget("text")!="select To unit" and to_label.cget("text")=="select From unit" and processed_val<0 and set_label.cget("text")!="Temperature" ):
        messagebox.showwarning("Invalid Selection and Input","Please select any To Unit and also input positive value") 
    elif(from_label.cget("text")=="select To unit" and to_label.cget("text")!="select From unit" and processed_val<0 and set_label.cget("text")!="Temperature" ):
        messagebox.showwarning("Invalid Selection","Please select any From Unit and also input positive value")
    elif(from_label.cget("text")=="select To unit" and to_label.cget("text")=="select From unit" ):
        messagebox.showwarning("Invalid Selection","Please select any From and To Units")
    elif(from_label.cget("text")!="select To unit" and to_label.cget("text")=="select From unit" ):
        messagebox.showwarning("Invalid Selection","Please select any To Unit")       
    elif(from_label.cget("text")=="select To unit" and to_label.cget("text")!="select From unit" ):
        messagebox.showwarning("Invalid Selection","Please select any From Unit")
    elif(val==""):
        messagebox.showwarning("Empty Input","Please Input any Value")
    else:    
        #for mass category
        if(set_label.cget("text")=="Mass" and from_label.cget("text")=="Kilograms" and to_label.cget("text")=="grams"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+" grams")
        elif(set_label.cget("text")=="Mass" and from_label.cget("text")=="Kilograms" and to_label.cget("text")=="milligram"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+" milligram")    
        elif(set_label.cget("text")=="Mass" and from_label.cget("text")=="grams" and to_label.cget("text")=="Kilograms"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+" Kilograms")    
        elif(set_label.cget("text")=="Mass" and from_label.cget("text")=="milligram" and to_label.cget("text")=="Kilograms"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+" Kilograms")    
        elif(set_label.cget("text")=="Mass" and from_label.cget("text")=="grams" and to_label.cget("text")=="milligram"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+" milligram")        
        elif(set_label.cget("text")=="Mass" and from_label.cget("text")=="milligram" and to_label.cget("text")=="grams"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+" grams")
        
        #for volume category
        elif(set_label.cget("text")=="Volume" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Mililitre"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+" Mililitre")
        elif(set_label.cget("text")=="Volume" and from_label.cget("text")=="Mililitre" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+" Litre")
        elif(set_label.cget("text")=="Volume" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Gallon"):
            final_result=processed_val/3.785
            result_str.set(str(final_result)+" Gallon")
        elif(set_label.cget("text")=="Volume" and from_label.cget("text")=="Gallon" and to_label.cget("text")=="Litre"):
            final_result=processed_val*3.785
            result_str.set(str(final_result)+" litre")
        elif(set_label.cget("text")=="Volume" and from_label.cget("text")=="Mililitre" and to_label.cget("text")=="Gallon"):
            final_result=processed_val/3785.41
            result_str.set(str(final_result)+" Gallon")
        elif(set_label.cget("text")=="Volume" and from_label.cget("text")=="Gallon" and to_label.cget("text")=="Mililitre"):
            final_result=processed_val*3785.41
            result_str.set(str(final_result)+" Mililitre")
        
        #for Temperature category    
        elif(set_label.cget("text")=="Temperature" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="celsius"):
            final_result=(processed_val-32)*(5/9)
            result_str.set(str(final_result)+" celsius")
        elif(set_label.cget("text")=="Temperature" and from_label.cget("text")=="celsius" and to_label.cget("text")=="fahrenheit"):
            final_result=(processed_val+32)*(9/5)
            result_str.set(str(final_result)+" fahrenheit")
        elif(set_label.cget("text")=="Temperature" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="kelvin"):
            final_result=((processed_val-32)*(5/9))+273.15
            result_str.set(str(final_result)+" kelvin")
        elif(set_label.cget("text")=="Temperature" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="fahrenheit"):
            final_result=((processed_val-273.15)*(9/5))+32
            result_str.set(str(final_result)+" fahrenheit")
        elif(set_label.cget("text")=="Temperature" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="celsius"):
            final_result=processed_val-273.15
            result_str.set(str(final_result)+" celsius")
        elif(set_label.cget("text")=="Temperature" and from_label.cget("text")=="celsius" and to_label.cget("text")=="kelvin"):
            final_result=processed_val+273.15
            result_str.set(str(final_result)+" kelvin")                                                
        
        #for Length category
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="meter" and to_label.cget("text")=="centimeters"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="centimeters" and to_label.cget("text")=="meter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="meter" and to_label.cget("text")=="kilometer"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="kilometer" and to_label.cget("text")=="meter"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="meter" and to_label.cget("text")=="feet"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="feet" and to_label.cget("text")=="meter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="miles" and to_label.cget("text")=="inches"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="meter" and to_label.cget("text")=="inches"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="inches" and to_label.cget("text")=="meter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="meter" and to_label.cget("text")=="miles"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="miles" and to_label.cget("text")=="meter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="centimeter" and to_label.cget("text")=="kilometer"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="kilometer" and to_label.cget("text")=="centimeter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="centimeter" and to_label.cget("text")=="feet"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="feet" and to_label.cget("text")=="centimeter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="centimeter" and to_label.cget("text")=="inches"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="inches" and to_label.cget("text")=="centimeter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="centimeter" and to_label.cget("text")=="miles"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="miles" and to_label.cget("text")=="centimeter"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="kilometer" and to_label.cget("text")=="feet"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="feet" and to_label.cget("text")=="kilometer"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="kilometer" and to_label.cget("text")=="inches"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="inches" and to_label.cget("text")=="kilometer"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="kilometer" and to_label.cget("text")=="miles"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="miles" and to_label.cget("text")=="kilometer"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="feet" and to_label.cget("text")=="inches"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="inches" and to_label.cget("text")=="feet"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="inches" and to_label.cget("text")=="miles"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="feet" and to_label.cget("text")=="miles"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Length" and from_label.cget("text")=="miles" and to_label.cget("text")=="feet"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
            
        #for Time category    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="second" and to_label.cget("text")=="minute"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="minute" and to_label.cget("text")=="second"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="second" and to_label.cget("text")=="hour"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="hour" and to_label.cget("text")=="second"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="second" and to_label.cget("text")=="day"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="day" and to_label.cget("text")=="second"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="second" and to_label.cget("text")=="week"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="week" and to_label.cget("text")=="second"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="second" and to_label.cget("text")=="normal year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="normal year" and to_label.cget("text")=="second"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="second" and to_label.cget("text")=="leap year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="leap year" and to_label.cget("text")=="second"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="minute" and to_label.cget("text")=="hour"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="hour" and to_label.cget("text")=="minute"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="minute" and to_label.cget("text")=="day"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="day" and to_label.cget("text")=="minute"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="minute" and to_label.cget("text")=="week"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="week" and to_label.cget("text")=="minute"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="minute" and to_label.cget("text")=="normal year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="normal year" and to_label.cget("text")=="minute"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="minute" and to_label.cget("text")=="leap year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="leap year" and to_label.cget("text")=="minute"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="hour" and to_label.cget("text")=="day"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="day" and to_label.cget("text")=="hour"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="hour" and to_label.cget("text")=="week"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="week" and to_label.cget("text")=="hour"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="hour" and to_label.cget("text")=="normal year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="normal year" and to_label.cget("text")=="hour"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="hour" and to_label.cget("text")=="leap year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="leap year" and to_label.cget("text")=="hour"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="day" and to_label.cget("text")=="week"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="week" and to_label.cget("text")=="day"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="day" and to_label.cget("text")=="normal year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="normal year" and to_label.cget("text")=="day"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="day" and to_label.cget("text")=="leap year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="leap year" and to_label.cget("text")=="day"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="week" and to_label.cget("text")=="normal year"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="normal year" and to_label.cget("text")=="week"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="week" and to_label.cget("text")=="leap year"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="leap year" and to_label.cget("text")=="week"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="normal year" and to_label.cget("text")=="leap year"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Time" and from_label.cget("text")=="leap year" and to_label.cget("text")=="normal year"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram") 
            
        #for Currency category           
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="grams"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Mililitre" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="Mililitre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="fahrenheit"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="fahrenheit"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Kilograms" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Indian Rupees" and to_label.cget("text")=="Kilograms"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="milligram" and to_label.cget("text")=="Indian Rupees"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="milligram"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="milligram" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="Mililitre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Mililitre" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="Gallon"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Gallon" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="Gallon"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Gallon" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="celsius"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="celsius" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="kelvin"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="USDollar" and to_label.cget("text")=="celsius"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="celsius" and to_label.cget("text")=="USDollar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dinar" and to_label.cget("text")=="milligram"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="grams" and to_label.cget("text")=="Dinar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dinar" and to_label.cget("text")=="Dinar"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="grams" and to_label.cget("text")=="Dinar"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dinar" and to_label.cget("text")=="grams"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Dinar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dinar" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Dinar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dinar" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Mililitre" and to_label.cget("text")=="Dinar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dinar" and to_label.cget("text")=="Mililitre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="Dinar"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Euro" and to_label.cget("text")=="fahrenheit"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="Euro"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Euro" and to_label.cget("text")=="fahrenheit"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="Euro"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Euro" and to_label.cget("text")=="kelvin"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Kilograms" and to_label.cget("text")=="Euro"):
            final_result=processed_val*1000000
            result_str.set(str(final_result)+"milligram")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Euro" and to_label.cget("text")=="Kilograms"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="milligram" and to_label.cget("text")=="Euro"):
            final_result=processed_val/1000000
            result_str.set(str(final_result)+"Kilograms")    
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Euro" and to_label.cget("text")=="milligram"):
            final_result=processed_val*1000
            result_str.set(str(final_result)+"milligram")        
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Pound" and to_label.cget("text")=="Euro"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Pound"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Pound" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Litre" and to_label.cget("text")=="Pound"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Pound" and to_label.cget("text")=="Litre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Mililitre" and to_label.cget("text")=="Pound"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Pound" and to_label.cget("text")=="Mililitre"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="fahrenheit" and to_label.cget("text")=="Pound"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Pound" and to_label.cget("text")=="fahrenheit"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Yen" and to_label.cget("text")=="kelvin"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="Yen"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Yen" and to_label.cget("text")=="celsius"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="celsius" and to_label.cget("text")=="Yen"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Yen" and to_label.cget("text")=="Gallon"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Gallon" and to_label.cget("text")=="Yen"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")   
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Ruble" and to_label.cget("text")=="celsius"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="celsius" and to_label.cget("text")=="Ruble"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Ruble" and to_label.cget("text")=="kelvin"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="kelvin" and to_label.cget("text")=="Ruble"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Taka" and to_label.cget("text")=="Dirham"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")
        elif(set_label.cget("text")=="Currency" and from_label.cget("text")=="Dirham" and to_label.cget("text")=="Taka"):
            final_result=processed_val/1000
            result_str.set(str(final_result)+"grams")                             
    
def reset():
    measurement_clicked.set("Select Unit Category")
    fromUnit_clicked.set("select From unit")
    toUnit_clicked.set("select To unit")
    val.set("")
    result_str.set("")

#initializing window
win=tk.Tk()
win.title("Unit Convertor")
win.geometry("800x600")
win.resizable(False,False)

#setting background image
original_convertorBg_image= Image.open("convertorbg.jpg")
resized_convertorBg_image= original_convertorBg_image.resize((800,600))
# Convert the resized image to PhotoImage format
convertorBg_img= ImageTk.PhotoImage(resized_convertorBg_image)
convertorBg_widget= tk.Label(master=win,image=convertorBg_img)
convertorBg_widget.image=convertorBg_img # This line is important to prevent the image from being garbage collected
convertorBg_widget.place(x=0,y=0)

title_label=tk.Label(master=win, text="Unit Convertor", font="verdana 30 bold", bg="black", fg="green", highlightbackground="green", highlightthickness=3).pack(pady=10)
heading_label=tk.Label(master=win, text="", font="verdana 20", bg="black", fg="white")
sentence ="Perform Conversion between any desired Units"
heading_label.pack(pady=10)

frame1=tk.Frame(master=win,highlightbackground="black", highlightthickness=5,border=5)
frame1.configure(background="white")
frame1.pack(pady=50)

measurement_options=["Select Unit Category","Mass","Length","Time","Volume","Temperature","Currency"]

# datatype of menu text and initializing
measurement_clicked = StringVar() 
measurement_clicked.set( "Select Unit Category" ) 
fromUnit_clicked=StringVar()
toUnit_clicked=StringVar()
val=tk.StringVar()

# Create Dropdown menu 
measurement_drop = OptionMenu( frame1 , measurement_clicked , *measurement_options ) 
measurement_drop.grid(row=0,column=0,padx=10,pady=30) 

# Create button, it will change label text 
set_button = Button( frame1 , text = "Set Unit Category" , font="verdana 10 bold",border=3,bg="yellow", command = set_measurement ).grid(row=0,column=1,padx=30 )
set_label = Label( frame1 , text = " " ,bg="white" ,fg="black" ) 

# Reset and Convert button
reset_button = Button( frame1 , text = "Reset" , font="verdana 10 bold", bg="red",border=3 , command = reset ).grid(row=3,column=0,pady=10)  
result_button = Button( frame1 , text = "Convert" , font="verdana 10 bold", bg="green",border=3, command = convert_unit ).grid(row=3,column=1,pady=10) 

result_str=StringVar()
result_label=tk.Label(master=win, text="", textvariable=result_str, font="verdana 20 bold", fg="blue", bg="black", highlightbackground="black", highlightthickness=3).pack()  

update2_label()

#run event loop
win.mainloop()

