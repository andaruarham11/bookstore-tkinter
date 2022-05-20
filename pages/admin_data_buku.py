import base64
import io
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.constants import W, VERTICAL, HORIZONTAL, Y, X, BOTTOM, RIGHT, NO, BOTH, DISABLED, NORMAL, END
from typing import List

from PIL import Image, ImageTk

from core import CoreApp, Response


class AdminDataBukuPage(tk.Frame):
    def __init__(self, parent, ctrl: CoreApp):
        tk.Frame.__init__(self, parent)
        self.book_image_tk = None
        self.filename = None
        self.book_image = None
        self.book_image_lbl = None
        self.books: List[dict] = []
        self.my_tabel = None
        self.ctrl = ctrl

        self.selected_book_id: str = ""
        self.render()

    def render(self):
        self.ctrl.title("Admin Data Buku Page")
        self.get_books()

        # style
        style = ttk.Style()

        # theme
        style.theme_use('default')

        # configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="white")

        # change selected color
        style.map('Treeview', background=[('selected', "lemonchiffon4")])

        # frame tabel
        tabel_frame = tk.Frame(self)
        tabel_frame.place(x=10, y=30, width=755, height=500)

        # scrollbar
        tabel_scroll_y = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        tabel_scroll_x = ttk.Scrollbar(tabel_frame, orient=HORIZONTAL)
        tabel_scroll_y.pack(side=RIGHT, fill=Y)
        tabel_scroll_x.pack(side=BOTTOM, fill=X)

        # create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, xscrollcommand=tabel_scroll_x.set, yscrollcommand=tabel_scroll_y.set)
        self.my_tabel.pack()

        # configure our columns
        # tabel_scroll_y=ttk.Scrollbar(command=self.my_tabel.yview)
        # tabel_scroll_x=ttk.Scrollbar(command=self.my_tabel.xview)
        tabel_scroll_y.config(command=self.my_tabel.yview)
        tabel_scroll_x.config(command=self.my_tabel.xview)

        # define columns
        self.my_tabel['column'] = ("id", "name", "author", "publisher", "category", "language", "description", "price", "qty")

        # headings
        self.my_tabel.heading("id", text="ID")
        self.my_tabel.heading("name", text="Nama")
        self.my_tabel.heading("author", text="Pengarang")
        self.my_tabel.heading("publisher", text="Penerbit")
        self.my_tabel.heading("category", text="Kategori")
        self.my_tabel.heading("language", text="Bahasa")
        self.my_tabel.heading("description", text="Deskripsi")
        self.my_tabel.heading("price", text="Harga")
        self.my_tabel.heading("qty", text="Stok")

        self.my_tabel["show"] = "headings"

        # format columns
        self.my_tabel.column("id", width=150)
        self.my_tabel.column("name", width=150)
        self.my_tabel.column("author", width=150)
        self.my_tabel.column("publisher", width=150)
        self.my_tabel.column("category", width=85)
        self.my_tabel.column("language", width=100)
        self.my_tabel.column("description", width=100)
        self.my_tabel.column("price", width=70)
        self.my_tabel.column("qty", width=50)

        self.my_tabel.pack(fill=BOTH, expand=1)

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lemonchiffon3")

        # add our data to the screen
        count = 0
        for b in self.books:
            tags = ""
            if count % 2 == 0:
                tags = "evenrow"
            else:
                tags = "oddrow"

            self.my_tabel.insert(parent='', index='end', text=f'{count + 1}',
                                 values=(b["id"], b["name"], b["author"], b["publisher"], b["category"], b["language"], b["description"], b["price"],
                                         b["qty"]),
                                 tags=tags)
            count += 1

        # add entry boxes
        # frame
        self.viewdata_frame = tk.LabelFrame(self, text="Details")
        self.viewdata_frame.place(x=785, y=30, width=735, height=750)

        # form input data
        label_id_buku = tk.Label(self.viewdata_frame, text="ID :", fg="black")
        label_id_buku.place(x=10, y=30)
        label_nama_buku = tk.Label(self.viewdata_frame, text="Nama :", fg="black")
        label_nama_buku.place(x=10, y=60)
        label_pengarang_buku = tk.Label(self.viewdata_frame, text="Pengarang :", fg="black")
        label_pengarang_buku.place(x=10, y=90)
        label_penerbit_buku = tk.Label(self.viewdata_frame, text="Penerbit :", fg="black")
        label_penerbit_buku.place(x=10, y=120)
        label_kategori_buku = tk.Label(self.viewdata_frame, text="Kategori :", fg="black")
        label_kategori_buku.place(x=10, y=150)
        label_bahasa_buku = tk.Label(self.viewdata_frame, text="Bahasa :", fg="black")
        label_bahasa_buku.place(x=10, y=180)
        label_harga_buku = tk.Label(self.viewdata_frame, text="Harga :", fg="black")
        label_harga_buku.place(x=10, y=210)
        label_stok_buku = tk.Label(self.viewdata_frame, text="Stok :", fg="black")
        label_stok_buku.place(x=10, y=240)
        label_deskripsi_buku = tk.Label(self.viewdata_frame, text="Deskripsi :", fg="black")
        label_deskripsi_buku.place(x=10, y=270)

        # entry boxes
        self.txt_idbuku = ttk.Entry(self.viewdata_frame, state="readonly")
        self.txt_idbuku.place(x=135, y=30, width=550)
        self.txt_namabuku = ttk.Entry(self.viewdata_frame)
        self.txt_namabuku.place(x=135, y=60, width=550)
        self.txt_pengarangbuku = ttk.Entry(self.viewdata_frame)
        self.txt_pengarangbuku.place(x=135, y=90, width=550)
        self.txt_penerbitbuku = ttk.Entry(self.viewdata_frame)
        self.txt_penerbitbuku.place(x=135, y=120, width=550)
        self.txt_kategoribuku = ttk.Entry(self.viewdata_frame)
        self.txt_kategoribuku.place(x=135, y=150, width=550)
        self.txt_bahasabuku = ttk.Entry(self.viewdata_frame)
        self.txt_bahasabuku.place(x=135, y=180, width=550)
        self.txt_hargabuku = ttk.Entry(self.viewdata_frame)
        self.txt_hargabuku.place(x=135, y=210, width=550)
        self.txt_stokbuku = ttk.Entry(self.viewdata_frame)
        self.txt_stokbuku.place(x=135, y=240, width=550)
        self.txt_deskripsibuku = tk.Text(self.viewdata_frame)
        self.txt_deskripsibuku.place(x=135, y=270, width=550, height=185)

        label_upld_foto = tk.Label(self.viewdata_frame, text='Cover buku (jpg or png):')
        label_upld_foto.place(x=10, y=480)

        upld_foto_btn = tk.Button(self.viewdata_frame, text='Choose File', command=lambda: self.open_image())
        upld_foto_btn.place(x=10, y=510, width=100, height=32)

        add_book_btn = tk.Button(self.viewdata_frame, text="Add", command=lambda: self.add_book())
        add_book_btn.place(x=10, y=550, width=100, height=30)

        edit_book_btn = tk.Button(self.viewdata_frame, text="Edit", command=lambda: self.edit_book())
        edit_book_btn.place(x=10, y=590, width=100, height=30)

        # Navigation Button
        clear_book_btn = tk.Button(self, text="Clear", command=lambda: self.clear(), font=("Calibri", 12), bd=3, fg="black")
        clear_book_btn.place(x=10, y=550, width=120, height=35)

        back_btn = tk.Button(self, text="Back", command=lambda: self.ctrl.show("AdminHomePage"), font=("Calibri", 12), bd=3, fg="black")
        back_btn.place(x=10, y=600, width=120, height=35)

        # bind select book handler
        self.my_tabel.bind("<ButtonRelease-1>", self.on_book_click_handler)

    def set_image(self, b64_image):
        self.book_image = Image.open(io.BytesIO(base64.b64decode(b64_image))).resize((150, 200))
        self.book_image_tk = ImageTk.PhotoImage(self.book_image)
        self.book_image_lbl = tk.Label(self.viewdata_frame, image=self.book_image_tk)

        # position image
        self.book_image_lbl.place(x=200, y=480)

    def open_image(self):
        f_types = [['JPG or PNG Files', '*.jpg *.png']]
        self.filename = filedialog.askopenfilename(filetypes=f_types)

        if not self.filename:
            return

        self.book_image = Image.open(self.filename).resize((150, 200))
        self.book_image_tk = ImageTk.PhotoImage(self.book_image)
        self.book_image_lbl = tk.Label(self.viewdata_frame, image=self.book_image_tk)

        # position image
        self.book_image_lbl.place(x=200, y=480)

    def get_b64_image_data(self) -> str:
        buffered = io.BytesIO()
        self.book_image.save(buffered, format="png")
        data = base64.b64encode(buffered.getvalue()).decode('ascii')
        return data

    def on_book_click_handler(self, a):
        # clear entry boxes
        self.clear()

        # grab record number
        selected = self.my_tabel.focus()
        if selected == "":
            return

        # grab record values
        values = self.my_tabel.item(selected, 'values')

        selected_book: dict = {}

        for book in self.books:
            if book["id"] == values[0]:
                selected_book = book
                break

        # output to entry boxes
        self.txt_idbuku.configure(state=NORMAL)
        self.txt_idbuku.insert(0, selected_book["id"])
        self.txt_idbuku.configure(state="readonly")
        self.txt_namabuku.insert(0, selected_book["name"])
        self.txt_pengarangbuku.insert(0, selected_book["author"])
        self.txt_penerbitbuku.insert(0, selected_book["publisher"])
        self.txt_kategoribuku.insert(0, selected_book["category"])
        self.txt_bahasabuku.insert(0, selected_book["language"])
        self.txt_deskripsibuku.insert("1.0", selected_book["description"])
        self.txt_hargabuku.insert(0, selected_book["price"])
        self.txt_stokbuku.insert(0, selected_book["qty"])
        self.set_image(selected_book["image"])

    def get_details_data(self) -> dict:
        return {
            "id": self.txt_idbuku.get().strip(),
            "name": self.txt_namabuku.get().strip(),
            "author": self.txt_pengarangbuku.get().strip(),
            "publisher": self.txt_penerbitbuku.get().strip(),
            "category": self.txt_kategoribuku.get().strip(),
            "language": self.txt_bahasabuku.get().strip(),
            "description": self.txt_deskripsibuku.get("1.0", END).strip(),
            "price": int(self.txt_hargabuku.get().strip()),
            "qty": int(self.txt_stokbuku.get().strip()),
            "image": self.get_b64_image_data()
        }

    def clear(self):
        # clear entry boxes
        self.txt_idbuku.configure(state=NORMAL)
        self.txt_idbuku.delete(0, END)
        self.txt_idbuku.configure(state="readonly")
        self.txt_namabuku.delete(0, END)
        self.txt_pengarangbuku.delete(0, END)
        self.txt_penerbitbuku.delete(0, END)
        self.txt_kategoribuku.delete(0, END)
        self.txt_bahasabuku.delete(0, END)
        self.txt_deskripsibuku.delete("1.0", END)
        self.txt_hargabuku.delete(0, END)
        self.txt_stokbuku.delete(0, END)

    def get_books(self):
        res: Response = self.ctrl.apis.get_all_books()
        if res.is_err():
            return self.ctrl.show("AdminHomePage")

        table_data = []
        for d in res.result():
            table_data.append(d)

        self.books = table_data

    def add_book(self):
        data = self.get_details_data()
        res: Response = self.ctrl.apis.add_book(
            name=data["name"],
            author=data["author"],
            publisher=data["publisher"],
            category=data["category"],
            language=data["language"],
            description=data["description"],
            price=data["price"],
            qty=data["qty"],
            image=data["image"],
        )
        if res.is_err():
            return

        messagebox.showinfo("Info", res.result())

    def edit_book(self):
        data = self.get_details_data()
        res: Response = self.ctrl.apis.edit_book(
            id=data["id"],
            name=data["name"],
            author=data["author"],
            publisher=data["publisher"],
            category=data["category"],
            language=data["language"],
            description=data["description"],
            price=data["price"],
            qty=data["qty"],
            image=data["image"],
        )
        if res.is_err():
            return

        messagebox.showinfo("Info", res.result())
        self.render()
