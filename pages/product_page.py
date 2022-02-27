from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser,  url)
        self.alerts_list = None

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()

    # из-за того, что у алертов отсутствуют индивидуальные локаторы, вытаскиваю все, чтобы потом каждый проверить
    # по наименованию
    def extract_text_different_alerts(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ANY_ALERT_MESSAGE)
        # TODO понять, что за конструкция
        self.alerts_list = [x.text for x in alerts]

    # проверяем, есть ли среди алертов тот, который содержит название добавленного продукта
    def should_be_product_name_in_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        for x in range(len(self.alerts_list)):
            if product_name in self.alerts_list[x]:
                assert True

    def should_be_price_in_alert(self):
        self.extract_text_different_alerts()
        price = self.browser.find_element(*ProductPageLocators.PRICE_MAIN).text
        for x in range(len(self.alerts_list)):
            if price in self.alerts_list[x]:
                assert True
