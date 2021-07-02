from time import sleep
from selenium.webdriver.support.ui import Select


def test_ui_2(selenium):
    selenium.get('https://testsheepnz.github.io/BasicCalculator.html')
    selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Select(selenium.find_element_by_id("selectBuild")).select_by_index(0)
    Select(selenium.find_element_by_id("selectOperationDropdown")).select_by_index(4)
    selenium.find_element_by_id('number1Field').send_keys("gs")
    selenium.find_element_by_id('number2Field').send_keys("bu")
    selenium.find_element_by_id("calculateButton").click()
    out = selenium.find_element_by_id("numberAnswerField").get_attribute('value')
    assert out == "gsbu"
    # sleep(1)
    selenium.close()
