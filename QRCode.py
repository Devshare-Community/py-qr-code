from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import shutil
import barcode
import MyQR
import csv
from datetime import datetime


s = 0
# Creating the base window for the GUI
window = Tk()
window.resizable(width=False, height=False)
window.title("QR and Bar Code Generator")


# func to set size
def setsize(a):
    global s
    s = a
    messagebox.showinfo("", "Select format")


