import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='function')
def browser():
    """Фикстура, инициализация и управление драйвером для тестов"""
    print('\nstart browser...')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(1)
    yield browser
    print('\nquit browser...')
    browser.quit()