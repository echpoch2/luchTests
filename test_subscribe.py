from pages.item_page import ItemPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pytest_bdd import scenario, given, when, then, parsers
import pytest
from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options

@scenario("email.feature", "Subscribe with incorrect email")
def test_correct_subscribe():
    pass
@scenario("email.feature", "Subscribe with correct email")
def test_incorrect_subscribe():
    pass
@given(parsers.cfparse("I am on {page:S} page"))
def start_page(browser,page):
    page = MainPage(browser,page)
    page.open()
@when(parsers.cfparse("I type {email:S} to {field:w}"))
def type_keys_to_email(browser,email,field):
    page = MainPage(browser)
    page.type_to_field(email,field)
@when(parsers.cfparse("I press {btn:S}"))
def type_keys_to_email(browser,btn):
    page = MainPage(browser)
    page.click_on_button(btn)
@then(parsers.cfparse("I should see popup with {type:w} message"))
def check_type_of_popup(browser,type):
    print(11111)
    assert MainPage(browser).get_type_of_popup()==type

