from __future__ import annotations
import tkinter as tk

from pages.data_buku import DataBukuPage
from pages.detail_buku import DetailBukuPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.order import OrderPage
from pages.payment import PaymentPage
from pages.register import RegisterPage
from utils import Apis


class CoreApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Pages
        self.page_list: tuple = ()

        # API
        self.apis: Apis = Apis()

        self.wm_frame()
        self.custom_state = {}

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def show(self, page_name):
        for F in self.page_list:
            if page_name == F.__name__:
                frame = F(parent=self.container, ctrl=self)
                frame.grid(row=0, column=0, sticky="nsew")
                frame.tkraise()
                return

    def set_s(self, state):
        self.custom_state.update(state)

    def get_s(self, field: str) -> dict | str | any:
        if not field:
            return {}
        return self.custom_state[field]

    def register_pages(self, pages: tuple):
        self.page_list = pages
        self.show("LoginPage")
        self.geometry("1550x800+0+0")


if __name__ == '__main__':
    app = CoreApp()
    app.register_pages((LoginPage, RegisterPage, HomePage, DataBukuPage, DetailBukuPage, PaymentPage, OrderPage))
    app.mainloop()
