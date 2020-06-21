import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')

try:
    browser.get(link)
    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")
    num1 = int(x.text)
    num2 = int(y.text)
    num3 = str(num1 + num2)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(num3)
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
