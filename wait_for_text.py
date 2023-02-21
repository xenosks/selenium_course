from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    solve = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", solve)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    start_x = browser.find_element(By.ID, "input_value")
    x = int(start_x.text)
    total = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(total)

    solve.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()