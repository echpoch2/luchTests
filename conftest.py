import pytest
from selenium.webdriver import Opera

@pytest.fixture(scope="session")
def browser():
    driver = Opera()
    yield driver
    driver.quit()