from .base_page import BasePage
from .locatorsItemPage import ItemPageLocators
from .locatorsMainPage import MainPageLocators
from .locatorsCartPage import CartLocators

class MainPage(BasePage):
    def get_type_of_popup(self):
        if(self.browser.find_element(*MainPageLocators.POPUP_HEADER).text=="Поздравляем!"):
            return "success"
        if (self.browser.find_element(*MainPageLocators.POPUP_HEADER).text == "Что-то пошло не так"):
            return "error"
