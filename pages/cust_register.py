from __future__ import annotations

import tkinter as tk
from tkinter import constants as tk_const, messagebox

from core import CoreApp, Response


class RegisterPage(tk.Frame):
    def __init__(self, parent, ctrl: CoreApp):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl
        self.render()

    def render(self):
        self.ctrl.title("Register Page")

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

        back_btn = tk.Button(frame, command=lambda: self.ctrl.show("LoginPage"), text="Back", font=("Calibri", 15), bd=3,
                             relief=tk_const.RAISED, fg="black", bg="#d1d1d1")
        back_btn.place(x=110, y=390, width=120, height=35)

    def do_register(self):
        id_admin = self.txtUser.get()
        name_admin = self.txtName.get()
        password_admin = self.txtPass.get()

        if id_admin == "" or password_admin == "" or name_admin == "":
            return messagebox.showerror("Error", "all field required")

        res: Response = self.ctrl.apis.req_register(id_admin, name_admin, password_admin)

        if res.is_err():
            return

        self.ctrl.show("LoginPage")
