from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector


class adminpage_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="Admin Page", fg="black", font=("Calibri", 30, "bold"))
        lbltitle.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

        # frame untuk logo
        logo1_frame = Frame(self.root, bg="#D1D1D1")
        logo1_frame.place(x=275, y=200, width=400, height=400)

        logo2_frame = Frame(self.root, bg="#D1D1D1")
        logo2_frame.place(x=875, y=200, width=400, height=400)

        # logo untuk button
        image1 = Image.open("books.png")
        resize_image = image1.resize((150, 150))
        self.image_book = ImageTk.PhotoImage(resize_image)
        image_book_label = Label(logo1_frame, image=self.image_book, bg="#D1D1D1")
        image_book_label.place(x=125, y=80)

        image2 = Image.open("pay.png")
        resize_image2 = image2.resize((150, 150))
        self.image_pay = ImageTk.PhotoImage(resize_image2)
        image_pay_label = Label(logo2_frame, image=self.image_pay, bg="#D1D1D1")
        image_pay_label.place(x=125, y=80)

        # button
        book_btn = Button(logo1_frame, command=self.book, text="Data Buku", font=("Calibri", 15), bd=3, fg="black")
        book_btn.place(x=125, y=290, width=150, height=50)

        customer_btn = Button(logo2_frame, text="Data Pembayaran", font=("Calibri", 15), bd=3, fg="black")
        customer_btn.place(x=100, y=290, width=200, height=50)

    '''def book(self):
        self.new_window=Toplevel(self.root)
        self.app=databuku_window(self.new_window)'''


if __name__ == "__main__":
    root = Tk()
    app = adminpage_window(root)
    root.mainloop()
