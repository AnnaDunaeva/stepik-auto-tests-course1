from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "100")
            )
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(y))
    btn = browser.find_element_by_id('solve')
    btn.click()
    alert=browser.switch_to_alert()
    print (alert.text)
finally:
    time.sleep(30)
    browser.quit()