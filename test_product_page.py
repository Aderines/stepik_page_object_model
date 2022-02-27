from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    product = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear')
    product.open()
    product.add_to_cart()
    product.solve_quiz_and_get_code()
    product.should_be_price_in_alert()
    product.should_be_product_name_in_alert()

