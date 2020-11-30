import pytest
from selenium.webdriver import Opera

@pytest.fixture(scope="session")
def browser():
    driver = Opera(executable_path='D:\web\operadriver.exe')
    yield driver
    driver.quit()
