from __future__ import annotations

import json
import tkinter as tk
from tkinter import constants as tk_const, messagebox, ttk
from typing import Any

from PIL import Image, ImageTk

from showcase.dummyData import dummy_record


def main():
    app = CoreApp()
    app.mainloop()


class CoreApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_frame()
        self.custom_state = {}

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frame_list = (LoginPage, AdminPage, DataBukuPage, TambahBukuPage, DetailBukuPage)
        # self.frames = {}
        # for F in self.frame_list:
        #     page_name = F.__name__
        #     frame = F(parent=self.container, controller=self)
        #     self.frames[page_name] = frame

        # self.show_frame("DetailBukuPage")
        self.show_frame("LoginPage")
        self.geometry("1550x800+0+0")

    def clean_frame(self, select_page_name):
        for F in self.frame_list:
            if select_page_name == F.__name__:
                F(parent=self.container, controller=self)

    def show_frame(self, page_name):
        for F in self.frame_list:
            if page_name == F.__name__:
                frame = F(parent=self.container, controller=self)
                frame.grid(row=0, column=0, sticky="nsew")
                frame.tkraise()

        self.title(page_name)

    def set_window_title(self, title):
        self.title(title)

    def set_s(self, state):
        self.custom_state = state

    def get_s(self) -> dict:
        return self.custom_state


