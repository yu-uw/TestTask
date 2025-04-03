import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from utils.screenshots import take_screenshot


@allure.epic("Авторизация")
@allure.feature("Успешный логин")
class TestAuthorization:
    """Тесты на авторизацию."""

    @allure.title("Проверка входа с валидными данными")
    def test_successful_login(self, browser: WebDriver, base_url: str) -> None:
        """
        Тест проверяет успешную авторизацию с корректными кредами.

        Ожидаемый результат:
        - Открыта страница с товарами
        - Отображается заголовок 'Products'.
        """
        auth_page = AuthPage(browser)
        auth_page.open(base_url)

        with allure.step("Вводим логин и пароль"):
            with allure.step("Вводим логин"):
                auth_page.username_input("standard_user")
                take_screenshot(browser, "Заполнен логин")

            with allure.step("Вводим пароль"):
                auth_page.password_input("secret_sauce")
                take_screenshot(browser, "Заполнен пароль")

        with allure.step("Кликаем по кнопке логина"):
            auth_page.login_button_click()
            take_screenshot(browser, "Успешный клик по кнопке логина")

        # Проверки
        main_page = MainPage(browser)
        with allure.step("ОР:"):
            with allure.step("Отображается страница товаров"):
                assert "inventory" in browser.current_url, "Не произошел переход на страницу товаров"
                assert main_page.get_products_title() == "Products", "Некорректный заголовок страницы"
