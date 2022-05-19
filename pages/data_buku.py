from __future__ import annotations

import tkinter as tk
from tkinter import constants as tk_const, ttk

from utils import Response


class DataBukuPage(tk.Frame):
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.my_tabel = None
        self.ctrl = ctrl

        self.ctrl.title("Data Buku Page")

        self.id_buku = tk.StringVar()
        self.nama_buku = tk.StringVar()
        self.pengarang_buku = tk.StringVar()
        self.penerbit_buku = tk.StringVar()
        self.kategori_buku = tk.StringVar()
        self.bahasa_buku = tk.StringVar()
        self.harga_buku = tk.StringVar()
        self.stok_buku = tk.StringVar()

        books = self.get_books()
        self.render(books)

    def render(self, books):
        lbl_title = tk.Label(self, text="Data Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        # style
        style = ttk.Style()

        # theme
        style.theme_use('default')

        # configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=40, fieldbackground="#D3D3D3")

        # change selected color
        style.map('Treeview', background=[('selected', "#347083")])

        # back button
        back_btn = tk.Button(self, command=lambda: self.ctrl.show("HomePage"), text="Kembali",
                             font=("Calibri", 15), bd=3, fg="black")
        back_btn.place(x=20, y=80, width=120, height=35)

        # frame tabel
        tabel_frame = tk.Frame(self)
        tabel_frame.place(x=10, y=150, width=1510, height=600)

        # style
        style = ttk.Style()

        # scrollbar
        tabel_scroll = tk.Scrollbar(tabel_frame, orient=tk_const.VERTICAL)
        tabel_scroll.pack(side=tk_const.RIGHT, fill=tk_const.Y)

        # create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, columns=(
            "IDBuku", "Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku",
            "Stok Buku"), yscrollcommand=tabel_scroll.set)

        self.my_tabel.pack()

        # configure our columns
        tabel_scroll = tk.Scrollbar(command=self.my_tabel.yview)

        # headings
        self.my_tabel.heading("IDBuku", text="ID Buku")
        self.my_tabel.heading("Nama Buku", text="Nama Buku")
        self.my_tabel.heading("Pengarang Buku", text="Pengarang Buku")
        self.my_tabel.heading("Penerbit Buku", text="Penerbit Buku")
        self.my_tabel.heading("Kategori Buku", text="Kategori Buku")
        self.my_tabel.heading("Bahasa Buku", text="Bahasa Buku")
        self.my_tabel.heading("Harga Buku", text="Harga Buku")
        self.my_tabel.heading("Stok Buku", text="Stok Buku")

        self.my_tabel["show"] = "headings"

        # format columns
        # self.my_tabel.column("#0", width=0, stretch=NO)
        self.my_tabel.column("IDBuku", width=100)
        self.my_tabel.column("Nama Buku", width=100)
        self.my_tabel.column("Pengarang Buku", width=100)
        self.my_tabel.column("Penerbit Buku", width=100)
        self.my_tabel.column("Kategori Buku", width=100)
        self.my_tabel.column("Bahasa Buku", width=100)
        self.my_tabel.column("Harga Buku", width=100)
        self.my_tabel.column("Stok Buku", width=100)

        self.my_tabel.pack(fill=tk_const.BOTH, expand=1)

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lavenderblush1")

        # add our data to the screen
        count = 0
        for b in books:
            tags = ""
            if count % 2 == 0:
                tags = "evenrow"
            else:
                tags = "oddrow"

            self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', tags=tags, values=(
                b["id"], b["nama"], b["pengarang"], b["penerbit"], b["kategori"], b["bahasa"], b["harga"], b["stok"])
                                 )

            count += 1

        self.my_tabel.selected_item = None
        self.my_tabel.bind('<ButtonRelease-1>', self.select_item)

    def select_item(self, a):
        cur_item = self.my_tabel.focus()
        self.my_tabel.selected_item = self.my_tabel.item(cur_item)
        table_data = self.my_tabel.selected_item["values"]
        state = {"book_id": table_data[0]}

        self.ctrl.set_s(state)
        self.ctrl.show("DetailBukuPage")

    def get_books(self):
        res: Response = self.ctrl.apis.get_all_books()
        if res.is_err():
            return self.ctrl.show("HomePage")

        table_data = []
        for d in res.result():
            table_data.append({
                "id": d["id"],
                "nama": d["name"],
                "pengarang": d["author"],
                "penerbit": d["publisher"],
                "kategori": d["category"],
                "bahasa": d["language"],
                "harga": d["price"],
                "stok": d["qty"]
            })
        return table_data
