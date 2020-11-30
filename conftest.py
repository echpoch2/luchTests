import pytest
from selenium.webdriver import Opera

@pytest.fixture(scope="session")
def browser():
    driver = Opera('D:\web\operadriver.exe')
    yield driver
    driver.quit()
