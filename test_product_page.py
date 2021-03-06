from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    product = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019')
    product.open()
    product.should_be_add_to_cart_button()
    product.add_to_cart()
    product.solve_quiz_and_get_code()
    product.extract_text_different_alerts()
    product.should_be_price_in_alert()
    product.should_be_product_name_in_alert()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_param(browser, link):
    product = ProductPage(browser, link)
    product.open()
    product.should_be_add_to_cart_button()
    product.add_to_cart()
    product.solve_quiz_and_get_code()
    product.extract_text_different_alerts()
    product.should_be_price_in_alert()
    product.should_be_product_name_in_alert()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product = ProductPage(browser,
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    product.open()
    product.should_be_add_to_cart_button()
    product.add_to_cart()
    product.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product = ProductPage(browser,
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    product.open()
    product.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    product = ProductPage(browser,
                          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    product.open()
    product.should_be_add_to_cart_button()
    product.add_to_cart()
    product.should_be_dissappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()

