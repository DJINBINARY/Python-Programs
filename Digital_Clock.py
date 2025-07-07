# Python Program to Display Digital Clock by Divyanshu Joshi
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p\n%d/%m/%Y")  # Corrected format
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='white', foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
