import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_register(self, browser, link):
        start_link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(start_link)
        browser.implicitly_wait(15)

        signUp = browser.find_element(By.ID, "ember33")
        signUp.click()

        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("example@gmail.com")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("Example")
        button = browser.find_element(By.XPATH, "//button[contains(@class, 'sign-form')]")
        button.click()
        time.sleep(2)

        input3 = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@class, 'ember-text-area')]"))
        )
        input3.send_keys(str(math.log(int(time.time()))))

        button1 = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'submit-submission')]"))
        )
        button1.click()

        message = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'smart-hints')]"))
        )
        assert "Correct!" in message.text, "the answer is wrong"




