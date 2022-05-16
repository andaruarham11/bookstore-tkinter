# import tkinter as tk
# from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# import requests
import json

# import mysql.connector
from showcase.dummyData import dummy_record


def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")

        # self.bg = PhotoImage(file="background-login-page.jpg")

        # lbl_bg = Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="#D1D1D1")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="Welcome, Customer", font=("Calibri", 20, "bold"), fg="black", bg="#D1D1D1")
        get_str.place(x=60, y=60)

        # label
        label_username = lbl = Label(frame, text="Username:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_username.place(x=40, y=140)

        self.txtUser = ttk.Entry(frame, font=("Calibri", 13))
        self.txtUser.place(x=40, y=170, width=260)

        label_password = lbl = Label(frame, text="Password:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_password.place(x=40, y=200)

        self.txtPass = ttk.Entry(frame, font=("Calibri", 13), show='*')
        self.txtPass.place(x=40, y=230, width=260)

        # login button
        login_btn = Button(frame, command=self.login, text="Login", font=("Calibri", 15), bd=3, relief=RAISED,
                           fg="white", bg="#008A31")
        login_btn.place(x=110, y=350, width=120, height=35)

    def login(self):

        id_admin = self.txtUser.get()
        password_admin = self.txtPass.get()

        if id_admin == "" or password_admin == "":
            messagebox.showerror("Error", "all field required")
        elif id_admin == "sabrina" and password_admin == "Admin123":
            # messagebox.showinfo("Success","Welcome to Bookstore")
            self.new_window = Toplevel(self.root)
            self.app = AdminPageWindow(self.new_window)
        else:
            messagebox.showerror("Invalid", "Invalid username or password")
            """conn=mysql.connector.connect(host="localhost",user="root",password="Admin123_",database="databaseadm")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from data admin where nama_admin=%s and password_admin=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.new_window=Toplevel(self.new_window)
                self.app=adminpage_window(self.new_window)
            
            conn.commit()
            conn.close()"""


class AdminPageWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page")
        self.root.geometry("1550x800+0+0")

        lbl_title = Label(self.root, text="Bookstore", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

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
        book_btn = Button(logo1_frame, command=self.book, text="Catalog Buku", font=("Calibri", 15), bd=3, fg="black")
        book_btn.place(x=125, y=290, width=150, height=50)

        customer_btn = Button(logo2_frame, text="Status Pembayaran", font=("Calibri", 15), bd=3, fg="black")
        customer_btn.place(x=100, y=290, width=200, height=50)

    def book(self):
        self.new_window = Toplevel(self.root)
        self.app = DataBukuWindow(self.new_window)


class DataBukuWindow:
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

        lbl_title = Label(self.root, text="Data Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

        # style
        style = ttk.Style()

        # theme
        style.theme_use('default')

        # configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=40, fieldbackground="#D3D3D3")

        # change selected color
        style.map('Treeview', background=[('selected', "#347083")])

        # frame tabel
        tabel_frame = Frame(self.root)
        tabel_frame.place(x=10, y=150, width=1510, height=600)

        # scrollbar
        tabel_scroll = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        tabel_scroll.pack(side=RIGHT, fill=Y)

        # create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, column=("IDBuku", "Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku"),
                                     yscrollcommand=tabel_scroll.set)
        self.my_tabel.pack()

        # configure our columns
        tabel_scroll = ttk.Scrollbar(command=self.my_tabel.yview)

        # define columns
        # self.my_tabel['column'] = ("IDBuku","Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku")

        # headings
        # self.my_tabel.heading("#0", text="", anchor=W)
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

        self.my_tabel.pack(fill=BOTH, expand=1)

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lavenderblush1")

        # add our data to the screen
        global count
        count = 0

        for record in dummy_record:
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

        # add buttons
        # button tambah buku
        add_new_book_btn = Button(self.root, command=self.add_new_book, text="tambah", font=("Calibri", 15), bd=3,
                                  fg="black")
        add_new_book_btn.place(x=1350, y=80, width=120, height=35)

        delete_book_btn = Button(self.root, text="hapus", font=("Calibri", 15), bd=3, fg="black")
        delete_book_btn.place(x=1230, y=80, width=120, height=35)

        viewall_book_btn = Button(self.root, text="lihat detail", font=("Calibri", 15), bd=3, fg="black")
        viewall_book_btn.place(x=1050, y=80, width=180, height=35)

    def add_new_book(self):
        self.new_window = Toplevel(self.root)
        self.app = TambahBukuWindow(self.new_window)


class TambahBukuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Tambah Buku")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="Tambah Buku", fg="black", font=("Calibri", 30, "bold"))
        lbltitle.grid(row=0, column=0, sticky=W, columnspan=2, padx=10, pady=10)

        # frame input data
        input_data_bukuframe = Frame(self.root, bg="#D1D1D1")
        input_data_bukuframe.place(x=50, y=80, width=1440, height=680)

        # form input data
        label_nama_buku = Label(input_data_bukuframe, text="Nama Buku :", font=("Calibri", 15), fg="black",
                                bg="#D1D1D1")
        label_nama_buku.place(x=40, y=40)
        label_pengarang_buku = Label(input_data_bukuframe, text="Pengarang Buku :", font=("Calibri", 15), fg="black",
                                     bg="#D1D1D1")
        label_pengarang_buku.place(x=40, y=120)
        label_penerbit_buku = Label(input_data_bukuframe, text="Penerbit Buku :", font=("Calibri", 15), fg="black",
                                    bg="#D1D1D1")
        label_penerbit_buku.place(x=40, y=200)
        label_kategori_buku = Label(input_data_bukuframe, text="Kategori Buku :", font=("Calibri", 15), fg="black",
                                    bg="#D1D1D1")
        label_kategori_buku.place(x=40, y=280)
        label_bahasa_buku = Label(input_data_bukuframe, text="Bahasa Buku :", font=("Calibri", 15), fg="black",
                                  bg="#D1D1D1")
        label_bahasa_buku.place(x=720, y=40)
        label_harga_buku = Label(input_data_bukuframe, text="Harga Buku :", font=("Calibri", 15), fg="black",
                                 bg="#D1D1D1")
        label_harga_buku.place(x=720, y=120)
        label_stok_buku = Label(input_data_bukuframe, text="Stok Buku :", font=("Calibri", 15), fg="black",
                                bg="#D1D1D1")
        label_stok_buku.place(x=720, y=200)
        label_deskripsi_buku = Label(input_data_bukuframe, text="Deskripsi Buku :", font=("Calibri", 15), fg="black",
                                     bg="#D1D1D1")
        label_deskripsi_buku.place(x=40, y=360)

        # entri boxes
        self.txt_namabuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_namabuku.place(x=40, y=80, width=640)
        self.txt_pengarangbuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_pengarangbuku.place(x=40, y=160, width=640)
        self.txt_penerbitbuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_penerbitbuku.place(x=40, y=240, width=640)
        self.txt_kategoribuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_kategoribuku.place(x=40, y=320, width=640)
        self.txt_bahasabuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_bahasabuku.place(x=720, y=80, width=640)
        self.txt_hargabuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_hargabuku.place(x=720, y=160, width=640)
        self.txt_stokbuku = ttk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_stokbuku.place(x=720, y=240, width=640)
        self.txt_deskripsibuku = Text(input_data_bukuframe, font=("Calibri", 13))
        self.txt_deskripsibuku.place(x=40, y=400, width=1360, height=185)

        # button tambah buku
        tambahbuku_btn = Button(input_data_bukuframe, command=self.tambahbuku, text="Tambah Buku", font=("Calibri", 15),
                                bd=3, fg="black")
        tambahbuku_btn.place(x=40, y=625, width=200, height=35)

    def tambah_buku(self):
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
    main()
