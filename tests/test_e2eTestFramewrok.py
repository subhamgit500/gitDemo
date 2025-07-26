import json

import pytest


from pageObjects.loginPage import LoginPage

with open("C:\\PythonProject\\Projects\\testData\\testDataForShopping.json") as f:

    test_data = json.load(f)
    test_list = test_data["data"]

# @pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):

    driver = browserInstance

    loginPage = LoginPage(driver)  #Passing the driver object
    print(loginPage.getTitle())     #get the title of the webpage

    shop_page = loginPage.login(test_list_item["userEmail"],test_list_item["password"])
    shop_page.add_to_cart(test_list_item["ItemName"])
    print(shop_page.getTitle())

    purchase = shop_page.checkout()
    purchase.purchase(test_list_item["CountryName"])
    print((purchase.getTitle()))


#Comments added during in develop branch




