from __future__ import annotations

import tkinter as tk
from tkinter import constants as tk_const, messagebox

from utils import Response


class LoginPage(tk.Frame):
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl
        self.render()

    def render(self):
        self.ctrl.title("Login Page")

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
        register_btn = tk.Button(frame, command=lambda: self.ctrl.show("RegisterPage"), text="Register", font=("Calibri", 15), bd=3,
                                 relief=tk_const.RAISED, fg="white",
                                 bg="#008A31")
        register_btn.place(x=110, y=390, width=120, height=35)

    def do_login(self):
        id_admin = self.txtUser.get()
        password_admin = self.txtPass.get()

        if id_admin == "" or password_admin == "":
            messagebox.showerror("Error", "all field required")

        res: Response = self.ctrl.apis.req_login(id_admin, password_admin)
        if res.is_err():
            messagebox.showerror("Error", res.error())
            self.ctrl.show("LoginPage")
            return

        self.ctrl.set_s({"user_data": res.result()})
        self.ctrl.show("HomePage")
