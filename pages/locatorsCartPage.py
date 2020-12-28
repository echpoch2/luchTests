from selenium.webdriver.common.by import By
class CartLocators():
    TOTAL_PRICE = (By.CLASS_NAME, "styled-price")
    CART_ITEMS = (By.CLASS_NAME, "td-price")
    ITEM_PRICE = (By.CLASS_NAME, "current_price")
