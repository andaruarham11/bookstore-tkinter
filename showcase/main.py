from __future__ import annotations
import json
import tkinter as tk
from tkinter import constants as tk_const, messagebox, ttk, filedialog

from PIL import Image, ImageTk

import urllib3

import base64
import io


class CoreApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.wm_frame()
        self.custom_state = {}

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frame_list = (LoginPage, RegisterPage, MainPage, DataBukuPage, DetailBukuPage, PaymentPage, OrderPage)

        self.show_frame("LoginPage")
        self.geometry("1550x800+0+0")

    def show_frame(self, page_name):
        for F in self.frame_list:
            if page_name == F.__name__:
                frame = F(parent=self.container, controller=self)
                frame.grid(row=0, column=0, sticky="nsew")
                frame.tkraise()

    def set_window_title(self, title):
        self.title(title)

    def set_s(self, state):
        self.custom_state.update(state)

    def get_s(self, field: str) -> dict | str | any:
        if not field:
            return {}
        return self.custom_state[field]


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Main Page")

        lbl_title = tk.Label(self, text="Bookstore", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        # frame logo
        book_frame = tk.Frame(self, bg="#D1D1D1")
        book_frame.place(x=275, y=200, width=400, height=400)

        pay_frame = tk.Frame(self, bg="#D1D1D1")
        pay_frame.place(x=875, y=200, width=400, height=400)

        # frame logo
        book_img = Image.open("./books.png")
        resize_book_image = book_img.resize((150, 150))
        self.image_book = ImageTk.PhotoImage(resize_book_image)
        image_book_label = tk.Label(book_frame, image=self.image_book, bg="#D1D1D1")
        image_book_label.place(x=125, y=80)

        pay_img = Image.open("./pay.png")
        resize_pay_img = pay_img.resize((150, 150))
        self.image_pay = ImageTk.PhotoImage(resize_pay_img)
        image_pay_label = tk.Label(pay_frame, image=self.image_pay, bg="#D1D1D1")
        image_pay_label.place(x=125, y=80)

        # button
        book_btn = tk.Button(book_frame, command=lambda: self.controller.show_frame("DataBukuPage"), text="Catalog Buku",
                             font=("Calibri", 15), bd=3, fg="black")
        book_btn.place(x=125, y=290, width=150, height=50)

        order_btn = tk.Button(pay_frame, command=lambda: self.controller.show_frame("OrderPage"), text="Status Order", font=("Calibri", 15), bd=3,
                              fg="black")
        order_btn.place(x=100, y=290, width=200, height=50)

        # logout button
        logout_btn = tk.Button(self, command=lambda: self.controller.show_frame("LoginPage"), text="Logout",
                               font=("Calibri", 15), bd=3, fg="black")
        logout_btn.place(x=0, y=80, width=120, height=35)
        ########


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Login Page")

        # create frame and place
        frame = tk.Frame(self, bg="#D1D1D1")
        frame.place(x=610, y=170, width=340, height=450)

        # greet label
        lbl_greet = tk.Label(frame, text="Login", font=("Calibri", 20, "bold"), fg="black", bg="#D1D1D1")
        lbl_greet.place(x=130, y=60)

        labal_username = tk.Label(frame, text="Username:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        labal_username.place(x=40, y=140)

        self.txtUser = tk.Entry(frame, font=("Calibri", 13))
        self.txtUser.place(x=40, y=170, width=260)

        label_password = tk.Label(frame, text="Password:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_password.place(x=40, y=200)

        self.txtPass = tk.Entry(frame, font=("Calibri", 13), show='*')
        self.txtPass.place(x=40, y=230, width=260)

        # login button
        login_btn = tk.Button(frame, command=self.do_login, text="Login", font=("Calibri", 15), bd=3, relief=tk_const.RAISED, fg="white",
                              bg="#008A31")
        login_btn.place(x=110, y=350, width=120, height=35)
        register_btn = tk.Button(frame, command=lambda: self.controller.show_frame("RegisterPage"), text="Register", font=("Calibri", 15), bd=3,
                                 relief=tk_const.RAISED, fg="white",
                                 bg="#008A31")
        register_btn.place(x=110, y=390, width=120, height=35)

    def do_login(self):
        id_admin = self.txtUser.get()
        password_admin = self.txtPass.get()

        if id_admin == "" or password_admin == "":
            messagebox.showerror("Error", "all field required")

        data = {
            "username": id_admin,
            "password": password_admin,
        }

        payload = json.dumps(data).encode('utf-8')

        r = urllib3.PoolManager().request('POST', "http://localhost:4000/login", body=payload)
        res = json.loads(r.data.decode('utf-8'))

        try:
            if res["success"]:
                self.controller.show_frame("MainPage")
                self.controller.set_s({"user_data": res["result"]})

        except:
            messagebox.showerror("error", res["error"])


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.set_window_title("Register Page")

        # create frame and place
        frame = tk.Frame(self, bg="#D1D1D1")
        frame.place(x=610, y=170, width=340, height=450)

        # greet label
        lbl_greet = tk.Label(frame, text="Register", font=("Calibri", 20, "bold"), fg="black", bg="#D1D1D1")
        lbl_greet.place(x=105, y=60)

        label_username = tk.Label(frame, text="Username:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_username.place(x=40, y=140)

        self.txtUser = tk.Entry(frame, font=("Calibri", 13))
        self.txtUser.place(x=40, y=170, width=260)

        label_name = tk.Label(frame, text="Name:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_name.place(x=40, y=200)

        self.txtName = tk.Entry(frame, font=("Calibri", 13))
        self.txtName.place(x=40, y=230, width=260)

        label_password = tk.Label(frame, text="Password:", font=("Calibri", 15), fg="black", bg="#D1D1D1")
        label_password.place(x=40, y=260)

        self.txtPass = tk.Entry(frame, font=("Calibri", 13), show='*')
        self.txtPass.place(x=40, y=290, width=260)

        # register button
        login_btn = tk.Button(frame, command=self.do_register, text="Register", font=("Calibri", 15), bd=3,
                              relief=tk_const.RAISED, fg="white", bg="#008A31")
        login_btn.place(x=110, y=350, width=120, height=35)

        back_btn = tk.Button(frame, command=lambda: self.controller.show_frame("LoginPage"), text="Back", font=("Calibri", 15), bd=3,
                             relief=tk_const.RAISED, fg="black", bg="#d1d1d1")
        back_btn.place(x=110, y=390, width=120, height=35)

    def do_register(self):
        id_admin = self.txtUser.get()
        name_admin = self.txtName.get()
        password_admin = self.txtPass.get()

        if id_admin == "" or password_admin == "" or name_admin == "":
            messagebox.showerror("Error", "all field required")

        data = {
            "username": id_admin,
            "name": name_admin,
            "password": password_admin,
        }

        payload = json.dumps(data).encode('utf-8')

        r = urllib3.PoolManager().request('POST', "http://localhost:4000/register", body=payload)
        res = json.loads(r.data.decode('utf-8'))

        try:
            if res["success"]:
                self.controller.show_frame("MainPage")
        except:
            messagebox.showerror("error", res["error"])


class DataBukuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.my_tabel = None
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
        back_btn = tk.Button(self, command=lambda: self.controller.show_frame("MainPage"), text="Kembali",
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

        self.controller.set_s(state)
        self.controller.show_frame("DetailBukuPage")

    def get_books(self):
        http = urllib3.PoolManager()
        r = http.request('GET', "http://localhost:4000/book/all?limit=50")
        res = json.loads(r.data.decode('utf-8'))

        table_data = []
        if res["result"] is None:
            return []

        for d in res["result"]:
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


class OrderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.my_tabel = None
        self.controller = controller

        controller.set_window_title("Order Page")

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
        back_btn = tk.Button(self, command=lambda: self.controller.show_frame("MainPage"), text="Kembali",
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

        self.controller.set_s({"selected_order_id": table_data[0]})
        self.controller.show_frame("PaymentPage")

    def get_book(self, bookId: str):
        http = urllib3.PoolManager()
        r = http.request('GET', f'http://localhost:4000/book/{bookId}')
        res = json.loads(r.data.decode('utf-8'))["result"]

        table_data = {
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
        return table_data

    def get_orders_by_userid(self):
        user_id = self.controller.get_s("user_data")["id"]

        http = urllib3.PoolManager()
        r = http.request('GET', f'http://localhost:4000/order/all/byuserid/{user_id}')
        res = json.loads(r.data.decode('utf-8'))["result"]

        if res is None:
            return []

        orders_data = []
        for order in res:
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


class PaymentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        order_data = self.get_order()
        self.is_paid = False

        if order_data['status'] == 'PAID':
            self.is_paid = True
            self.payment = self.get_payment()

        self.render(order_data)

    def render(self, order_data: dict):
        self.controller.set_window_title("Payment Page")

        lbl_title = tk.Label(self, text="Pembayaran Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        back_btn = tk.Button(self, command=lambda: self.controller.show_frame("OrderPage"), text="Kembali", font=("Calibri", 15), bd=3, fg="black")
        back_btn.place(x=20, y=80, width=120, height=35)

        self.lbl_book_name = ttk.Label(self, foreground="#000000", anchor='w', justify='left', text="Nama Buku:", compound='left')
        self.lbl_book_name.place(relx=0.594, rely=0.25, height=32, width=122)

        self.lbl_qty = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text="Jumlah:", compound='left')
        self.lbl_qty.place(relx=0.594, rely=0.313, height=32, width=122)

        self.lbl_price = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text="Harga:")
        self.lbl_price.place(relx=0.594, rely=0.375, height=32, width=122)

        self.lbl_total_price = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text="Total Harga:", compound='left')
        self.lbl_total_price.place(relx=0.594, rely=0.438, height=32, width=122)

        self.lbl_status = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text="Status:", compound='left')
        self.lbl_status.place(relx=0.594, rely=0.5, height=32, width=122)

        self.data_book_name = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=order_data["book_name"], compound='left')
        self.data_book_name.place(relx=0.69, rely=0.25, height=32, width=122)

        self.data_qty = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=order_data["qty"], compound='left')
        self.data_qty.place(relx=0.69, rely=0.313, height=32, width=122)

        self.data_price = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=order_data["price"], compound='left')
        self.data_price.place(relx=0.69, rely=0.375, height=32, width=122)

        self.data_total_price = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=order_data["total_price"], compound='left')
        self.data_total_price.place(relx=0.69, rely=0.438, height=32, width=122)

        self.data_status = ttk.Label(self, background="#d9d9d9", anchor='w', justify='left', text=order_data["status"], compound='left')
        self.data_status.place(relx=0.69, rely=0.5, height=32, width=200)

        if not self.is_paid:
            self.btn_do_payment = tk.Button(self, command=lambda: self.do_payment(), activebackground="beige", borderwidth="2", compound='left',
                                            text="Bayar")
            self.btn_do_payment.place(relx=0.69, rely=0.638, height=47, width=89)

            my_font1 = ('times', 18, 'bold')
            l1 = tk.Label(self, text='Upload Receipt', width=30, font=my_font1)
            l1.place(relx=0, rely=0.25)
            b1 = tk.Button(self, text='Upload File', width=20, command=lambda: self.upload_file())
            b1.place(relx=0.3, rely=0.25)

        else:
            self.receipt_img = Image.open(io.BytesIO(base64.b64decode(self.payment["receipt"]))).resize((300, 450))
            self.receipt_img = ImageTk.PhotoImage(self.receipt_img)
            receipt_img_tk = tk.Label(self, image=self.receipt_img)
            receipt_img_tk.grid(row=3, column=1)
            receipt_img_tk.place(relx=0.1, rely=0.3)

    def upload_file(self):
        f_types = [['JPG or PNG Files', '*.jpg, *.png']]
        self.filename = filedialog.askopenfilename(filetypes=f_types)

        if not self.filename:
            return

        self.receipt_img = Image.open(self.filename).resize((300, 450))
        self.tkimg = ImageTk.PhotoImage(self.receipt_img)
        lbl_image = tk.Label(self, image=self.tkimg)  # using Button
        lbl_image.grid(row=3, column=1)
        lbl_image.place(relx=0.1, rely=0.3)

    def get_book(self, bookId: str):
        http = urllib3.PoolManager()
        r = http.request('GET', f'http://localhost:4000/book/{bookId}')
        res = json.loads(r.data.decode('utf-8'))["result"]

        table_data = {
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
        return table_data
        # 123

    def get_payment(self):
        selected_order_id = self.controller.get_s("selected_order_id")

        r = urllib3.PoolManager().request('GET', f'http://localhost:4000/payment/byorderid/{selected_order_id}')
        res = json.loads(r.data.decode('utf-8'))["result"]

        return res

    def get_order(self):
        selected_order_id = self.controller.get_s("selected_order_id")

        r = urllib3.PoolManager().request('GET', f'http://localhost:4000/order/{selected_order_id}')
        res = json.loads(r.data.decode('utf-8'))["result"]

        book = self.get_book(res["book_id"])
        order_data = {
            "id": res["id"],
            "book_name": book["nama_buku"],
            "order_time": res["order_time"],
            "qty": res["qty"],
            "price": book["harga_buku"],
            "total_price": res["total_price"],
            "status": res["status"]
        }

        return order_data

    def do_payment(self):
        if not self.receipt_img:
            messagebox.showerror("Error", "Upload Receipt!")
            return

        user_id = self.controller.get_s("user_data")["id"]
        order_id = self.controller.get_s("selected_order_id")

        buffered = io.BytesIO()
        self.receipt_img.save(buffered, format=self.filename.split('.', 1)[1])
        receipt_b64 = base64.b64encode(buffered.getvalue()).decode('ascii')

        if user_id == "" or order_id == "" or receipt_b64 == "":
            messagebox.showerror("Error", "all field required")

        data = {
            "user_id": user_id,
            "order_id": order_id,
            "receipt": receipt_b64,
        }

        payload = json.dumps(data).encode('utf-8')

        r = urllib3.PoolManager().request('POST', "http://localhost:4000/payment", body=payload)
        res = json.loads(r.data.decode('utf-8'))

        try:
            if res["success"]:
                self.controller.show_frame("OrderPage")
        except:
            messagebox.showerror("error", res["error"])


class DetailBukuPage(tk.Frame):
    def __init__(self, parent, controller):
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

        self.controller = controller

        state = self.controller.get_s("book_id")
        book_data = self.get_book(state)

        self.render(book_data)

    def render(self, book_data: dict):
        self.controller.set_window_title("Detail Buku Page")

        lbl_title = tk.Label(self, text="Detail Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        back_btn = tk.Button(self, command=lambda: self.controller.show_frame("DataBukuPage"), text="Kembali", font=("Calibri", 15), bd=3, fg="black")
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
        http = urllib3.PoolManager()
        r = http.request('GET', f'http://localhost:4000/book/{bookId}')
        res = json.loads(r.data.decode('utf-8'))["result"]

        table_data = {
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
        return table_data

    def order_book(self):
        book_id = self.controller.get_s("book_id")
        user_id = self.controller.get_s("user_data")["id"]
        qty = int(self.data_jumlah_beli.get())

        request_data = {
            "user_id": user_id,
            "book_id": book_id,
            "qty": qty
        }
        payload = json.dumps(request_data).encode('utf-8')

        r = urllib3.PoolManager().request('POST', "http://localhost:4000/order", body=payload)
        res = json.loads(r.data.decode('utf-8'))

        try:
            self.controller.set_s({"order_id": res["result"]["id"]})
            self.controller.show_frame("OrderPage")
        except:
            messagebox.showerror("Error", res["error"])


if __name__ == '__main__':
    app = CoreApp()
    app.mainloop()
