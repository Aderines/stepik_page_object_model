from .base_page import BasePage
from selenium.webdriver.common.by import By


# Наследник класса BasePage. Класс-предок в Python указывается в скобках. класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
