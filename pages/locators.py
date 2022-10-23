from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы."""
    SELECT_ALL_PRODUCTS = (By.CSS_SELECTOR, "li.dropdown-submenu")
    NUM_ALL_PRODUCTS = (By.CSS_SELECTOR, "div > form > strong:nth-child(2)")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".basket-mini a")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    LINK_PRODUCT = (By.CSS_SELECTOR, ".product_pod >h3 > a")
    MAX_PAGE = (By.CSS_SELECTOR, "ul.pager .current")
    BUTTON_NEXT_PAGE = (By.CSS_SELECTOR, "ul.pager li.next a")
    CARD_PRODUCT = (By.CSS_SELECTOR, "ol.row li")


class ProductPageLocators:
    """Локаторы для страницы товара."""
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, "[value='Добавить в корзину']")
    TITLE_PRODUCT = (By.CSS_SELECTOR, "h1")
    NOT_AVAILABLE_TO_ORDER = (By.CSS_SELECTOR, "p.outofstock.availability>i")


class BasketPageLocators:
    """Локаторы для страницы корзины."""
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TITLE_BASKET = (By.CSS_SELECTOR, "h1")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".basket-items h3 > a")
    VOLUME_PRODUCT = (By.CSS_SELECTOR, ".input-group > input")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".basket-items div:nth-child(4)")
    PRICE_WITHOUT_DISCOUNT = (By.CSS_SELECTOR, "tr:nth-child(2) > td.align-right")
    DISCOUNT = (By.CSS_SELECTOR, "tr:nth-child(3) > td.align-right")
    TOTAL_PRICE = (By.CSS_SELECTOR, "tr:nth-child(9) > td.align-right >h3")
