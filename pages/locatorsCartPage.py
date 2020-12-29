from selenium.webdriver.common.by import By
class CartLocators():
    TOTAL_PRICE = (By.CLASS_NAME, "styled-price")
    CART_ITEMS = (By.CLASS_NAME, "td-price")
    ITEM_PRICE = (By.CLASS_NAME, "current_price")
    DELETE_BUTTON = (By.CLASS_NAME, "delete__link")
    PROMO_BUTTON = (By.XPATH, '//*[@id="coupons_block"]/div/a')
    PROMO_INPUT = (By.ID,"coupon")
    BAD_LABEL_MESSAGE = (By.CLASS_NAME, "bad")
