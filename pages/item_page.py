from .base_page import BasePage
from selenium.webdriver.common.by import By

class ItemPage(BasePage):
    def add_item_to_cart(self):
        cart_button = self.browser.find_element(By.CLASS_NAME, 'button_add')
        cart_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

