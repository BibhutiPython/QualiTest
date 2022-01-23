import time

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    wishlist_btn = (By.XPATH, "//span[contains(text(),'Add to wishlist')]")
    heart_btn = (By.XPATH, "//i[@class='lar la-heart']")

    def get_wishlist_buttons(self):
        return self.driver.find_elements(*HomePage.wishlist_btn)

    def selectitemstowishlist(self, numofproducts):
        wishlist_btns = self.get_wishlist_buttons()
        i = 1
        for wishlist in wishlist_btns:
            if i <= numofproducts:
                wishlist.click()
                time.sleep(5)
                i = i + 1
        time.sleep(5)

    def get_heart_btn(self):
        return self.driver.find_elements(*HomePage.heart_btn)
