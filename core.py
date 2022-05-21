from __future__ import annotations

import json
import tkinter as tk
from tkinter import messagebox

import urllib3

from models.order_status import OrderStatus


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


class Response:
    def __init__(self, is_error=False, error=None, result=None):
        self.__is_error = is_error
        self.__error = error
        self.__result = result

    def is_err(self) -> bool:
        if self.__is_error:
            messagebox.showerror("Error", self.__error)
        return self.__is_error

    def result(self) -> dict | list | any:
        if not self.__is_error and self.__result is None:
            return []

        return self.__result

    def error(self) -> str:
        return self.__error


class Apis:
    def __init__(self):
        # http client
        self.__client = urllib3.PoolManager()

    @staticmethod
    def __get_result(response) -> Response:
        response_json = json.loads(response.data.decode('utf-8'))
        try:
            if response_json["success"]:
                return Response(result=response_json["result"])
        except:
            return Response(is_error=True, error=response_json["error"])

    def get_user(self, userId: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/user/{userId}'))

    def get_book(self, bookId: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/book/{bookId}'))

    def get_all_books(self, limit: int = 50) -> Response:
        return self.__get_result(self.__client.request('GET', f"http://localhost:4000/book/all?limit={str(limit)}"))

    def req_login(self, username: str, password: str) -> Response:
        payload = json.dumps({"username": username, "password": password}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/login", body=payload))

    def req_register(self, username: str, name: str, password: str) -> Response:
        payload = json.dumps({"username": username, "name": name, "password": password}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/register", body=payload))

    def get_all_orders_by_userid(self, user_id: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/order/all/byuserid/{user_id}'))

    def get_all_orders(self) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/order/all/'))

    def get_order(self, order_id: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/order/{order_id}'))

    def do_order(self, user_id: str, book_id: str, qty: int) -> Response:
        payload = json.dumps({"user_id": user_id, "book_id": book_id, "qty": qty}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/order", body=payload))

    def set_order_status(self, order_id: str, order_status: str) -> Response:
        return self.__get_result(self.__client.request('PUT', f"http://localhost:4000/order/{order_id}/setstatus/{order_status}"))

    def get_payment_by_orderid(self, order_id: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/payment/byorderid/{order_id}'))

    def do_payment(self, user_id: str, order_id: str, receipt: str) -> Response:
        payload = json.dumps({"user_id": user_id, "order_id": order_id, "receipt": receipt}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/payment", body=payload))

    def add_book(self, name: str, author: str, publisher: str, category: str, language: str, description: str, price: int, qty: int,
                 image: str) -> Response:
        args = locals()
        add_payload: dict = {}
        for k, v in args.items():
            if v is not None and v != "" and k != 'self':
                add_payload.update({k: v})

        payload = json.dumps(add_payload).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/book", body=payload))

    def edit_book(self, id: str, name: None, author: None, publisher: None, category: None, language: None, description: None, price: None, qty: None,
                  image: None) -> Response:
        args = locals()
        update_payload: dict = {}
        for k, v in args.items():
            if v is not None and v != "" and k != 'self':
                update_payload.update({k: v})

        payload = json.dumps(update_payload).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/book/update", body=payload))
