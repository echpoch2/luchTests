from selenium.webdriver.common.by import By


class MainPageLocators():
    EMAIL_INPUT = (By.CLASS_NAME, 'bx-form-control')
    SUBSCRIBE_BUTTON = (By.ID,'bx_subscribe_btn_sljzMT')
    POPUP_HEADER = (By.XPATH,'//*[@id="sender-subscribe-response-cont"]/div/div[1]')
