from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def sum(x, y):
        return str(x + y)

    start_x = browser.find_element(By.ID, "num1")
    x = int(start_x.text)
    start_y = browser.find_element(By.ID, "num2")
    y = int(start_y.text)
    total = sum(x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(total)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()