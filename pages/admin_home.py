import os
import tkinter as tk
from tkinter.constants import W

from PIL import Image, ImageTk

from core import CoreApp


class AdminHomePage(tk.Frame):
    def __init__(self, parent, ctrl: CoreApp):
        tk.Frame.__init__(self, parent)
        self.my_tabel = None
        self.ctrl = ctrl

        self.ctrl.title("Admin Home Page")
        self.render()

    def render(self):
        lbltitle = tk.Label(self, text="Admin Page", fg="black", font=("Calibri", 30, "bold"))
        lbltitle.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

        logout_btn = tk.Button(self, text="Logout", command=lambda: self.ctrl.show("LoginPage"), font=("Calibri", 12), bd=3, fg="black")
        logout_btn.place(x=10, y=100, width=120, height=35)

        # frame untuk logo
        logo1_frame = tk.Frame(self, bg="#D1D1D1")
        logo1_frame.place(x=275, y=200, width=400, height=400)

        logo2_frame = tk.Frame(self, bg="#D1D1D1")
        logo2_frame.place(x=875, y=200, width=400, height=400)

        script_dir = os.path.dirname(os.path.abspath(__file__))

        # logo untuk button
        image1 = Image.open(os.path.join(script_dir, "../assets/books.png")).resize((150, 150))
        self.image_book = ImageTk.PhotoImage(image1)
        image_book_label = tk.Label(logo1_frame, image=self.image_book, bg="#D1D1D1")
        image_book_label.place(x=125, y=80)

        image2 = Image.open(os.path.join(script_dir, "../assets/pay.png")).resize((150, 150))
        self.image_pay = ImageTk.PhotoImage(image2)
        image_pay_label = tk.Label(logo2_frame, image=self.image_pay, bg="#D1D1D1")
        image_pay_label.place(x=125, y=80)

        # button
        book_btn = tk.Button(logo1_frame, command=lambda: self.ctrl.show("AdminDataBukuPage"), text="Data Buku", font=("Calibri", 15), bd=3, fg="black")
        book_btn.place(x=125, y=290, width=150, height=50)

        customer_btn = tk.Button(logo2_frame, command=lambda: self.ctrl.show("AllOrderPage"), text="Data Pembayaran", font=("Calibri", 15), bd=3, fg="black")
        customer_btn.place(x=100, y=290, width=200, height=50)
