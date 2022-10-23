from pages.main_page import MainPage
from pages.basket_page import BasketPage


class TestSite:
    """Класс для группировки тестов."""

    def test_quantity_products(self, browser):
        """Тест проверяющий совпадение количества полученных продуктов с сайта, с количеством продуктов на сайте."""
        link = "https://selenium1py.pythonanywhere.com/ru/"
        page = MainPage(browser, link)
        page.quantity_products()

    def test_add_products_in_basket(self, browser):
        """Тест проверяющий, что в корзину добавлены три продукта с ценой меньше 10 £."""
        link = "https://selenium1py.pythonanywhere.com/ru/"
        page = MainPage(browser, link)
        page.add_products()

    def test_enter_basket_page(self, browser):
        """Тест проверяющий, что произошел переход на страницу корзины."""
        link = "https://selenium1py.pythonanywhere.com/ru/"
        basket_page = BasketPage(browser, link)
        basket_page.enter_basket_page()

    def test_comparison_name_volume_products_in_basket(self, browser):
        """Тест проверяющий, что названия и количество продуктов в корзине совпадают с названием и количеством
        продуктов которые добавляли в корзину."""
        link = "https://selenium1py.pythonanywhere.com/ru/"
        basket_page = BasketPage(browser, link)
        basket_page.comparison_name_and_volume_products_in_basket()

    def test_comparison_price_products_in_basket(self, browser):
        """Тест проверяющий, что цена каждой книги в корзине меньше 10 £ и итоговая цена отображается корректно с
        учетом скидки."""
        link = "https://selenium1py.pythonanywhere.com/ru/"
        basket_page = BasketPage(browser, link)
        basket_page.comparison_price_products_in_basket()
