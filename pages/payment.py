from __future__ import annotations

import base64
import io
import tkinter as tk
from tkinter import constants as tk_const, ttk, filedialog, messagebox

from PIL import Image, ImageTk

from utils import Response


class PaymentPage(tk.Frame):
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl

        order_data = self.get_order()
        self.is_paid = False

        if order_data['status'] == 'PAID':
            self.is_paid = True
            self.payment = self.get_payment()

        self.render(order_data)

    def render(self, order_data: dict):
        self.ctrl.title("Payment Page")

        lbl_title = tk.Label(self, text="Pembayaran Buku", fg="black", font=("Calibri", 30, "bold"))
        lbl_title.grid(row=0, column=0, sticky=tk_const.W, columnspan=2, padx=10, pady=10)

        back_btn = tk.Button(self, command=lambda: self.ctrl.show("OrderPage"), text="Kembali", font=("Calibri", 15), bd=3, fg="black")
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
        res: Response = self.ctrl.apis.get_book(bookId)
        if res.is_err():
            return self.ctrl.show("HomePage")

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

    def get_payment(self):
        selected_order_id = self.ctrl.get_s("selected_order_id")

        res: Response = self.ctrl.apis.get_payment_by_orderid(selected_order_id)
        if res.is_err():
            return self.ctrl.show("HomePage")

        res: dict = res.result()
        return res

    def get_order(self):
        selected_order_id = self.ctrl.get_s("selected_order_id")

        res: Response = self.ctrl.apis.get_order(selected_order_id)
        if res.is_err():
            return self.ctrl.show("HomePage")

        res: dict = res.result()

        book = self.get_book(res["book_id"])
        return {
            "id": res["id"],
            "book_name": book["nama_buku"],
            "order_time": res["order_time"],
            "qty": res["qty"],
            "price": book["harga_buku"],
            "total_price": res["total_price"],
            "status": res["status"]
        }

    def do_payment(self):
        try:
            type(self.receipt_img)
        except:
            messagebox.showerror("Error", "Upload Receipt!")
            return

        user_id = self.ctrl.get_s("user_data")["id"]
        order_id = self.ctrl.get_s("selected_order_id")

        buffered = io.BytesIO()
        self.receipt_img.save(buffered, format=self.filename.split('.', 1)[1])
        receipt_b64 = base64.b64encode(buffered.getvalue()).decode('ascii')

        if user_id == "" or order_id == "" or receipt_b64 == "":
            messagebox.showerror("Error", "all field required")

        res: Response = self.ctrl.apis.do_payment(user_id, order_id, receipt_b64)
        if res.is_err():
            return

        self.ctrl.show("OrderPage")
