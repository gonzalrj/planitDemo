from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopPage(BasePage):
    __buy_btn_stuffed_frog = (By.XPATH, "//li[@id='product-2']//a[contains(text(), 'Buy')]")
    __price_stuffed_frog = (By.XPATH, "//li[@id='product-2']//span[@class='product-price ng-binding']")

    __buy_btn_fluffy_bunny = (By.XPATH, "//li[@id='product-4']//a[contains(text(), 'Buy')]")
    __price_fluffy_bunny = (By.XPATH, "//li[@id='product-4']//span[@class='product-price ng-binding']")

    __buy_btn_valentine_bear = (By.XPATH, "//li[@id='product-7']//a[contains(text(), 'Buy')]")
    __price_valentine_bear = (By.XPATH, "//li[@id='product-7']//span[@class='product-price ng-binding']")

    __cart_page_link = (By.XPATH, "//a[@href='#/cart']")

    def add_to_cart(self, product: str, quantity: int):
        if product == "stuffed frog":
            for i in range(quantity):
                super()._click(self.__buy_btn_stuffed_frog)
        elif product == "fluffy bunny":
            for i in range(quantity):
                super()._click(self.__buy_btn_fluffy_bunny)
        elif product == "valentine bear":
            for i in range(quantity):
                super()._click(self.__buy_btn_valentine_bear)
        else:
            raise TypeError("Selected invalid product.")

    def get_unit_price_as_float(self, product) -> float:
        if product == "stuffed frog":
            dollar_str = super()._find(self.__price_stuffed_frog).text
            amount_str = dollar_str.replace('$', '')
            amount_float = float(amount_str)
            return amount_float

        elif product == "fluffy bunny":
            dollar_str = super()._find(self.__price_fluffy_bunny).text
            amount_str = dollar_str.replace('$', '')
            amount_float = float(amount_str)
            return amount_float

        elif product == "valentine bear":
            dollar_str = super()._find(self.__price_valentine_bear).text
            amount_str = dollar_str.replace('$', '')
            amount_float = float(amount_str)
            return amount_float

        else:
            raise TypeError("Selected invalid product.")

    def goto_cart(self):
        super()._click(self.__cart_page_link)
