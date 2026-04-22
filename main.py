"""
BMI calculator to calculate based on the mass and hieght of a person 
"""

# impotant tkinter with the shorter alies 'tk'
import tkinter as tk 

#set up root window 
root = tk.Tk()
root.title("BMI Calculator") # titile at the top  of the window 

# create function that will do the calculations for BMI
def calculate_bmi(): 
    mass = float (entry_mass.get())
    height = float (enetry_height.get())
    bmi = round  (mass/(height**2), 2)
    lable_bmi['text'] = f"BMI: {bmi}" 
#create and place the GUI widgets on the grid 
#lable widgets 
lable_mass = tk.Lable (root,text="mass
#entry widgets 
#lable widgets 
#entry widgets 
#button widgets 
#lable widgets 

#Event loop and keep  the gui running 
root.mainloop()