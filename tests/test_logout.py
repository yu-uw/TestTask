import allure
import pytest

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope='function')
def main_page(browser) -> MainPage:
    return MainPage(driver=browser)


@pytest.fixture(scope='function')
def auth_page(browser) -> AuthPage:
    return AuthPage(driver=browser)


@allure.epic("Авторизация")
@allure.feature("Выход из системы")
class TestLogout:

    @allure.title("Выход залогиненного пользователя")
    def test_successful_logout(self, browser: WebDriver, base_url: str, auth_page, main_page) -> None:
        """
        Тест проверяет успешный логаут из системы.

        Ожидаемый результат:
        - Отображается боковое меню с кнопкой логаута
        - После нажатия кнопки логаута отображается страница логина
        - При нажатии назад в браузере отображается ошибка доступа
        """

        auth_page.open(base_url)

        with allure.step("Вводим логин и пароль"):
            auth_page.username_input("standard_user")
            auth_page.password_input("secret_sauce")

        auth_page.login_button_click()

        main_page.logout_click()

        with allure.step("Проверить переход на страницу логина"):
            assert "inventory" not in main_page.url()
            assert "saucedemo.com" in main_page.url()

        with allure.step("Пытаемся вернуться на страницу назад (на главную)"):
            auth_page.go_back()

        with allure.step("Проверить текст ошибки"):
            expected_error = "Epic sadface: You can only access '/inventory.html' when you are logged in."
            assert auth_page.get_error_text() == expected_error, f"Ожидалась ошибка: {expected_error!r}"