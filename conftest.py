import pytest
from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options

@pytest.fixture(scope="session")
def browser():
<<<<<<< HEAD
    opts = Options()
    opts.set_headless()
    driver = Opera(executable_path='D:\web\operadriver.exe',options=opts)
=======
    driver = Opera(executable_path='D:\web\operadriver.exe')
>>>>>>> 5b366ea5db64ade3ad36f2ee01d827e445f1ddf4
    yield driver
    driver.quit()
