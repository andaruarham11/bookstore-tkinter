from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector


class databuku_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Buku")
        self.root.geometry("1550x800+0+0")

        self.id_buku = StringVar()
        self.nama_buku = StringVar()
        self.pengarang_buku = StringVar()
        self.penerbit_buku = StringVar()
        self.kategori_buku = StringVar()
        self.bahasa_buku = StringVar()
        self.harga_buku = StringVar()
        self.stok_buku = StringVar()

        # lbltitle = Label(self.root,text="Data Buku",fg="black",font=("Calibri",30,"bold"))
        # lbltitle.grid(row=0,column=0, sticky=W, columnspan=2, padx=10, pady=10)

        # style
        style = ttk.Style()

        # theme
        style.theme_use('default')

        # configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="white")

        # change selected color
        style.map('Treeview', background=[('selected', "lemonchiffon4")])

        # frame tabel
        tabel_frame = Frame(self.root)
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
        self.my_tabel['column'] = (
            "IDBuku", "Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku",
            "Stok Buku")

        # headings
        self.my_tabel.heading("#0", text="", anchor=W)
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
        self.my_tabel.column("#0", width=0, stretch=NO)
        self.my_tabel.column("IDBuku", width=100)
        self.my_tabel.column("Nama Buku", width=100)
        self.my_tabel.column("Pengarang Buku", width=100)
        self.my_tabel.column("Penerbit Buku", width=100)
        self.my_tabel.column("Kategori Buku", width=100)
        self.my_tabel.column("Bahasa Buku", width=100)
        self.my_tabel.column("Harga Buku", width=100)
        self.my_tabel.column("Stok Buku", width=100)

        self.my_tabel.pack(fill=BOTH, expand=1)

        # data dummy
        data = [
            [1, "Bibi Gill", "Tere Liye", "PENERBIT SABAK GRIP", "Fiksi Ilmiah", "Indonesia", 89000, 50],
            [2, "Spy X Family 03", "Endo Tatsuya", "Elex Media Komputindo", "Manga", "Indonesia", 36000, 50],
            [3, "Laut Bercerita", "Leila S. Chudori", "Kepustakaan Populer Gramedia", "Fiksi Ilmiah", "Indonesia",
             70000, 50],
            [4, "Sebuah Seni untuk Bersikap Bodo Amat", "Nark Manson", "Gramedia Widiasarana Indonesia",
             "Pengembangan Diri", "Indonesia", 54600, 50],
            [5, "Hai, Miko! 34 - Premium", "Ono Eriko", "m&c!", "Manga", "Indonesia", 42000, 50],
            [6, "Home Sweet Loan", "Almira Bastari", "Gramedia Pustaka Utama", "Novel", "Indonesia", 66500, 50],
            [7, "Jujutsu Kaisen 05", "Gege Akutami", "Elex Media Komputindo", "Manga", "Indonesia", 32000, 50],
            [8, "Sagaras", "Tere Liye", "PENERBIT SABAK GRIP", "Fiksi Ilmiah", "Indonesia", 89000, 50],
            [9, "Merawat Luka Batin", "Dr Jiemi Ardian", "Gramedia Pustaka Utama", "Pengembangan Diri", "Indonesia",
             78400, 50],
            [10, "Heartbreak Motel", "Ika Natassa", "Gramedia Pustaka Utama", "Romance", "Indonesia", 69300, 50],
            [11, "Anak Bajang Mengayun Bulan", "Sindhunata", "Gramedia Pustaka Utama", "Novel", "Indonesia", 170800,
             50],
            [12, "Pachinko", "Min Jin Lee", "Gramedia Pustaka Utama", "Romance", "Indonesia", 95200, 50],
            [13, "Cr: The Sweetest Hours", "Cathryn Parry", "Elex Media Komputindo", "Romance", "Indonesia", 72000, 50],
            [14, "Membasmi Frustasi Fotografer", "Edwin Effendi", "Elex Media Komputindo", "Seni Desain", "Indonesia",
             72000, 50],
            [15, "Panduan Praktis Seminar Edisi Ketiga", "Indra Yuzal", "Pt Rajagrafindo Persada", "Pendidikan",
             "Indonesia", 69000, 50],
            [16, "Cake Kekinian Favorit", "Meida Felici", "Gramedia Pustaka Utama", "Buku Masakan", "Indonesia", 78400,
             50],
            [17, "Yuk Belajar Nabung Saham", "Ryan Filbert Wijaya, S.Sn, ME.", "Elex Media Komputindo", "Finansial",
             "Indonesia", 63000, 50],
            [18, "Siap-Siap Jadi Orangtua", "Najelaa Shihab", "Buah Hati", "Buku Parenting", "Indonesia", 120000, 50],
            [19, "Violet", "Kyung Sook Shin", "Gramedia Pustaka Utama", "Sastra", "Indonesia", 61600, 50],
            [20, "35 Fabel Anak", "Any Hidayati", "Anak Hebat Indonesia", "Buku Anak", "Indonesia", 55500, 50]
        ]

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lemonchiffon3")

        # add our data to the screen
        global count
        count = 0

        for record in data:
            if count % 2 == 0:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                                     tags=('evenrow',))
            else:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                                     tags=('oddrow',))

            # increment count
            count += 1

        # add entry boxes
        # frame
        viewdata_frame = LabelFrame(self.root, text="Details")
        viewdata_frame.place(x=785, y=30, width=735, height=750)

        # form input data
        label_nama_buku = Label(viewdata_frame, text="Nama Buku :", fg="black")
        label_nama_buku.place(x=10, y=30)
        label_pengarang_buku = Label(viewdata_frame, text="Pengarang Buku :", fg="black")
        label_pengarang_buku.place(x=10, y=60)
        label_penerbit_buku = Label(viewdata_frame, text="Penerbit Buku :", fg="black")
        label_penerbit_buku.place(x=10, y=90)
        label_kategori_buku = Label(viewdata_frame, text="Kategori Buku :", fg="black")
        label_kategori_buku.place(x=10, y=120)
        label_bahasa_buku = Label(viewdata_frame, text="Bahasa Buku :", fg="black")
        label_bahasa_buku.place(x=10, y=150)
        label_harga_buku = Label(viewdata_frame, text="Harga Buku :", fg="black")
        label_harga_buku.place(x=10, y=180)
        label_stok_buku = Label(viewdata_frame, text="Stok Buku :", fg="black")
        label_stok_buku.place(x=10, y=210)
        label_deskripsi_buku = Label(viewdata_frame, text="Deskripsi Buku :", fg="black")
        label_deskripsi_buku.place(x=10, y=240)

        # entry boxes
        self.txt_namabuku = ttk.Entry(viewdata_frame)
        self.txt_namabuku.place(x=135, y=30, width=550)
        self.txt_pengarangbuku = ttk.Entry(viewdata_frame)
        self.txt_pengarangbuku.place(x=135, y=60, width=550)
        self.txt_penerbitbuku = ttk.Entry(viewdata_frame)
        self.txt_penerbitbuku.place(x=135, y=90, width=550)
        self.txt_kategoribuku = ttk.Entry(viewdata_frame)
        self.txt_kategoribuku.place(x=135, y=120, width=550)
        self.txt_bahasabuku = ttk.Entry(viewdata_frame)
        self.txt_bahasabuku.place(x=135, y=150, width=550)
        self.txt_hargabuku = ttk.Entry(viewdata_frame)
        self.txt_hargabuku.place(x=135, y=180, width=550)
        self.txt_stokbuku = ttk.Entry(viewdata_frame)
        self.txt_stokbuku.place(x=135, y=210, width=550)
        self.txt_deskripsibuku = Text(viewdata_frame)
        self.txt_deskripsibuku.place(x=135, y=240, width=550, height=185)

        # add buttons
        # button tambah buku
        add_new_book_btn = Button(self.root, text="tambah", font=("Calibri", 12), bd=3, fg="black")
        add_new_book_btn.place(x=10, y=550, width=120, height=35)

        delete_book_btn = Button(self.root, text="hapus", font=("Calibri", 12), bd=3, fg="black")
        delete_book_btn.place(x=130, y=550, width=120, height=35)

        viewall_book_btn = Button(self.root, text="lihat detail", font=("Calibri", 12), bd=3, fg="black")
        viewall_book_btn.place(x=250, y=550, width=180, height=35)

        edit_book_btn = Button(self.root, text="edit", font=("Calibri", 12), bd=3, fg="black")
        edit_book_btn.place(x=430, y=550, width=120, height=35)

    '''def add_new_book(self):
        self.new_window=Toplevel(self.root)
        self.app=tambahbuku_window(self.new_window)'''


if __name__ == "__main__":
    root = Tk()
    app = databuku_window(root)
    root.mainloop()
