import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class Mysite(unittest.TestCase):
    def setUp(self):
        #Open chrome browser and navigate this URL's
        driver.get("http://127.0.0.1:8000/home/")

    def test_test001(self):
        #Navigate all members element
        all_members = driver.find_element(By.XPATH, "//a[contains(text(),'All members')]")
        time.sleep(5)
        # click on
        all_members.click()
        time.sleep(5)
        #Navigate Venky alane Name elemet and click on it
        venky_data = driver.find_element(By.XPATH, "//a[contains(text(),'Venky Alane')]")
        venky_data.click()
        time.sleep(5)

    def tearDown(self):
        #After test case end then browser close
        driver.close()

if __name__ == '__main__':
    unittest.main()