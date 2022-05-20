from __future__ import annotations

import tkinter as tk
from tkinter import constants as tk_const, ttk

from core import CoreApp, Response


class OrderPage(tk.Frame):
    def __init__(self, parent, ctrl: CoreApp):
        tk.Frame.__init__(self, parent)
        self.my_tabel = None
        self.ctrl = ctrl

        self.ctrl.title("Order Page")

        self.id_buku = tk.StringVar()
        self.nama_buku = tk.StringVar()
        self.pengarang_buku = tk.StringVar()
        self.penerbit_buku = tk.StringVar()
        self.kategori_buku = tk.StringVar()
        self.bahasa_buku = tk.StringVar()
        self.harga_buku = tk.StringVar()
        self.stok_buku = tk.StringVar()

        orders = self.get_orders_by_userid()
        self.render(orders)

    def render(self, orders):
        lbl_title = tk.Label(self, text="Data Order", fg="black", font=("Calibri", 30, "bold"))
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
        back_btn = tk.Button(self, command=lambda: self.ctrl.show("UserHomePage"), text="Kembali",
                             font=("Calibri", 15), bd=3, fg="black")
        back_btn.place(x=20, y=80, width=120, height=35)

        # frame tabel
        tabel_frame = tk.Frame(self)
        tabel_frame.place(x=10, y=150, width=1200, height=600)

        # scrollbar
        tabel_scroll = tk.Scrollbar(tabel_frame, orient=tk_const.VERTICAL)
        tabel_scroll.pack(side=tk_const.RIGHT, fill=tk_const.Y)

        # create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, columns=("id", "book_name", "qty", "price", "total_price", "status", "order_time"),
                                     yscrollcommand=tabel_scroll.set)

        self.my_tabel.pack()

        # configure our columns
        tabel_scroll = tk.Scrollbar(command=self.my_tabel.yview)

        # headings
        self.my_tabel.heading("id", text="ID Order")
        self.my_tabel.heading("book_name", text="Nama Buku")
        self.my_tabel.heading("qty", text="Jumlah")
        self.my_tabel.heading("price", text="Harga Buku")
        self.my_tabel.heading("total_price", text="Harga Total")
        self.my_tabel.heading("status", text="Status Pembayaran")
        self.my_tabel.heading("order_time", text="Waktu Order")

        self.my_tabel["show"] = "headings"

        # format columns
        self.my_tabel.column("id", width=100)
        self.my_tabel.column("book_name", width=100)
        self.my_tabel.column("qty", width=5)
        self.my_tabel.column("price", width=15)
        self.my_tabel.column("total_price", width=15)
        self.my_tabel.column("status", width=100)
        self.my_tabel.column("order_time", width=100)

        self.my_tabel.pack(fill=tk_const.BOTH, expand=1)

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lavenderblush1")

        # add our data to the screen
        count = 0
        for o in orders:
            tags = ""
            if count % 2 == 0:
                tags = "evenrow"
            else:
                tags = "oddrow"

            self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', tags=tags, values=(
                o["id"], o["book_name"], o["qty"], o["price"], o["total_price"], o["status"], o["order_time"],
            ))

            count += 1

            self.my_tabel.selected_item = None
            self.my_tabel.bind('<ButtonRelease-1>', self.select_item)

    def select_item(self, a):
        cur_item = self.my_tabel.focus()
        self.my_tabel.selected_item = self.my_tabel.item(cur_item)
        table_data = self.my_tabel.selected_item["values"]

        self.ctrl.set_s({"selected_order_id": table_data[0]})
        self.ctrl.show("PaymentPage")

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

    def get_orders_by_userid(self):
        user_id = self.ctrl.get_s("user_data")["id"]

        res: Response = self.ctrl.apis.get_all_orders_by_userid(user_id)
        if res.is_err():
            return self.ctrl.show("UserHomePage")

        orders_data = []
        for order in res.result():
            book = self.get_book(order["book_id"])
            orders_data.append({
                "id": order["id"],
                "book_name": book["nama_buku"],
                "order_time": order["order_time"],
                "qty": order["qty"],
                "price": book["harga_buku"],
                "total_price": order["total_price"],
                "status": order["status"]
            })
        return orders_data
