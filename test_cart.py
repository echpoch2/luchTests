from pages.item_page import ItemPage
from pages.cart_page import CartPage
from pytest_bdd import scenario, given, when, then, parsers
import pytest
from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options

@scenario("add_to_cart.feature", "Adding one item")
def test_add_to_cart_one_item():
    pass
@scenario("add_to_cart.feature", "Adding one more item")
def test_add_to_cart_two_item():
    pass
@scenario("add_to_cart.feature", "Check total cost")
def test_check_total_cost():
    pass

@given(parsers.cfparse("I am on {page:S} page"))
def start_page(browser,page):
    page = ItemPage(browser,page)
    page.open()
    return page

@when("I add item to cart")
def add_item(browser):
    ItemPage(browser).add_item_to_cart()

@then(parsers.cfparse("I should see {count:d} items in my cart"))
def should_have_item(browser,count):
    page = CartPage(browser, "https://luch.by/cart/")
    page.open()
    assert page.get_items_count()==count
@then("Sum of each item cost should be equals to total cost")
def check_total_cost(browser):
    assert CartPage(browser).calculate_total_cost() == CartPage(browser).get_total_cost()



