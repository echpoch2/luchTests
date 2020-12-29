import time

from pages.item_page import ItemPage
from pages.cart_page import CartPage
from pytest_bdd import scenario, given, when, then, parsers


@scenario("cart.feature", "Adding one item")
def test_add_to_cart_one_item():
    pass
@scenario("cart.feature", "Adding one more item")
def test_add_to_cart_two_item():
    pass
@scenario("cart.feature", "Check total cost")
def test_check_total_cost():
    pass
@scenario("cart.feature", "Delete one item")
def test_delete_items():
    pass

@scenario("promo.feature", "Input incorrect promo")
def test_promo():
    pass
@given(parsers.cfparse("I am on {page:S} page"))
def start_page(browser,page):
    page = ItemPage(browser,page)
    page.open()
    return page
@when("I add item to cart")
def add_item(browser):
    ItemPage(browser).add_item_to_cart()
@when(parsers.cfparse("I press {btn:S} of first item"))
def type_keys_to_email(browser,btn):
    CartPage(browser).click_on_button(btn)
@when(parsers.cfparse("I type {text:S} to {field:w}"))
def type_keys_to_input(browser,text,field):
    page = CartPage(browser)
    page.type_to_field(text,field)
@when(parsers.cfparse("I press {btn:S}"))
def press_button(browser,btn):
    page = CartPage(browser)
    page.click_on_button(btn)
@then(parsers.cfparse("I should see {count:d} items in my cart"))
def should_have_item(browser,count):
    page = CartPage(browser, "https://luch.by/cart/")
    page.open()
    assert page.get_items_count()==count
@then("Sum of each item cost should be equals to total cost")
def check_total_cost(browser):
    assert CartPage(browser).calculate_total_cost() == CartPage(browser).get_total_cost()
@then("I should see label with error message")
def check_label(browser):
    assert CartPage(browser).get_label_message()=="incorrect"



