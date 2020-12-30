from selenium.webdriver.common.by import By


class MainPageLocators():

    EMAIL_INPUT = (By.CLASS_NAME, 'bx-form-control')
    SUBSCRIBE_BUTTON = (By.ID,'bx_subscribe_btn_sljzMT')
    POPUP_HEADER = (By.XPATH,'//*[@id="sender-subscribe-response-cont"]/div/div[1]')
    SEARCH_INPUT = (By.XPATH,'/html/body/div[3]/section[2]/div/div[1]/div/form/input[1]')
    SEARCH_BUTTON = (By.CLASS_NAME,"button-search")
    ERROR_LABEL = (By.CLASS_NAME, "errortext")
    NOTE_LABEL = (By.CLASS_NAME,"notetext")
    SEARCH_ITEM_RESULT = (By.CLASS_NAME, "w-item")
