from __future__ import annotations
import imp

from core import CoreApp
from pages.admin_data_buku import AdminDataBukuPage
from pages.login import LoginPage
from pages.admin_home import AdminHomePage
from pages.cust_home import UserHomePage
from pages.cust_data_buku import DataBukuPage
from pages.cust_detail_buku import DetailBukuPage
from pages.cust_order import OrderPage
from pages.cust_payment import PaymentPage
from pages.cust_register import RegisterPage
from pages.admin_all_order import AllOrderPage
from pages.admin_detail_order import DetailOrder

if __name__ == '__main__':
    app = CoreApp()
    app.register_pages((LoginPage, RegisterPage, UserHomePage, DataBukuPage, DetailBukuPage, PaymentPage, OrderPage,
                        AdminHomePage, AdminDataBukuPage, AllOrderPage, DetailOrder))
    app.mainloop()
