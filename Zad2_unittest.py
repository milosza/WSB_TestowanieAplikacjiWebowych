import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WizzairComRegister(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    def test_register_by_email_on_wizzair_com(self):
        browser = self.browser
        browser.get("http://www.wizzair.com")
        browser.maximize_window()

        login = browser.find_element_by_xpath('//*/header/div[1]/div/div/button')
        #login.click()
        browser.execute_script("arguments[0].click();",login)

        registration = browser.find_element_by_xpath('//*/form/div/p/button')
        #registration.click()
        browser.execute_script("arguments[0].click();", registration)

        firstname = browser.find_element_by_name("firstName")
        firstname.send_keys("aaa")

        lastname = browser.find_element_by_xpath('//*/label[2]/div[1]/input')
        lastname.send_keys("aaa")

        gender = browser.find_element_by_xpath('//*/div[1]/label[2]/span')
        browser.execute_script("arguments[0].click();", gender)

        phone = browser.find_element_by_name("mobilePhone")
        phone.send_keys("111")

        email_niepoprawny = browser.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[1]/label/input')
        email_niepoprawny.send_keys("aaa@111")

        password = browser.find_element_by_xpath('//*[@id="regmodal-scroll-hook-5"]/div[1]/label/input')
        password.send_keys("aaa1111")

        checkbox = browser.find_element_by_xpath('//*/form/div[2]/div[10]/span/label[1]')
        browser.execute_script("arguments[0].click();", checkbox)

        register = browser.find_element_by_xpath('//*/form/div[2]/div[11]/button')
        browser.execute_script("arguments[0].click();", register)

        hidden_element = browser.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span/span')
        self.assertTrue("Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny", hidden_element.is_displayed())

if __name__ == "__main__": unittest.main()
