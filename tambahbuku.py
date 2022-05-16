from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import json
import mysql.connector


class tambahbuku_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Tambah Buku")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="Tambah Buku", fg="black", font=("Calibri", 30, "bold"))
        lbltitle.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

        # frame input data
        inputdatabukuframe = Frame(self.root, bg="#D1D1D1")
        inputdatabukuframe.place(x=50, y=80, width=1440, height=680)

        # form input data
        label_nama_buku = Label(inputdatabukuframe, text="Nama Buku :", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_nama_buku.place(x=40, y=40)
        label_pengarang_buku = Label(inputdatabukuframe, text="Pengarang Buku :", font=("Calibri", 15), fg="black",
                                     bg="#D1D1D1")
        label_pengarang_buku.place(x=40, y=120)
        label_penerbit_buku = Label(inputdatabukuframe, text="Penerbit Buku :", font=("Calibri", 15), fg="black",
                                    bg="#D1D1D1")
        label_penerbit_buku.place(x=40, y=200)
        label_kategori_buku = Label(inputdatabukuframe, text="Kategori Buku :", font=("Calibri", 15), fg="black",
                                    bg="#D1D1D1")
        label_kategori_buku.place(x=40, y=280)
        label_bahasa_buku = Label(inputdatabukuframe, text="Bahasa Buku :", font=("Calibri", 15), fg="black",
                                  bg="#D1D1D1")
        label_bahasa_buku.place(x=720, y=40)
        label_harga_buku = Label(inputdatabukuframe, text="Harga Buku :", font=("Calibri", 15), fg="black",
                                 bg="#D1D1D1")
        label_harga_buku.place(x=720, y=120)
        label_stok_buku = Label(inputdatabukuframe, text="Stok Buku :", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_stok_buku.place(x=720, y=200)
        label_deskripsi_buku = Label(inputdatabukuframe, text="Deskripsi Buku :", font=("Calibri", 15), fg="black",
                                     bg="#D1D1D1")
        label_deskripsi_buku.place(x=40, y=360)

        # entri boxes
        self.txt_namabuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_namabuku.place(x=40, y=80, width=640)
        self.txt_pengarangbuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_pengarangbuku.place(x=40, y=160, width=640)
        self.txt_penerbitbuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_penerbitbuku.place(x=40, y=240, width=640)
        self.txt_kategoribuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_kategoribuku.place(x=40, y=320, width=640)
        self.txt_bahasabuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_bahasabuku.place(x=720, y=80, width=640)
        self.txt_hargabuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_hargabuku.place(x=720, y=160, width=640)
        self.txt_stokbuku = ttk.Entry(inputdatabukuframe, font=("Calibri", 13))
        self.txt_stokbuku.place(x=720, y=240, width=640)
        self.txt_deskripsibuku = Text(inputdatabukuframe, font=("Calibri", 13))
        self.txt_deskripsibuku.place(x=40, y=400, width=1360, height=185)

        # button tambah buku
        tambahbuku_btn = Button(inputdatabukuframe, command=self.tambahbuku, text="Tambah Buku", font=("Calibri", 15),
                                bd=3, fg="black")
        tambahbuku_btn.place(x=40, y=625, width=200, height=35)

    def tambahbuku(self):
        Nama_Buku = self.txt_namabuku.get()
        Pengarang_Buku = self.txt_pengarangbuku.get()
        Penerbit_Buku = self.txt_penerbitbuku.get()
        Kategori_Buku = self.txt_kategoribuku.get()
        Bahasa_Buku = self.txt_bahasabuku.get()
        Harga_Buku = self.txt_hargabuku.get()
        Stok_Buku = self.txt_stokbuku.get()
        Deskripsi_Buku = self.txt_deskripsibuku.get(1.0, END)

        # creating dictionary
        data_tambah_buku = {}
        data_tambah_buku['Nama_Buku'] = Nama_Buku
        data_tambah_buku['Pengarang_Buku'] = Pengarang_Buku
        data_tambah_buku['Penerbit_Buku'] = Penerbit_Buku
        data_tambah_buku['Kategori_Buku'] = Kategori_Buku
        data_tambah_buku['Bahasa_Buku'] = Bahasa_Buku
        data_tambah_buku['Harga_Buku'] = Harga_Buku
        data_tambah_buku['Stok_Buku'] = Stok_Buku
        data_tambah_buku['Deskripsi_Buku'] = Deskripsi_Buku

        # print(idbuku," ", namabuku," ", pengarangbuku," ",kategoribuku," ",hargabuku," ",stokbuku)
        # data_tambahbuku = '''{ 'Nama_Buku': '%s', 'Pengarang_Buku': '%s', 'Penerbit_Buku': '%s', 'Kategori_Buku': '%s', 'Bahasa_Buku': '%s', 'Harga_Buku': %s, 'Stok_Buku': %s, 'Deskripsi_Buku': %s}''' %(Nama_Buku, Pengarang_Buku, Penerbit_Buku, Kategori_Buku, Bahasa_Buku, Harga_Buku, Stok_Buku, Deskripsi_Buku)
        # print(data_tambahbuku)
        out_file = open("data_tambah_buku.json", "w")
        json.dump(data_tambah_buku, out_file)
        print(data_tambah_buku)

        # convert string to object
        # json_object = json.loads(data_tambahbuku)

        # print untuk ngecek
        # print(type(json_object))

        # json_object = json.dumps(data_tambahbuku, indent = 4)
        # print(json_object)
        # with open("datatambahbuku.json","w") as outfile:
        #    outfile.write(json_object)


if __name__ == "__main__":
    root = Tk()
    app = tambahbuku_window(root)
    root.mainloop()
