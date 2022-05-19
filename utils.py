from __future__ import annotations

import json
from tkinter import messagebox

import urllib3


class Response:
    def __init__(self, is_error=False, error=None, result=None):
        self.__is_error = is_error
        self.__error = error
        self.__result = result

    def is_err(self) -> bool:
        return self.__is_error

    def result(self) -> dict | list | any:
        if not self.is_err() and self.__result is None:
            return []

        return self.__result

    def error(self) -> str:
        messagebox.showerror("Error", self.__error)
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

    def get_book(self, bookId: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/book/{bookId}'))

    def get_all_books(self) -> Response:
        return self.__get_result(self.__client.request('GET', "http://localhost:4000/book/all?limit=50"))

    def req_login(self, username: str, password: str) -> Response:
        payload = json.dumps({"username": username, "password": password}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/login", body=payload))

    def req_register(self, username: str, name: str, password: str) -> Response:
        payload = json.dumps({"username": username, "name": name, "password": password}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/register", body=payload))

    def get_all_orders_by_userid(self, user_id: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/order/all/byuserid/{user_id}'))

    def get_order(self, order_id: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/order/{order_id}'))

    def do_order(self, user_id: str, book_id: str, qty: int) -> Response:
        payload = json.dumps({"user_id": user_id, "book_id": book_id, "qty": qty}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/order", body=payload))

    def get_payment_by_orderid(self, order_id: str) -> Response:
        return self.__get_result(self.__client.request('GET', f'http://localhost:4000/payment/byorderid/{order_id}'))

    def do_payment(self, user_id: str, order_id: str, receipt: str) -> Response:
        payload = json.dumps({"user_id": user_id, "order_id": order_id, "receipt": receipt}).encode('utf-8')
        return self.__get_result(self.__client.request('POST', "http://localhost:4000/payment", body=payload))
