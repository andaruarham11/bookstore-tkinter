from __future__ import annotations

import os
import tkinter as tk
from tkinter import constants as tk_const

from PIL import Image, ImageTk

from core import CoreApp


class UserHomePage(tk.Frame):
    def __init__(self, parent, ctrl: CoreApp):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl

        self.ctrl.title("Main Page")

        lbl_title = tk.Label(self, text="Bookstore", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        # frame logo
        book_frame = tk.Frame(self, bg="#D1D1D1")
        book_frame.place(x=275, y=200, width=400, height=400)

        pay_frame = tk.Frame(self, bg="#D1D1D1")
        pay_frame.place(x=875, y=200, width=400, height=400)

        script_dir = os.path.dirname(os.path.abspath(__file__))

        # frame logo
        book_img = Image.open(os.path.join(script_dir, "../assets/books.png"))
        resize_book_image = book_img.resize((150, 150))
        self.image_book = ImageTk.PhotoImage(resize_book_image)
        image_book_label = tk.Label(book_frame, image=self.image_book, bg="#D1D1D1")
        image_book_label.place(x=125, y=80)

        pay_img = Image.open(os.path.join(script_dir, "../assets/pay.png"))
        resize_pay_img = pay_img.resize((150, 150))
        self.image_pay = ImageTk.PhotoImage(resize_pay_img)
        image_pay_label = tk.Label(pay_frame, image=self.image_pay, bg="#D1D1D1")
        image_pay_label.place(x=125, y=80)

        # button
        book_btn = tk.Button(book_frame, command=lambda: self.ctrl.show("DataBukuPage"), text="Catalog Buku",
                             font=("Calibri", 15), bd=3, fg="black")
        book_btn.place(x=125, y=290, width=150, height=50)

        order_btn = tk.Button(pay_frame, command=lambda: self.ctrl.show("OrderPage"), text="Status Order", font=("Calibri", 15), bd=3,
                              fg="black")
        order_btn.place(x=100, y=290, width=200, height=50)

        # logout button
        logout_btn = tk.Button(self, command=lambda: self.ctrl.show("LoginPage"), text="Logout",
                               font=("Calibri", 15), bd=3, fg="black")
        logout_btn.place(x=0, y=80, width=120, height=35)
        ########
