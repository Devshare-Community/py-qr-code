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


# function generate the qr code
def generate():
    if len(name.get()) != 0 and name.get() != "Enter filename here" and len(
            Subject.get()) != 0 and Subject.get() != "Enter subject here":
        if '/' not in name.get():
            global qr, photo, filename, save_dir, timestampStr1, type1
            filename = open_file()
            version, level, qr = myqr.run(Subject.get(), version=1, level='H', picture=filename, colorized=True,
                                          contrast=1.0, brightness=1.0, save_name=name.get() + ".png",
                                          save_dir=os.path.join(os.getcwd(), "src"))
            dateTimeObj = datetime.now()
            timestampStr1 = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            type1 = 1
            storedata()
            try:
                showcode()
            except:
                pass
        else:
            messagebox.showinfo("", "filename can't contains '/'")
    else:
        messagebox.showinfo("", "Please Enter some filename or subject")


