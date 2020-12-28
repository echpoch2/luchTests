from .base_page import BasePage
from .locatorsItemPage import ItemPageLocators
from .locatorsMainPage import MainPageLocators
from .locatorsCartPage import CartLocators

class MainPage(BasePage):
    def type_to_field(self,text,field):
        print(field,text)
        if(field=="EMAIL_INPUT"):
            self.browser.find_element(*MainPageLocators.EMAIL_INPUT).send_keys(text)
    def click_on_button(self,element):
        if(element=="SUBSCRIBE_BUTTON"):
            self.browser.find_element(*MainPageLocators.SUBSCRIBE_BUTTON).click()
    def get_type_of_popup(self):
        if(self.browser.find_element(*MainPageLocators.POPUP_HEADER).text=="Поздравляем!"):
            return "success"
        if (self.browser.find_element(*MainPageLocators.POPUP_HEADER).text == "Что-то пошло не так"):
            return "error"
