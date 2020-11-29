from pages.item_page import ItemPage
from pages.cart_page import CartPage

def test_ading_items_to_cart(browser):
    link = "https://luch.by/kollektsii/basic/78441380/"
    page = ItemPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_item_to_cart()

    link = "https://luch.by/cart"
    page = CartPage(browser,link)
    page.open()
    page.should_be_items()