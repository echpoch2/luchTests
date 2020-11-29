from .base_page import BasePage
from .locators import ItemPageLocators

class CartPage(BasePage):
    def should_be_items(self):
        assert float(self.browser.find_element(*ItemPageLocators.TOTAL_PRICE).text[:-4]) > 0, "In the cart are'nt items"