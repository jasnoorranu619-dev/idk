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
lable_mass = tk.Lable (root, text="mass: ")
lable_mass.grid(column=0, row=0)
#entry widgets 
enetry_mass = tk.Entry(root)
enetry_mass.grid(column=1, row=0)
#lable widgets 
lable_height = tk.Lable(root, text="Height:")
lable_height.grid(column=0, row=1)
#entry widgets 
enetry_height = tk.Enetry(root)
enetry_height.grid(column=1,row=1 )
#button widgets 
button_calculate =tk.button(root, text="calculate", command =calculate_bmi)
button_calculate.grid(column=0, row=2)
#lable widgets 
lable_bmi =tk.Lable(root, text="BMI:")
lable_bmi.grid(column=1, row=2) 

#Event loop and keep  the gui running 
root.mainloop()