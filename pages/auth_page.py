import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class AuthPage(BasePage):
    """Локаторы для страницы авторизации."""

    USERNAME_INPUT = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="login-button"]')
    ERROR_MESSAGE = (By.XPATH, '//h3[contains(text(), "Epic sadface: You can only access")]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)  # Вызываем конструктор BasePage

    def open(self, url: str) -> None:
        """Открывает страницу по указанному URL."""
        self.driver.get(url)
        self.take_screenshot("Open_login_page")

    def username_input(self, username: str) -> None:
        with allure.step("Вводим логин"):
            self.wait.until(ec.element_to_be_clickable(self.USERNAME_INPUT)).send_keys(username)
            self.take_screenshot("Enter_login")

    def password_input(self, password: str) -> None:
        with allure.step("Вводим пароль"):
            self.wait.until(ec.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)
            self.take_screenshot('Enter_password')

    def login_button_click(self) -> None:
        with allure.step("Кликаем по кнопке логина"):
            self.wait.until(ec.element_to_be_clickable(self.LOGIN_BUTTON)).click()
            self.take_screenshot('Enter_login_button_click')

    def get_error_text(self) -> str:
        """Возвращает текст ошибки авторизации."""
        return self.driver.find_element(*self.ERROR_MESSAGE).text
