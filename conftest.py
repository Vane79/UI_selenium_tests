import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def selenium():
    driver = webdriver.Firefox()
    # driver.maximize_window()  # раскомментить эту строку и
    driver.minimize_window()  # закомментить эту строку для браузера в полный экран
    driver.implicitly_wait(2)
    return driver
