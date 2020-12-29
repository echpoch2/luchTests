import pytest
from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options

@pytest.fixture(scope="session")
def browser():
    opts = Options()
    opts.headless = True
    assert opts.headless
    driver = Opera(executable_path='D:\web\operadriver.exe',options=opts)
    yield driver
    driver.quit()