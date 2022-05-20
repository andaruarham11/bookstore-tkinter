from __future__ import annotations

import base64
import io
import tkinter as tk
from tkinter import constants as tk_const, ttk

from PIL import Image, ImageTk

from core import CoreApp, Response


class DetailBukuPage(tk.Frame):
    def __init__(self, parent, ctrl: CoreApp):
        tk.Frame.__init__(self, parent)
        self.btn_beli = None
        self.lbl_harga = None
        self.lbl_bahasa = None
        self.lbl_kategori = None
        self.lbl_penerbit = None
        self.book_img = None
        self.lbl_stok = None
        self.data_pengarang = None
        self.data_penerbit = None
        self.data_kategori = None
        self.data_bahasa = None
        self.data_harga = None
        self.data_stok = None
        self.data_jumlah_beli = None

        self.ctrl = ctrl

        state = self.ctrl.get_s("book_id")
        book_data = self.get_book(state)

        self.render(book_data)

    def render(self, book_data: dict):
        self.ctrl.title("Detail Buku Page")

        lbl_title = tk.Label(self, text="Detail Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        back_btn = tk.Button(self, command=lambda: self.ctrl.show("DataBukuPage"), text="Kembali", font=("Calibri", 15), bd=3, fg="black")
        back_btn.place(x=20, y=80, width=120, height=35)

        self.book_img = Image.open(io.BytesIO(base64.b64decode(book_data["gambar_buku"]))).resize((400, 450))
        self.book_img = ImageTk.PhotoImage(self.book_img)
        image_book_label = tk.Label(self, image=self.book_img)
        image_book_label.place(x=250, y=200)

        lbl_book_name = tk.Label(self, text=book_data["nama_buku"], fg="black", font=("Calibri", 22, "bold"), compound="left", anchor='w')
        lbl_book_name.place(relx=0.206, rely=0.163, height=52, width=1000)

        lbl_pengarang = ttk.Label(self, foreground="#000000", anchor='w', justify='left', text='''Pengarang:''', compound='left')
        lbl_pengarang.place(relx=0.594, rely=0.25, height=32, width=122)

        self.lbl_penerbit = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text='''Penerbit:''', compound='left')
        self.lbl_penerbit.place(relx=0.594, rely=0.313, height=32, width=122, )

        self.lbl_kategori = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text='''Kategori:''')
        self.lbl_kategori.place(relx=0.594, rely=0.375, height=32, width=122)

        self.lbl_bahasa = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text='''Bahasa:''', compound='left')
        self.lbl_bahasa.place(relx=0.594, rely=0.438, height=32, width=122)

        self.lbl_harga = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text='''Harga:''', compound='left')
        self.lbl_harga.place(relx=0.594, rely=0.5, height=32, width=122)

        self.lbl_stok = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text='''Stok:''', compound='left')
        self.lbl_stok.place(relx=0.594, rely=0.563, height=32, width=122)

        self.data_pengarang = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=book_data["pengarang_buku"], compound='left')
        self.data_pengarang.place(relx=0.69, rely=0.25, height=32, width=122)

        self.data_penerbit = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=book_data["penerbit_buku"], compound='left')
        self.data_penerbit.place(relx=0.69, rely=0.313, height=32, width=122)

        self.data_kategori = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=book_data["kategori_buku"], compound='left')
        self.data_kategori.place(relx=0.69, rely=0.375, height=32, width=122)

        self.data_bahasa = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=book_data["bahasa_buku"], compound='left')
        self.data_bahasa.place(relx=0.69, rely=0.438, height=32, width=122)

        self.data_harga = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=book_data["harga_buku"], compound='left')
        self.data_harga.place(relx=0.69, rely=0.5, height=32, width=122)

        self.data_stok = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=book_data["stok_buku"], compound='left')
        self.data_stok.place(relx=0.69, rely=0.563, height=32, width=122)

        self.data_jumlah_beli = tk.Spinbox(self, from_=1.0, to=int(book_data["stok_buku"]), activebackground="#f9f9f9", background="white",
                                           highlightbackground="black", selectbackground="#c4c4c4")
        self.data_jumlah_beli.place(relx=0.626, rely=0.65, relheight=0.03, relwidth=0.038)

        self.btn_beli = tk.Button(self, command=self.order_book, activebackground="beige", borderwidth="2", compound='left', text="Beli")
        self.btn_beli.place(relx=0.69, rely=0.638, height=47, width=89)

    def get_book(self, bookId: str):
        res: Response = self.ctrl.apis.get_book(bookId)
        if res.is_err():
            return self.ctrl.show("UserHomePage")

        res: dict = res.result()

        return {
            "id_buku": res["id"],
            "nama_buku": res["name"],
            "pengarang_buku": res["author"],
            "penerbit_buku": res["publisher"],
            "kategori_buku": res["category"],
            "bahasa_buku": res["language"],
            "harga_buku": res["price"],
            "stok_buku": res["qty"],
            "gambar_buku": res["image"]
        }

    def order_book(self):
        user_id = self.ctrl.get_s("user_data")["id"]
        book_id = self.ctrl.get_s("book_id")
        qty = int(self.data_jumlah_beli.get())

        res: Response = self.ctrl.apis.do_order(user_id, book_id, qty)
        if res.is_err():
            return self.ctrl.show("UserHomePage")

        res: dict = res.result()

        self.ctrl.set_s({"order_id": res["id"]})
        self.ctrl.show("OrderPage")
