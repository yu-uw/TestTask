import allure
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from pages.auth_page import AuthPage
from pages.main_page import MainPage

@pytest.fixture(scope='function')
def auth_page(browser) -> AuthPage:
    return AuthPage(driver=browser)
@allure.epic("Авторизация")
@allure.feature("Успешный логин")
class TestAuthorization:
    @allure.title("Проверка входа с валидными данными")
    def test_successful_login(self, browser: WebDriver, base_url: str, auth_page) -> None:
        """
        Тест проверяет успешную авторизацию с корректными кредами.

        Ожидаемый результат:
        - Открыта страница с товарами
        - Отображается заголовок 'Products'.
        """

        auth_page.open(base_url)

        with allure.step("Вводим логин и пароль"):
            auth_page.username_input("standard_user")
            auth_page.password_input("secret_sauce")

        auth_page.login_button_click()

        main_page = MainPage(browser)

        with allure.step("Отображается страница товаров"):
            assert "inventory" in browser.current_url, "Не произошел переход на страницу товаров"
            assert main_page.get_products_title() == "Products", "Некорректный заголовок страницы"
