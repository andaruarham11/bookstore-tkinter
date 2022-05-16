# coba ambil data dari json ke tabel
from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector
import json
import requests

data = requests.get('https://reqres.in/api/users?page=2')


class user:
    def __init__(self, id, email, first_name, last_name):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


def import_json_to_list(data):
    list = []
    data = data.json()
    j = 0
    for i in data['data']:
        # _data = book(i['id'], i['nama_buku'], i['pengarang_buku'], i['penerbit_buku'], i['kategori'], i['bahasa'], i['harga'], i['stok'], i['deskripsi'])
        _data = user(i['id'], i['email'], i['first_name'], i['last_name'])
        list.append(_data)
        print('test isi dari list: %d %s %s %s' % (list[j].id, list[j].email, list[j].first_name, list[j].last_name))
        j += 1
    return list


# l = import_json_to_list(data)

# ----------------------------------------------------------------------------------------------------------------
class databuku_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Buku")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="Data Buku", fg="black", font=("Calibri", 30, "bold"))
        lbltitle.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

        # style
        style = ttk.Style()

        # theme
        style.theme_use('default')

        # configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=30, fieldbackground="white")

        # change selected color
        style.map('Treeview', background=[('selected', "#347083")])

        # frame tabel
        tabel_frame = Frame(self.root)
        tabel_frame.place(x=10, y=150, width=1510, height=620)

        # scrollbar
        tabel_scroll = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        tabel_scroll.pack(side=RIGHT, fill=Y)

        # create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, column=("ID", "Email", "First Name", "Last Name"),
                                     yscrollcommand=tabel_scroll.set)
        self.my_tabel.pack()

        # configure our columns
        tabel_scroll = ttk.Scrollbar(command=self.my_tabel.yview)

        # define columns
        # self.my_tabel['column'] = ("IDBuku","Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku")

        # headings
        self.my_tabel.heading("#0", text="", anchor=W)
        self.my_tabel.heading("ID", text="ID")
        self.my_tabel.heading("Email", text="Email")
        self.my_tabel.heading("First Name", text="First Name")
        self.my_tabel.heading("Last Name", text="Last Name")

        self.my_tabel["show"] = "headings"

        # format columns
        self.my_tabel.column("#0", width=0, stretch=NO)
        self.my_tabel.column("ID", width=100)
        self.my_tabel.column("Email", width=100)
        self.my_tabel.column("First Name", width=100)
        self.my_tabel.column("Last Name", width=100)

        self.my_tabel.pack(fill=BOTH, expand=1)

        # data dummy
        l = import_json_to_list(data)

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lemonchiffon3")

        # add our data to the screen
        global count
        count = 0

        for record in l:
            if count % 2 == 0:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}',
                                     values=(record.id, record.email, record.first_name, record.last_name),
                                     tags=('evenrow',))
            else:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}',
                                     values=(record.id, record.email, record.first_name, record.last_name),
                                     tags=('oddrow',))

            # increment count
            count += 1

        # add buttons
        # button tambah buku
        add_new_book_btn = Button(self.root, text="tambah", font=("Calibri", 12), bd=3, fg="black")
        add_new_book_btn.place(x=1350, y=80, width=120, height=35)

        delete_book_btn = Button(self.root, text="hapus", font=("Calibri", 12), bd=3, fg="black")
        delete_book_btn.place(x=1230, y=80, width=120, height=35)

        viewall_book_btn = Button(self.root, text="lihat detail", font=("Calibri", 12), bd=3, fg="black")
        viewall_book_btn.place(x=1050, y=80, width=180, height=35)

        edit_book_btn = Button(self.root, text="edit", font=("Calibri", 12), bd=3, fg="black")
        edit_book_btn.place(x=930, y=80, width=120, height=35)


if __name__ == "__main__":
    root = Tk()
    app = databuku_window(root)
    root.mainloop()
