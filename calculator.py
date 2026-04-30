import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

First = tk.Label(mainWindow,text="Enter Your First Number",pady=10)
First.pack()

First_Value = tk.Entry(mainWindow)
First_Value.pack()

Second = tk.Label(mainWindow,text="Enter Your Second Number",pady=10,padx=10)
Second.pack()

Second_Value = tk.Entry(mainWindow)
Second_Value.pack()


    
button = tk.Button(mainWindow,text="+",
                   command = lambda:Add())
button.pack()

button = tk.Button(mainWindow,text="-",
                   command = lambda:Sub())
button.pack()

button = tk.Button(mainWindow,text="*",
                   command = lambda:Mul())
button.pack()

button = tk.Button(mainWindow,text="/",
                   command = lambda:Div())
button.pack()

result_label=tk.Label(mainWindow,text="Operation Result is : ")
result_label.pack()

def Add():
    try:
        a = int(First_Value.get())
        b = int(Second_Value.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    result = a + b
    result_label.config(text="Operation Result is : " + str(result))
    
    
def Sub():
    a=int(First_Value.get())
    b=int(Second_Value.get())
    result = a - b
    result_label.config(text = "Operation Result is : " +str(result))
    
    
def Mul():
    a=int(First_Value.get())
    b=int(Second_Value.get())
    Mul=a*b
    result_label.config(text = "Operation Result is : " +str(Mul))
    
def Div():
    a = int(First_Value.get())
    b = int(Second_Value.get())
    try:
        result = a / b
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        return
    result_label.config(text="Operation Result is : " + str(result))

mainWindow.mainloop()
    