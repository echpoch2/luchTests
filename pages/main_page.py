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
    def get_search_result(self):
        if (len(self.browser.find_elements(*MainPageLocators.ERROR_LABEL))>0):
            return "empty query"
        if(len(self.browser.find_elements(*MainPageLocators.NOTE_LABEL))>0):
            return "empty result"
        if (len(self.browser.find_elements(*MainPageLocators.SEARCH_ITEM_RESULT)) > 0):
            return "success search"
