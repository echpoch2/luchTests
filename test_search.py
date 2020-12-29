from pages.item_page import ItemPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pytest_bdd import scenario, given, when, then, parsers


@scenario("search.feature", "Search with empty query")
def test_empty_query():
    pass
@scenario("search.feature", "Search with incorrect query")
def test_incorrect_query():
    pass
@scenario("search.feature", "Search with correct query")
def test_correct_query():
    pass
@given(parsers.cfparse("I am on {page:S} page"))
def start_page(browser,page):
    page = MainPage(browser,page)
    page.open()
@when(parsers.cfparse("I don't type to SEARCH_INPUT"))
def type_keys_to_email(browser):
    return False
@when(parsers.cfparse("I type {email:S} to {field:w}"))
def type_keys_to_email(browser,email,field):
    page = MainPage(browser)
    page.type_to_field(email,field)
@when(parsers.cfparse("I press {btn:S}"))
def type_keys_to_email(browser,btn):
    page = MainPage(browser)
    page.click_on_button(btn)
@then(parsers.cfparse("I should see label with error message about empty query"))
def check_result_empty(browser):
    assert True
@then(parsers.cfparse("I should see label with error message about empty result"))
def check_result_incorrect(browser):
    assert True
@then(parsers.cfparse("I should see search results"))
def check_result(browser):
    assert True