class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Admin Page")

        lbl_title = tk.Label(self, text="Bookstore", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        # frame logo
        book_frame = tk.Frame(self, bg="#D1D1D1")
        book_frame.place(x=275, y=200, width=400, height=400)

        pay_frame = tk.Frame(self, bg="#D1D1D1")
        pay_frame.place(x=875, y=200, width=400, height=400)

        # frame logo
        book_img = Image.open("../books.png")
        resize_book_image = book_img.resize((150, 150))
        self.image_book = ImageTk.PhotoImage(resize_book_image)
        image_book_label = tk.Label(book_frame, image=self.image_book, bg="#D1D1D1")
        image_book_label.place(x=125, y=80)

        pay_img = Image.open("../pay.png")
        resize_pay_img = pay_img.resize((150, 150))
        self.image_pay = ImageTk.PhotoImage(resize_pay_img)
        image_pay_label = tk.Label(pay_frame, image=self.image_pay, bg="#D1D1D1")
        image_pay_label.place(x=125, y=80)

        # button
        book_btn = tk.Button(book_frame, command=lambda: controller.show_frame("DataBukuPage"), text="Catalog Buku", font=("Calibri", 15), bd=3, fg="black")
        book_btn.place(x=125, y=290, width=150, height=50)

        customer_btn = tk.Button(pay_frame, text="Status Pembayaran", font=("Calibri", 15), bd=3, fg="black")
        customer_btn.place(x=100, y=290, width=200, height=50)

        # logout button
        logout_btn = tk.Button(self, command=lambda: controller.show_frame("LoginPage"), text="Logout", font=("Calibri", 15), bd=3, fg="black")
        logout_btn.place(x=0, y=80, width=120, height=35)
        ########


class TambahBukuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.winfo_toplevel().title("Tambah Buku Page")

        lbltitle = tk.Label(self, text="Tambah Buku", fg="black", font=("Calibri", 30, "bold"))
        lbltitle.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        # frame input data
        input_data_bukuframe = tk.Frame(self, bg="#D1D1D1")
        input_data_bukuframe.place(x=50, y=80, width=1440, height=680)

        # form input data
        label_nama_buku = tk.Label(input_data_bukuframe, text="Nama Buku :", font=("Calibri", 15), fg="black",
                                   bg="#D1D1D1")
        label_nama_buku.place(x=40, y=40)
        label_pengarang_buku = tk.Label(input_data_bukuframe, text="Pengarang Buku :", font=("Calibri", 15), fg="black",
                                        bg="#D1D1D1")
        label_pengarang_buku.place(x=40, y=120)
        label_penerbit_buku = tk.Label(input_data_bukuframe, text="Penerbit Buku :", font=("Calibri", 15), fg="black",
                                       bg="#D1D1D1")
        label_penerbit_buku.place(x=40, y=200)
        label_kategori_buku = tk.Label(input_data_bukuframe, text="Kategori Buku :", font=("Calibri", 15), fg="black",
                                       bg="#D1D1D1")
        label_kategori_buku.place(x=40, y=280)
        label_bahasa_buku = tk.Label(input_data_bukuframe, text="Bahasa Buku :", font=("Calibri", 15), fg="black",
                                     bg="#D1D1D1")
        label_bahasa_buku.place(x=720, y=40)
        label_harga_buku = tk.Label(input_data_bukuframe, text="Harga Buku :", font=("Calibri", 15), fg="black",
                                    bg="#D1D1D1")
        label_harga_buku.place(x=720, y=120)
        label_stok_buku = tk.Label(input_data_bukuframe, text="Stok Buku :", font=("Calibri", 15), fg="black",
                                   bg="#D1D1D1")
        label_stok_buku.place(x=720, y=200)
        label_deskripsi_buku = tk.Label(input_data_bukuframe, text="Deskripsi Buku :", font=("Calibri", 15), fg="black",
                                        bg="#D1D1D1")
        label_deskripsi_buku.place(x=40, y=360)

        # entri boxes
        self.txt_namabuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_namabuku.place(x=40, y=80, width=640)
        self.txt_pengarangbuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_pengarangbuku.place(x=40, y=160, width=640)
        self.txt_penerbitbuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_penerbitbuku.place(x=40, y=240, width=640)
        self.txt_kategoribuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_kategoribuku.place(x=40, y=320, width=640)
        self.txt_bahasabuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_bahasabuku.place(x=720, y=80, width=640)
        self.txt_hargabuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_hargabuku.place(x=720, y=160, width=640)
        self.txt_stokbuku = tk.Entry(input_data_bukuframe, font=("Calibri", 13))
        self.txt_stokbuku.place(x=720, y=240, width=640)
        self.txt_deskripsibuku = tk.Text(input_data_bukuframe, font=("Calibri", 13))
        self.txt_deskripsibuku.place(x=40, y=400, width=1360, height=185)

        # button tambah buku
        tambahbuku_btn = tk.Button(input_data_bukuframe, command=self.tambah_buku, text="Tambah Buku", font=("Calibri", 15), bd=3, fg="black")
        tambahbuku_btn.place(x=40, y=625, width=200, height=35)

        back_to_data_buku_page_btn = tk.Button(input_data_bukuframe, command=lambda: controller.show_frame("DataBukuPage"), text="Kembali", font=("Calibri", 15), bd=3, fg="black")
        back_to_data_buku_page_btn.place(x=1200, y=625, width=200, height=35)

    ########

    def tambah_buku(self):
        Nama_Buku = self.txt_namabuku.get()
        Pengarang_Buku = self.txt_pengarangbuku.get()
        Penerbit_Buku = self.txt_penerbitbuku.get()
        Kategori_Buku = self.txt_kategoribuku.get()
        Bahasa_Buku = self.txt_bahasabuku.get()
        Harga_Buku = self.txt_hargabuku.get()
        Stok_Buku = self.txt_stokbuku.get()
        Deskripsi_Buku = self.txt_deskripsibuku.get(1.0, tk_const.END)

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
        out_file = open("../data_tambah_buku.json", "w")
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


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Login Page")

        # create frame and place
        frame = tk.Frame(self, bg="#D1D1D1")
        frame.place(x=610, y=170, width=340, height=450)

        # greet label
        lbl_greet = tk.Label(frame, text="Welcome, Customer", font=("Calibri", 20, "bold"), fg="black", bg="#D1D1D1")
        lbl_greet.place(x=60, y=60)

        # save user txt
        self.txtUser = tk.Entry(frame, font=("Calibri", 13))
        self.txtUser.place(x=40, y=170, width=260)

        label_password = tk.Label(frame, text="Password:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_password.place(x=40, y=200)

        self.txtPass = tk.Entry(frame, font=("Calibri", 13), show='*')
        self.txtPass.place(x=40, y=230, width=260)

        # login button
        login_btn = tk.Button(frame, command=self.do_login, text="Login", font=("Calibri", 15), bd=3, relief=tk_const.RAISED, fg="white", bg="#008A31")
        login_btn.place(x=110, y=350, width=120, height=35)

    def do_login(self):
        id_admin = self.txtUser.get()
        password_admin = self.txtPass.get()

        if id_admin == "" or password_admin == "":
            messagebox.showerror("Error", "all field required")
        elif id_admin == "a" and password_admin == "a":
            # messagebox.showinfo("Success","Welcome to Bookstore")
            self.controller.show_frame("AdminPage")
        else:
            messagebox.showerror("Invalid", "Invalid username or password")
            """conn=mysql.connector.connect(host="localhost",user="root",password="Admin123_",database="databaseadm")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from data admin where nama_admin=%s and password_admin=%s",(self.txtuser.get(),self.txtpass.get()))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.new_window=Toplevel(self.new_window)
                self.app=adminpage_window(self.new_window)

            conn.commit()
            conn.close()"""


class DataBukuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Data Buku Page")

        self.id_buku = tk.StringVar()
        self.nama_buku = tk.StringVar()
        self.pengarang_buku = tk.StringVar()
        self.penerbit_buku = tk.StringVar()
        self.kategori_buku = tk.StringVar()
        self.bahasa_buku = tk.StringVar()
        self.harga_buku = tk.StringVar()
        self.stok_buku = tk.StringVar()

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

        # frame tabel
        tabel_frame = tk.Frame(self)
        tabel_frame.place(x=10, y=150, width=1510, height=600)

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

        # frame tabel
        tabel_frame = tk.Frame(self)
        tabel_frame.place(x=10, y=150, width=1510, height=600)

        # scrollbar
        tabel_scroll = tk.Scrollbar(tabel_frame, orient=tk_const.VERTICAL)
        tabel_scroll.pack(side=tk_const.RIGHT, fill=tk_const.Y)

        # create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, columns=("IDBuku", "Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku"),
                                     yscrollcommand=tabel_scroll.set)

        self.my_tabel.pack()

        # configure our columns
        tabel_scroll = tk.Scrollbar(command=self.my_tabel.yview)

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

        self.my_tabel.pack(fill=tk_const.BOTH, expand=1)

        # create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lavenderblush1")

        # add our data to the screen
        count = 0

        for record in dummy_record:
            if count % 2 == 0:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))

            # increment count
            count += 1

        # ########

        self.my_tabel.selected_item = None

        def select_item(a):
            cur_item = self.my_tabel.focus()
            self.my_tabel.selected_item = self.my_tabel.item(cur_item)
            table_data = self.my_tabel.selected_item["values"]

            # set dummy data
            self.controller.set_s({
                "id_buku": table_data[0],
                "nama_buku": table_data[1],
                "pengarang_buku": table_data[2],
                "penerbit_buku": table_data[3],
                "kategori_buku": table_data[4],
                "bahasa_buku": table_data[5],
                "harga_buku": table_data[6],
                "stok_buku": table_data[7],
            })
            self.controller.show_frame("DetailBukuPage")

        self.my_tabel.bind('<ButtonRelease-1>', select_item)

        # add buttons
        back_btn = tk.Button(self, command=lambda: controller.show_frame("AdminPage"), text="Kembali",
                             font=("Calibri", 15), bd=3, fg="black")
        back_btn.place(x=0, y=80, width=120, height=35)

        # # button tambah buku
        # add_new_book_btn = tk.Button(self,
        #                              command=lambda: controller.show_frame("TambahBukuPage"),
        #                              text="tambah",
        #                              font=("Calibri", 15), bd=3, fg="black")
        # add_new_book_btn.place(x=1350, y=80, width=120, height=35)
        #
        # delete_book_btn = tk.Button(self, text="hapus", font=("Calibri", 15), bd=3, fg="black")
        # delete_book_btn.place(x=1230, y=80, width=120, height=35)
        #
        # viewall_book_btn = tk.Button(self, text="lihat detail", font=("Calibri", 15), bd=3, fg="black")
        # viewall_book_btn.place(x=1050, y=80, width=180, height=35)


class DetailBukuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Detail Buku Page")

        self.style = ttk.Style()

        table_data = self.controller.get_s()

        lbl_title = tk.Label(self, text="Detail Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        ####

        back_btn = tk.Button(self, command=lambda: controller.show_frame("DataBukuPage"), text="Kembali", font=("Calibri", 15), bd=3, fg="black")
        back_btn.place(x=0, y=80, width=120, height=35)

        lbl_book_img = tk.Label(self, text="gambar buku", fg="black", font=("Calibri", 10, "bold"), compound="left", anchor='w')
        lbl_book_img.place(relx=0.213, rely=0.3, height=332, width=248)

        lbl_book_name = tk.Label(self, text=table_data["nama_buku"], fg="black", font=("Calibri", 22, "bold"), compound="left", anchor='w')
        lbl_book_name.place(relx=0.206, rely=0.163, height=52, width=1000)

        lbl_pengarang = ttk.Label(self, foreground="#000000", font="TkDefaultFont", relief="flat", anchor='w', justify='left', text='''Pengarang:''', compound='left')
        lbl_pengarang.place(relx=0.594, rely=0.25, height=32, width=122)

        self.TLabel1_1 = ttk.Label(self)
        self.TLabel1_1.place(relx=0.594, rely=0.313, height=32, width=122)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(font="TkDefaultFont")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Penerbit:''')
        self.TLabel1_1.configure(compound='left')

        self.TLabel1_1_1 = ttk.Label(self)
        self.TLabel1_1_1.place(relx=0.594, rely=0.375, height=32, width=122)
        self.TLabel1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1.configure(relief="flat")
        self.TLabel1_1_1.configure(anchor='w')
        self.TLabel1_1_1.configure(justify='left')
        self.TLabel1_1_1.configure(text='''Kategori:''')
        self.TLabel1_1_1.configure(compound='left')

        self.TLabel1_1_1_1 = ttk.Label(self)
        self.TLabel1_1_1_1.place(relx=0.594, rely=0.438, height=32, width=122)
        self.TLabel1_1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1.configure(relief="flat")
        self.TLabel1_1_1_1.configure(anchor='w')
        self.TLabel1_1_1_1.configure(justify='left')
        self.TLabel1_1_1_1.configure(text='''Bahasa:''')
        self.TLabel1_1_1_1.configure(compound='left')

        self.TLabel1_1_1_1_1 = ttk.Label(self)
        self.TLabel1_1_1_1_1.place(relx=0.594, rely=0.5, height=32, width=122)
        self.TLabel1_1_1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1_1.configure(relief="flat")
        self.TLabel1_1_1_1_1.configure(anchor='w')
        self.TLabel1_1_1_1_1.configure(justify='left')
        self.TLabel1_1_1_1_1.configure(text='''Harga:''')
        self.TLabel1_1_1_1_1.configure(compound='left')

        self.TLabel1_1_1_1_1_1 = ttk.Label(self)
        self.TLabel1_1_1_1_1_1.place(relx=0.594, rely=0.563, height=32, width=122)
        self.TLabel1_1_1_1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1_1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1_1_1.configure(relief="flat")
        self.TLabel1_1_1_1_1_1.configure(anchor='w')
        self.TLabel1_1_1_1_1_1.configure(justify='left')
        self.TLabel1_1_1_1_1_1.configure(text='''Stok:''')
        self.TLabel1_1_1_1_1_1.configure(compound='left')

        self.TLabel1_2 = ttk.Label(self)
        self.TLabel1_2.place(relx=0.69, rely=0.25, height=32, width=122)
        self.TLabel1_2.configure(background="#d9d9d9")
        self.TLabel1_2.configure(font="TkDefaultFont")
        self.TLabel1_2.configure(relief="flat")
        self.TLabel1_2.configure(anchor='w')
        self.TLabel1_2.configure(justify='left')
        self.TLabel1_2.configure(text=table_data["pengarang_buku"])
        self.TLabel1_2.configure(compound='left')

        self.TLabel1_2_1 = ttk.Label(self)
        self.TLabel1_2_1.place(relx=0.69, rely=0.313, height=32, width=122)
        self.TLabel1_2_1.configure(background="#d9d9d9")
        self.TLabel1_2_1.configure(font="TkDefaultFont")
        self.TLabel1_2_1.configure(relief="flat")
        self.TLabel1_2_1.configure(anchor='w')
        self.TLabel1_2_1.configure(justify='left')
        self.TLabel1_2_1.configure(text=table_data["penerbit_buku"])
        self.TLabel1_2_1.configure(compound='left')

        self.TLabel1_2_1_1 = ttk.Label(self)
        self.TLabel1_2_1_1.place(relx=0.69, rely=0.375, height=32, width=122)
        self.TLabel1_2_1_1.configure(background="#d9d9d9")
        self.TLabel1_2_1_1.configure(font="TkDefaultFont")
        self.TLabel1_2_1_1.configure(relief="flat")
        self.TLabel1_2_1_1.configure(anchor='w')
        self.TLabel1_2_1_1.configure(justify='left')
        self.TLabel1_2_1_1.configure(text=table_data["kategori_buku"])
        self.TLabel1_2_1_1.configure(compound='left')

        self.TLabel1_1_1_1_2 = ttk.Label(self)
        self.TLabel1_1_1_1_2.place(relx=0.69, rely=0.438, height=32, width=122)
        self.TLabel1_1_1_1_2.configure(background="#d9d9d9")
        self.TLabel1_1_1_1_2.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1_2.configure(relief="flat")
        self.TLabel1_1_1_1_2.configure(anchor='w')
        self.TLabel1_1_1_1_2.configure(justify='left')
        self.TLabel1_1_1_1_2.configure(text=table_data["bahasa_buku"])
        self.TLabel1_1_1_1_2.configure(compound='left')

        self.TLabel1_1_1_1_1_2 = ttk.Label(self)
        self.TLabel1_1_1_1_1_2.place(relx=0.69, rely=0.5, height=32, width=122)
        self.TLabel1_1_1_1_1_2.configure(background="#d9d9d9")
        self.TLabel1_1_1_1_1_2.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1_1_2.configure(relief="flat")
        self.TLabel1_1_1_1_1_2.configure(anchor='w')
        self.TLabel1_1_1_1_1_2.configure(justify='left')
        self.TLabel1_1_1_1_1_2.configure(text=table_data["harga_buku"])
        self.TLabel1_1_1_1_1_2.configure(compound='left')

        self.TLabel1_1_1_1_1_1_1 = ttk.Label(self)
        self.TLabel1_1_1_1_1_1_1.place(relx=0.69, rely=0.563, height=32, width=122)
        self.TLabel1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1_1_1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1_1_1_1.configure(relief="flat")
        self.TLabel1_1_1_1_1_1_1.configure(anchor='w')
        self.TLabel1_1_1_1_1_1_1.configure(justify='left')
        self.TLabel1_1_1_1_1_1_1.configure(text=table_data["stok_buku"])
        self.TLabel1_1_1_1_1_1_1.configure(compound='left')

        self.Spinbox1 = tk.Spinbox(self, from_=1.0, to=int(table_data["stok_buku"]))
        self.Spinbox1.place(relx=0.626, rely=0.65, relheight=0.03, relwidth=0.038)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.69, rely=0.638, height=47, width=89)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound='left')
        self.Button1.configure(text="Beli")


main()
