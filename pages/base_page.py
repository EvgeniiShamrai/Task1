import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """Базовый класс, где записываем базовые методы для всех страниц сайта"""

    def __init__(self, browser: webdriver.Chrome, link: str):
        self.browser = browser
        self.link = link

    def open_page(self, url=None):
        """Метод, который открывает страницу сайта"""
        if url is None:
            url = self.link
        self.browser.get(url)

    def clik_on_the_element(self, how, locator):
        """Метод, который производит нажатие на элемент сайта"""
        element = self.browser.find_element(how, locator)
        element.click()

    def is_element_present(self, how, locator):
        "Метод, который проверяет наличие элемента на странице"
        try:
            self.browser.find_element(how, locator)
        except NoSuchElementException:
            return False
        return True

    def count_products(self, lst):
        """Метод, который подсчитывает количество продуктов"""
        return len(lst)

    def change_the_sign(self, price):
        """Метод, который заменяет символ запятой, на точку, для приведения цены к вещественному числу"""
        return re.sub(",", ".", price)
