from selenium.common import NoSuchElementException
from pages.locators import MainPageLocators, ProductPageLocators, BasketPageLocators
from get_all_products import AllProducts


class MainPage(AllProducts):
    """Класс главной страницы"""

    def quantity_products(self):
        """Метод сравнения полученных товаров с товарами на сайте """
        all_products = self.get_all_products()  # Получение всех товаров через метод
        num_products = self.browser.find_element(
            *MainPageLocators.NUM_ALL_PRODUCTS).text  # Получение числа товаров с главной страницы
        assert int(num_products) == len(
            all_products), "The number of products does not match"  # Проверка соответствия товаров

    def add_products(self):
        """Метод добавления продуктов в корзину"""
        all_product = self.get_all_products()  # Получение всех товаров через метод
        # products_low_price = self.select_min_price_product(all_product)
        name_books = []  # Массив для сохранения названий книг добавленных в корзину
        count_product_in_basket = 0  # Счетчик, который считает количество добавленных товаров в корзину
        for product in all_product:  # Перебор продуктов
            self.open_page(
                product[1])  # Переход на страницу продукта. В product[1] находится ссылка на карточку продукта
            price = self.change_the_sign(self.browser.find_element(*MainPageLocators.PRICE_PRODUCT).text.strip(
                " £"))  # Получение цены продукта с карточки продукта
            try:
                out_of_stock = self.browser.find_element(
                    *ProductPageLocators.NOT_AVAILABLE_TO_ORDER).text.strip()  # Получение статуса продукта (наличие) продукта
            except NoSuchElementException:
                out_of_stock = "Доступно"
            if float(price) < 10.0 and out_of_stock != "Недоступно":  # Отбор продуктов по цене и наличию
                name_books.append((self.browser.find_element(
                    *ProductPageLocators.TITLE_PRODUCT)).text)  # Добавление названия продуктов в массив
                self.clik_on_the_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)  # Добавление продукта в корзину
                count_product_in_basket += 1  # Увеличение счетчика подсчета добавленных продуктов в корзину
            if count_product_in_basket == 3:  # Выход из цикла при добавлении трех продуктов в корзину
                break
        self.clik_on_the_element(*MainPageLocators.BUTTON_BASKET)  # Переход с главной страницы в корзину
        items_in_basket = self.browser.find_elements(
            *BasketPageLocators.PRODUCT_IN_BASKET)  # Подсчет количества продуктов в корзине
        assert 3 == len(
            items_in_basket), "The number of products added to the basket does not match the number of products in the basket"  # Проверка того, что в корзину добавлены три продукта
        return name_books  # Возвращаем список названий товаров для дальнейших манипуляций
