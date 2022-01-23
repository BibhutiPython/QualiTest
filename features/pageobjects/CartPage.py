from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    priceOnCart = (By.CSS_SELECTOR,"td[class='product-price'] span bdi")

    def getPriceOfProductOnCart(self):
        productPrice = self.driver.find_element(By.CSS_SELECTOR, "td[class='product-price'] span bdi").text
        return productPrice[1:]