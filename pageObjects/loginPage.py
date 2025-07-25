import time

from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from util.browserUtil import browserCommonFunction


class LoginPage(browserCommonFunction):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.CSS_SELECTOR, "#username")
        self.password = (By.CSS_SELECTOR, "#password")
        self.signInButton = (By.CSS_SELECTOR, "#signInBtn")


    def login(self,username, passwd):

        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(passwd)
        self.driver.find_element(*self.signInButton).click()
        time.sleep(3)
        shop_page = ShopPage(self.driver)
        return shop_page
