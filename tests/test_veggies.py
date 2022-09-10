import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service
import time

@pytest.mark.usefixtures("drivers")
class first_Test:
    pass
class Test_veggie(first_Test):

    @pytest.mark.sanity
    def test_file1(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("be")
        time.sleep(4)
        time.sleep(3)
        a = self.driver.find_elements(By.XPATH, "//a[@class='increment']")
        for i in a:
            i.click()
        b = self.driver.find_elements(By.XPATH, "//button[contains(text(),'ADD TO CART')]")
        for j in b:
            j.click()
        self.driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED')]").click()
        c = self.driver.find_elements(By.XPATH, "//p[contains(text(),'e')]")
        print("the number of selected vegetables in a list is", len(c))
        for k in c:
            print(k.text)
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
        time.sleep(3)
        d = Select(self.driver.find_element(By.XPATH, "//select[@style='width: 200px;']"))
        d.select_by_value("India")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()

