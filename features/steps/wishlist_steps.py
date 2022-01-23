from behave import *
import time
from features.pageobjects.homepage import HomePage
from features.pageobjects.CartPage import CartPage
from features.pageobjects.wishlist import WishlistPage


@given(u'I add four different products to my wish list')
def step_impl(context):
    context.homePage = HomePage(context.driver)
    context.homePage.selectitemstowishlist(4)


@when(u'I view my wishlist table')
def step_impl(context):
    context.heart_btns = context.homePage.get_heart_btn()
    context.heart_btns[0].click()
    time.sleep(5)


@then(u'I find total four selected item in the wishlist')
def step_impl(context):
    context.wishlistPage = WishlistPage(context.driver)
    context.product_Count = context.wishlistPage.getProductsPriceOnWishlist()
    assert len(context.product_Count) == 4


@when(u'I search for the lowest price product')
def step_impl(context):
    context.wishlistPage.getaddCartPricesWithBtns()
    context.lowestPrice = context.wishlistPage.getLowestPriceOnWishList()
    print("Lowest price found on product:" + context.lowestPrice)


@when(u'I am able to add the lowest price item to my cart')
def step_impl(context):
    context.wishlistPage.addtoCartLowestPriceProductOnWishList()


@then(u'I am able to verify the item in my cart')
def step_impl(context):
    context.shopBtn = context.wishlistPage.getShopBtns()
    context.shopBtn[0].click()
    time.sleep(5)
    context.cartPage = CartPage(context.driver)
    context.productPriceOnCart = context.cartPage.getPriceOfProductOnCart()
    assert context.lowestPrice == context.productPriceOnCart

