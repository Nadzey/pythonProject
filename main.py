import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Открытие главной страницы Google
    driver.get("https://www.google.com/")
    yield driver
    # Закрытие браузера после выполнения всех тестов
    driver.quit()


def test_google_title(browser):
    # Проверка заголовка страницы
    assert browser.title == "Google"


def test_google_search_bar(browser):
    # Проверка наличия строки поиска на странице
    assert browser.find_element_by_name("q").is_displayed()


def test_google_search_button(browser):
    # Проверка наличия кнопки поиска на странице
    assert browser.find_element_by_name("btnK").is_displayed()
