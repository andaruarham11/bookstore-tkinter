class OrderStatus:
    @staticmethod
    def PAID() -> str:
        return "PAID"

    @staticmethod
    def CANCELLED() -> str:
        return "CANCELLED"

    @staticmethod
    def WAITING_FOR_PAYMENT() -> str:
        return "WAITING_FOR_PAYMENT"

    @staticmethod
    def DECLINED() -> str:
        return "DECLINED"

    @staticmethod
    def ON_SHIPPING() -> str:
        return "ON_SHIPPING"
