from selenium.webdriver.common.by import By
class CartLocators():
    TOTAL_PRICE = (By.CLASS_NAME, "styled-price")
    CART_ITEMS = (By.TAG_NAME, "tbody")
