# coba upload file

from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

import time
import requests

ws = Tk()
ws.title('PythonGuides')
ws.geometry('800x800')


def open_file():
    global img
    # file_path = askopenfile(mode='r', filetypes=[('Image Files', '*.jpg')])
    # if file_path is not None:
    # pass

    f_types = [('JPG Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    # print(filename)
    img = Image.open(filename)
    print(filename)
    # img_resized = img.resize((100,100))
    img = ImageTk.PhotoImage(img)

    label1 = tkinter.Label(image=img)
    label1.image = img

    # Position image
    label1.place(x=10, y=10)

    # url = 'http://'
    # files = {'media': open(img, 'rb')}
    # requests.post(url, files=files)


# ini ga kepake, yg bisa kepake baru yg open_file()
def uploadFiles():
    global img
    pb1 = Progressbar(ws, orient=HORIZONTAL, length=300, mode='determinate')
    pb1.grid(row=4, columnspan=3, pady=20)

    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

    # img = ImageTk.PhotoImage(file=file_path)
    # image1 = Image.open("books.png")
    # image_book_label = Label(logo1_frame, image=self.image_book, bg="#D1D1D1")
    # image_book_label.place(x=125, y=80)


adhar = Label(ws, text='Upload Image in jpg format ')
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(ws, text='Choose File', command=lambda: open_file())
adharbtn.grid(row=0, column=1)

upld = Button(ws, text='Upload Files', command=uploadFiles)
upld.grid(row=3, columnspan=3, pady=10)

ws.mainloop()
