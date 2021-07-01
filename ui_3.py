from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def ui_test_3():
    try:
        driver = webdriver.Firefox()
        # driver.maximize_window()
        driver.minimize_window()
        driver.implicitly_wait(1)

        driver.get('https://testsheepnz.github.io/random-number.html')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Select(driver.find_element_by_id("buildNumber")).select_by_index(1)

        driver.find_element_by_id("rollDiceButton").click()

        sleep(1)

        driver.find_element_by_id("numberGuess").send_keys("string")
        driver.find_element_by_id("submitButton").click()

        out = driver.find_element_by_id("feedbackLabel")

        assert 'Not a number!' in out.text

        # sleep(1)

        driver.close()
        print('"Not a Number" in output. Test 3 passed')
    except AssertionError:
        print('"Not a Number" NOT in output. Test 3 failed')
