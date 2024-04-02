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


def open_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return file


# fucn to store data in csv files
def storedata():
    if not os.path.isfile(os.getcwd() + "\\QrCode and Barcode Datas.csv"):
        with open("QrCode and Barcode Datas.csv", "w", newline="") as codes:
            fields = ["Subject", "Type", "Timestamp"]
            writer = csv.DictWriter(codes, fieldnames=fields)
            writer.writeheader()
    with open("QrCode and Barcode Datas.csv", "a", newline="") as codes:
        writer = csv.writer(codes)
        if type1 == 1:
            writer.writerow([Subject.get(), "Qrcode", timestampStr1])
        elif type1 == 2:
            writer.writerow([Subject.get(), "Barcode", timestampStr2])


