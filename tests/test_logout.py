import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from utils.screenshots import take_screenshot


@allure.epic("Авторизация")
@allure.feature("Выход из системы")
class TestLogout:
    """Тесты на выход из системы."""

    @allure.title("Выход залогиненного пользователя")
    def test_successful_logout(self, browser: WebDriver, base_url: str) -> None:
        """
        Тест проверяет успешный выход залогиненного пользователя

        Ожидаемый результат:
        - Открыта страница логина
        - При нажатии кнопки назад в браузере отображается ошибка.
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
            take_screenshot(browser, "Клик по кнопке логина")

        with allure.step("ОР:"):
            with allure.step("Мы на главной странице"):
                main_page = MainPage(browser)
                assert "inventory" in browser.current_url, "Не произошел переход на страницу товаров"
                assert main_page.get_products_title() == "Products", "Некорректный заголовок страницы"

        with allure.step("Кликаем по кнопке логаута"):
            main_page.logout_click()
            take_screenshot(browser, "Клик по кнопке логаута")

        with allure.step("ОР:"):
            with allure.step("Проверить переход на страницу логина"):
                assert "inventory" not in browser.current_url
                assert "saucedemo.com" in browser.current_url

        with allure.step("Пытаемся вернуться на страницу назад (на главную)"):
            browser.back()

        with allure.step("ОР:"):
            with allure.step("Проверить текст ошибки"):
                auth_page = AuthPage(browser)
                expected_error = "Epic sadface: You can only access '/inventory.html' when you are logged in."
                assert auth_page.get_error_text() == expected_error, f"Ожидалась ошибка: {expected_error!r}"
                take_screenshot(browser, "Отображается ошибка")
