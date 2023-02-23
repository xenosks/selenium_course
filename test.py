from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class test_class_name(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        elem1 = self.browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
        elem1.send_keys("Ivan")
        elem2 = self.browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
        elem2.send_keys("Petrov")
        elem3 = self.browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
        elem3.send_keys("ivan@gmail.com")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        congratulation = self.browser.find_element(By.CSS_SELECTOR, "h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!',
                         "button_click_error")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        elem1 = self.browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
        elem1.send_keys("Ivan")
        elem2 = self.browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
        elem2.send_keys("Petrov")
        elem3 = self.browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
        elem3.send_keys("ivan@gmail.com")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        congratulation = self.browser.find_element(By.CSS_SELECTOR, "h1")
        self.assertEqual(congratulation.text, 'Congratulations! You have successfully registered!',
                         "button_click_error")
if __name__ == "__main__":
    unittest.main()

