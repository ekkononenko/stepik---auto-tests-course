import os
import time

from selenium import webdriver

link = " http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
browser.get(link)
try:
    elements = browser.find_elements_by_css_selector("input.form-control")
    for element in elements:
        element.send_keys("hello")
    # получаем путь к директории текущего исполняемого файл

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
