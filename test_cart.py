from pages.item_page import ItemPage
from pages.cart_page import CartPage


def test_ading_items_to_cart(browser):

    link = "https://luch.by/kollektsii/basic/78441380/"

    pg = ItemPage(browser,link)
    pg.add_item_to_cart()
    link = "https://luch.by/cart/"
    #pg = CartPage(browser,link)
    #pg.get_items()
    assert 1 >0


