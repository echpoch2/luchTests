from selenium.common.exceptions import NoSuchElementException
from .locatorsItemPage import ItemPageLocators
from .locatorsCartPage import CartLocators
from .locatorsMainPage import MainPageLocators
class BasePage():
    def __init__(self, browser, url='None', timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def click_on_button(self,element):
        if(element=="SUBSCRIBE_BUTTON"):
            self.browser.find_element(*MainPageLocators.SUBSCRIBE_BUTTON).click()
        if(element=="DELETE_BUTTON"):
            elements = self.browser.find_elements(*CartLocators.DELETE_BUTTON)
            elements[0].click()
        if (element == "PROMO_BUTTON"):
            self.browser.find_element(*CartLocators.PROMO_BUTTON).click()
    def type_to_field(self,text,field):
        print(field,text)
        if(field=="EMAIL_INPUT"):
            self.browser.find_element(*MainPageLocators.EMAIL_INPUT).send_keys(text)
        if (field == "PROMO_INPUT"):
            self.browser.find_element(*CartLocators.PROMO_INPUT).send_keys(text)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True