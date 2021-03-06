from .base_page import BasePage
from .locatorsItemPage import ItemPageLocators
from .locatorsCartPage import CartLocators

class ItemPage(BasePage):
    def add_item_to_cart(self):
        cart_button = self.browser.find_element(*ItemPageLocators.CART_BUTTON)
        cart_button.click()

    def get_item_price(self):
        return self.browser.find_element(*CartLocators.TOTAL_PRICE)

    def should_be_login_link(self):
        assert self.is_element_present(*CartLocators.TOTAL_PRICE), "Login link is not presented"

