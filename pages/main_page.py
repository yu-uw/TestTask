import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage

class MainPage(BasePage):
    """Локаторы для главной страницы."""

    PRODUCTS_TITLE = (By.XPATH, '//span[@class="title"]')
    MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)  # Вызываем конструктор BasePage

    def get_products_title(self) -> str:
        self.take_screenshot("Products_page")
        return self.driver.find_element(*self.PRODUCTS_TITLE).text

    def open_menu(self) -> None:
        with allure.step("Открытие бокового меню"):
            self.wait.until(ec.element_to_be_clickable(self.MENU_BUTTON)).click()
            self.take_screenshot("Menu")
    def logout_click(self) -> None:
        with allure.step("Выход из аккаунта"):
            self.open_menu()
            self.wait.until(ec.element_to_be_clickable(self.LOGOUT_LINK)).click()
            self.take_screenshot("Successful_logout")