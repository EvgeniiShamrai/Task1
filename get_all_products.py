from selenium.common import NoSuchElementException

from pages.locators import MainPageLocators
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class AllProducts(BasePage):
    """Класс получения всех продуктов на сайте"""

    def get_all_products(self):
        """Метод получения всех прожуктов на сайте"""
        array_product = []  # Пустой массив для сохранения всех продуктов
        self.open_page()  # Метод, который открывает страницу сайта
        self.clik_on_the_element(
            *MainPageLocators.SELECT_ALL_PRODUCTS)  # Клик на каталог "Books" на левом меню, для получения всех товаров
        self.browser.find_element(By.TAG_NAME, "html").send_keys(
            Keys.END)  # Прокрутка главной страницы вниз для нажатия кнопки перехода на следующую страницу
        max_page = self.browser.find_element(*MainPageLocators.MAX_PAGE).text.split(" ")[
            -1]  # Получение значения последней страницы для дальнейшего перехода страниц
        for i in range(int(max_page)):  # Переход страниц
            products_page = self.browser.find_elements(
                *MainPageLocators.CARD_PRODUCT)  # Получение всех карточек товара на текущей странице
            for product in products_page:  # Перебор карточек для получения ссылок и цен товаров
                price = self.change_the_sign(
                    product.find_element(*MainPageLocators.PRICE_PRODUCT).text.strip(" £"))  # Получение цены товара
                link_product = product.find_element(*MainPageLocators.LINK_PRODUCT).get_attribute(
                    'href')  # Получение ссылки на товар
                array_product.append(
                    (price, link_product))  # Добавление цены и ссылки на товар в список всех товаров на сайте
            try:
                self.browser.find_element(
                    *MainPageLocators.BUTTON_NEXT_PAGE).click()  # Клик на кнопку "Вперед" для перехода на следующую
                # страницу
            except NoSuchElementException:  # Если кнопки нет на странице, то выходим их цикла перебора страниц
                break
        return array_product  # Возвращаем список всех товаров для дальнейших монипуляций

    # def select_min_price_product(self, array_products):
    #     return list(sorted(array_products, key=lambda x: float(x[0]))) Специально оставил метод, чтоб показать как можно было сортеровать товары


if __name__ == '__main__':
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Инициализация драйвера
    browser.implicitly_wait(2)  # Неявное ожидание 2 сек для поиска веб элементов
    pr = AllProducts(browser, 'https://selenium1py.pythonanywhere.com/ru/')  # Объявление экземпляра класса AllProducts
    all_products = pr.get_all_products()  # Получаем все товары на сайте
    # products_minimum_price = pr.select_min_price_product(all_products) Сортировка товаров
    browser.quit()  # Закрытие драйвера
