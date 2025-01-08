class StockItem:
    stock_category = "Car accessories"  # Class variable

    def __init__(self, stock_code, quantity, price):
        self.__stock_code = stock_code  # Private instance variable
        self.__quantity = quantity
        self.__price = price
