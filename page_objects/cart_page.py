from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    __unit_price_stuffed_frog = (By.XPATH, "//td[contains(text(), 'Stuffed Frog')]/following-sibling::td[1]")
    __subtotal_stuffed_frog = (By.XPATH, "//td[contains(text(), 'Stuffed Frog')]/following-sibling::td[3]")

    __unit_price_fluffy_bunny = (By.XPATH, "//td[contains(text(), 'Fluffy Bunny')]/following-sibling::td[1]")
    __subtotal_fluffy_bunny = (By.XPATH, "//td[contains(text(), 'Fluffy Bunny')]/following-sibling::td[3]")

    __unit_price_valentine_bear = (By.XPATH, "//td[contains(text(), 'Valentine Bear')]/following-sibling::td[1]")
    __subtotal_valentine_bear = (By.XPATH, "//td[contains(text(), 'Valentine Bear')]/following-sibling::td[3]")

    __total_price = (By.XPATH, "//strong[@class='total ng-binding']")

    def get_unit_price(self, product) -> float:
        if product == "stuffed frog":
            super()._wait_until_element_is_visible(self.__unit_price_stuffed_frog)
            price_str = super()._find(self.__unit_price_stuffed_frog).text
            return self.convert_price_to_float(price_str)

        elif product == "fluffy bunny":
            super()._wait_until_element_is_visible(self.__unit_price_fluffy_bunny)
            price_str = super()._find(self.__unit_price_fluffy_bunny).text
            return self.convert_price_to_float(price_str)

        elif product == "valentine bear":
            super()._wait_until_element_is_visible(self.__unit_price_valentine_bear)
            price_str = super()._find(self.__unit_price_valentine_bear).text
            return self.convert_price_to_float(price_str)

        else:
            raise TypeError("Invalid product selected.")

    @staticmethod
    def convert_price_to_float(raw_price: str) -> float:
        price_formatted = raw_price.replace("$", "")
        return float(price_formatted)

    @staticmethod
    def convert_total_price_to_float(raw_price: str) -> float:
        price_formatted = raw_price.replace("Total: ", "")
        return float(price_formatted)

    def get_unit_subtotal(self, product) -> float:
        if product == "stuffed frog":
            super()._wait_until_element_is_visible(self.__subtotal_stuffed_frog)
            price_str = super()._find(self.__subtotal_stuffed_frog).text
            return self.convert_price_to_float(price_str)

        elif product == "fluffy bunny":
            super()._wait_until_element_is_visible(self.__subtotal_fluffy_bunny)
            price_str = super()._find(self.__subtotal_fluffy_bunny).text
            return self.convert_price_to_float(price_str)

        elif product == "valentine bear":
            super()._wait_until_element_is_visible(self.__subtotal_valentine_bear)
            price_str = super()._find(self.__subtotal_valentine_bear).text
            return self.convert_price_to_float(price_str)

        else:
            raise TypeError("Invalid product selected.")

    def get_total_price(self) -> float:
        super()._wait_until_element_is_visible(self.__total_price)
        price_str = super()._find(self.__total_price).text
        return self.convert_total_price_to_float(price_str)
