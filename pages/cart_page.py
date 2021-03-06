import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locatorsItemPage import ItemPageLocators
from .locatorsCartPage import CartLocators

class CartPage(BasePage):
    def get_items(self):
        return self.browser.find_elements(*CartLocators.CART_ITEMS)
    def calculate_total_cost(self):
        prices=self.browser.find_elements(*CartLocators.ITEM_PRICE)
        total=0
        for price in prices:
            total+=float(price.text[:-4])
        return total
    def get_total_cost(self):
        price =self.browser.find_element(*CartLocators.TOTAL_PRICE)
        return float(price.text[:-4])
    def get_label_message(self):
        if(len(self.browser.find_elements(*CartLocators.BAD_LABEL_MESSAGE))>0):
            return "incorrect"
        else:
            return "correct"

    def get_items_count(self):
        return len(self.get_items())
    def should_be_items(self):
        assert float(self.browser.find_element(*CartLocators.TOTAL_PRICE).text[:-4]) > 0, "In the cart are'nt items"