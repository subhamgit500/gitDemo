import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from util.browserUtil import browserCommonFunction


class ConfirmCheckout(browserCommonFunction):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout = (By.XPATH, "//button[@class='btn btn-success']")
        self.countryTextBox = (By.CSS_SELECTOR, "#country")
        self.purchase_btn = (By.CSS_SELECTOR, "input[type='submit']")
        self.dropDownSuggestions = (By.XPATH, "//div[@class='suggestions']")

    def purchase(self,countryName):
        self.driver.find_element(*self.checkout).click()  # main checkout
        self.driver.find_element(*self.countryTextBox).send_keys("Ind")  # enter country name

        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(self.dropDownSuggestions))  #here it takes locator, so unpacking is required, hence don't add *
        countries = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']")
        for country in countries:
            if country.find_element(By.XPATH, "ul/li/a").text == countryName:
                country.find_element(By.XPATH, "ul/li/a").click()
        print(f"{countryName} selected successfully")

        self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()  # checkbox
        self.driver.find_element(*self.purchase_btn).click()  # click purchase

        time.sleep(1)

        successMsg = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text  # get success message

        assert "Success" in successMsg
        print("Purchase completed successfully")
        print("Execution completed successfully")
