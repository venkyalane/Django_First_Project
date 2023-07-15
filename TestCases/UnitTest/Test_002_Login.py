import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class Login(unittest.TestCase):
    def setUp(self):
        driver.get("http://127.0.0.1:8000/home/")
    
    def test_002_login(self):
        #Navigate Login Button and click on it
        driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
        time.sleep(5)
        #Navigate username field and send username
        driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys('venky')
        time.sleep(5)
        #Navigate password field and send password
        driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys('admin')
        time.sleep(5)
        #Navigate login button and click on it
        driver.find_element(By.XPATH, "//body/div[@id='container']/div[@id='main']/div[@id='content-start']/div[@id='content']/div[@id='content-main']/form[@id='login-form']/div[3]/input[1]").click()
        time.sleep(5)

    def tearDown(self):
        driver.close()

if __name__ == '__main__':
    unittest.main()