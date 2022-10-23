from pages.main_page import MainPage
from pages.locators import MainPageLocators, BasketPageLocators


class BasketPage(MainPage):
    """Класс страницы корзины."""

    def enter_basket_page(self):
        """Метод перехода в корзину."""
        link = 'https://selenium1py.pythonanywhere.com/ru/'
        self.open_page(link)  # Переход на главную страницу
        self.clik_on_the_element(*MainPageLocators.BUTTON_BASKET)  # Переход в корзину
        assert "basket" in self.browser.current_url, "'Basket' is not in current url"  # Проверка что в урле есть "basket"
        assert self.is_element_present(
            *BasketPageLocators.TITLE_BASKET), "Title page is not presented"  # Проверка что веб элемент с название страницы присутствует
        title_page = self.browser.find_element(*BasketPageLocators.TITLE_BASKET).text
        assert "Корзина" == title_page, "Probably the name of the basket"  # Проверка, что название страницы 'Корзина'"

    def comparison_name_and_volume_products_in_basket(self):
        """Метод, который сравнивает количество и названия добавленных продуктов с количеством и названием продуктов
        в корзине. """
        names_products_in_main_page = sorted([name.lower().strip() for name in
                                              self.add_products()])  # Получение названий продуктов который добавили в корзину
        self.enter_basket_page()  # Переход в корзину
        names_products_in_basket = sorted(
            [name.text.lower().strip() for name in
             self.browser.find_elements(*BasketPageLocators.NAME_PRODUCT)])  # Получение названий продукта в корзине
        assert names_products_in_main_page == names_products_in_basket, "The name of the books does not match"  # Проверка названий
        number_products = [int(volume.get_attribute("value")) for volume in
                           self.browser.find_elements(
                               *BasketPageLocators.VOLUME_PRODUCT)]  # Получение количества продукта в корзине
        assert all(number_product == 1 for number_product in
                   number_products), "Each book is not in one copy"  # Проверка количества

    def comparison_price_products_in_basket(self):
        self.add_products()  # Добавление продуктов в корзину
        self.enter_basket_page()  # Переход в корзину
        price_products = [float(self.change_the_sign(price.text.strip(" £"))) for price in
                          self.browser.find_elements(
                              *BasketPageLocators.PRICE_PRODUCT)]  # Получение цены каждой книги в корзине
        assert all(price < 10.0 for price in
                   price_products), "The price of each book exceeds £ 10"  # Проверка, что цена каждой книги ниже 10 £
        price_without_discount = float(
            self.change_the_sign(self.browser.find_element(*BasketPageLocators.PRICE_WITHOUT_DISCOUNT).text.strip(
                " £")))  # Получение цены без скидки в корзине
        discount = float(
            self.change_the_sign(self.browser.find_element(*BasketPageLocators.DISCOUNT).text.strip(" £").strip(
                "-")))  # Получение значения скидки в корзине
        total_price = float(
            self.change_the_sign(self.browser.find_element(*BasketPageLocators.TOTAL_PRICE).text.strip(
                " £")))  # Получение цены с учетом скидки в корзине
        assert price_without_discount == total_price + discount, "The final price is not correct taking into account the discount"  # Проверка правильности расчета итоговой цены с учетом скидки
