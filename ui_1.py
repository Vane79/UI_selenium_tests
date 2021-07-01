# from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def ui_test_1():
    try:
        driver = webdriver.Firefox()
        # driver.maximize_window()
        driver.minimize_window()
        driver.implicitly_wait(1)

        driver.get('https://testsheepnz.github.io/BasicCalculator.html')

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Select(driver.find_element_by_id("selectBuild")).select_by_index(0)
        Select(driver.find_element_by_id("selectOperationDropdown")).select_by_index(1)

        driver.find_element_by_id('number1Field').send_keys("2")
        driver.find_element_by_id('number2Field').send_keys("3")

        driver.find_element_by_id("calculateButton").click()

        # sleep(1)

        out = driver.find_element_by_id("numberAnswerField").get_attribute('value')

        assert out == "-1"

        driver.close()
        print('-1 in output. Test 1 passed')
    except AssertionError:
        print('-1 NOT in output. Test 1 failed')
