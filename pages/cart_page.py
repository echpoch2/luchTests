from .base_page import BasePage
from .locatorsItemPage import ItemPageLocators
from .locatorsCartPage import CartLocators

class CartPage(BasePage):
    def get_items(self):
        return 1
    def should_be_items(self):
        assert float(self.browser.find_element(*CartLocators.TOTAL_PRICE).text[:-4]) > 0, "In the cart are'nt items"