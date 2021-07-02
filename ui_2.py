# from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def ui_test_2():
    try:
        driver = webdriver.Firefox()
        # driver.maximize_window()  # раскомментить эту строку и
        driver.minimize_window()  # закомментить эту строку для браузера в полный экран
        driver.implicitly_wait(1)

        driver.get('https://testsheepnz.github.io/BasicCalculator.html')

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Select(driver.find_element_by_id("selectBuild")).select_by_index(0)
        Select(driver.find_element_by_id("selectOperationDropdown")).select_by_index(4)

        driver.find_element_by_id('number1Field').send_keys("gs")
        driver.find_element_by_id('number2Field').send_keys("bu")

        driver.find_element_by_id("calculateButton").click()

        # sleep(1)

        out = driver.find_element_by_id("numberAnswerField").get_attribute('value')

        assert out == "gsbu"

        driver.close()
        print('"gsbu" in output. Test 2 passed')
    except AssertionError:
        print('"gsbu" NOT in output. Test 2 failed')
