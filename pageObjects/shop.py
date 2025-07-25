import time

from selenium.webdriver.common.by import By

from pageObjects.confirmCheckoutPage import ConfirmCheckout
from util.browserUtil import browserCommonFunction


#This shop.py purely follow POM - Page Object Model
class ShopPage(browserCommonFunction):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.productCard = (By.XPATH, "div/h4")
        self.addToCart_btn = (By.XPATH, "div/button")


    def add_to_cart(self,itemName):

        self.driver.find_element(*self.shop_link).click()

        products = self.driver.find_elements(*self.products)
        for product in products:
            if product.find_element(*self.productCard).text == itemName:  # item name
                product.find_element(*self.addToCart_btn).click()  # Add to cart button
        print(f"{itemName} added to cart.")


    def checkout(self):
        # Checkout
        self.driver.find_element(*self.checkout_btn).click()  # click Checkout
        time.sleep(1)
        purchase = ConfirmCheckout(self.driver)
        return purchase

