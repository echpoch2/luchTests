from pages.item_page import ItemPage


def test_guest_can_go_to_login_page(browser):
    link = "https://luch.by/kollektsii/basic/78441380/"
    page = ItemPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_item_to_cart()
    page.should_be_login_link()