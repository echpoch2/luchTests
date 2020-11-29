from selenium.webdriver.common.by import By


class ItemPageLocators():
    TOTAL_PRICE = (By.CLASS_NAME, "styled-price")
    CART_BUTTON = (By.CLASS_NAME, 'button_add')