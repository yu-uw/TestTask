import allure
import pytest

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from utils.screenshots import take_screenshot
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope='function')
def main_page(browser) -> MainPage:
    return MainPage(driver=browser)


@pytest.fixture(scope='function')
def auth_page(browser) -> AuthPage:
    return AuthPage(driver=browser)


@pytest.fixture(scope="function")
def setup(browser: WebDriver, base_url: str, auth_page) -> None:
    auth_page.open(base_url)

    with allure.step("Вводим логин и пароль"):
        auth_page.username_input("standard_user")
        take_screenshot(browser, "Заполнен логин")

        auth_page.password_input("secret_sauce")
        take_screenshot(browser, "Заполнен пароль")

    auth_page.login_button_click()
    take_screenshot(browser, "Клик по кнопке логина")


@allure.epic("Авторизация")
@allure.feature("Выход из системы")
class TestLogout:

    @allure.title("Выход залогиненного пользователя")
    def test_successful_logout(self, setup, main_page, auth_page) -> None:
        main_page.logout_click()

        with allure.step("ОР:"):
            with allure.step("Проверить переход на страницу логина"):
                assert "inventory" not in main_page.url()
                assert "saucedemo.com" in main_page.url()

        with allure.step("Пытаемся вернуться на страницу назад (на главную)"):
            main_page.back()

        with allure.step("ОР:"):
            with allure.step("Проверить текст ошибки"):
                expected_error = "Epic sadface: You can only access '/inventory.html' when you are logged in."
                assert auth_page.get_error_text() == expected_error, f"Ожидалась ошибка: {expected_error!r}"
