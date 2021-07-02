from time import sleep
from selenium.webdriver.support.ui import Select


def test_ui_3(selenium):
    selenium.get('https://testsheepnz.github.io/random-number.html')
    selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Select(selenium.find_element_by_id("buildNumber")).select_by_index(1)
    selenium.find_element_by_id("rollDiceButton").click()
    sleep(1)
    selenium.find_element_by_id("numberGuess").send_keys("string")
    selenium.find_element_by_id("submitButton").click()
    out = selenium.find_element_by_id("feedbackLabel")
    selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    assert 'Not a number!' in out.text
    sleep(1)
    selenium.close()

