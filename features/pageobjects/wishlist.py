import time
from typing import Any

from selenium.webdriver.common.by import By


class WishlistPage:
    def __init__(self, driver):
        self.driver = driver

    productsSelPrices = (By.CSS_SELECTOR, "td[class='product-price']")
    shopBtns = (By.XPATH, "//i[@class='la la-shopping-bag']")
    addtocart: list[list[Any]] = []
    lownum = 0

    def getProductsPriceOnWishlist(self):
        return self.driver.find_elements(*WishlistPage.productsSelPrices)

    def getaddCartPricesWithBtns(self):
        tableObj = self.driver.find_element(By.CSS_SELECTOR, "table.shop_table")
        tabindex = 0
        for tabRow in tableObj.find_elements(By.CSS_SELECTOR, "tr"):
            for tabCell in tabRow.find_elements(By.CSS_SELECTOR, "td[class='product-price']"):
                tabpriceObjs = tabCell.find_elements(By.CSS_SELECTOR, "span bdi")
                if len(tabpriceObjs) == 1:
                    price = tabpriceObjs[0].text
                    price = price[1:]
                else:
                    price1 = tabpriceObjs[0].text
                    price1 = price1[1:]
                    price2 = tabpriceObjs[1].text
                    price2 = price2[1:]
                    if price1 < price2:
                        price = price1
                    else:
                        price = price2
                addCartBtn = tabRow.find_element(By.CSS_SELECTOR, "a[class*='add_to_cart']")
                templist = [price, addCartBtn]
                WishlistPage.addtocart.append(templist)
            tabindex = tabindex + 1
        return WishlistPage.addtocart

    def getLowestPriceOnWishList(self):
        WishlistPage.lownum = WishlistPage.addtocart[0][0]
        for pri in WishlistPage.addtocart:
            #    print(pri[0])
            if pri[0] <= WishlistPage.lownum:
                WishlistPage.lownum = pri[0]

        return WishlistPage.lownum

    def addtoCartLowestPriceProductOnWishList(self):
        for pri in WishlistPage.addtocart:
            if pri[0] == WishlistPage.lownum:
                pri[1].click()
                time.sleep(5)
                break

    def getShopBtns(self):
        return self.driver.find_elements(*WishlistPage.shopBtns)

