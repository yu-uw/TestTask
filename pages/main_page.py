from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    """Локаторы для главной страницы."""

    PRODUCTS_TITLE = (By.XPATH, '//span[@class="title"]')
    MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_products_title(self) -> str:
        """Возвращает текст заголовка товаров."""
        return self.driver.find_element(*self.PRODUCTS_TITLE).text

    def open_menu(self) -> None:
        """Метод открытия бокового меню"""
        self.wait.until(ec.element_to_be_clickable(self.MENU_BUTTON)).click()

    def logout_click(self) -> None:
        """Метод выхода из учетной записи: открыть боковое меню, нажать кнопку logout."""
        self.open_menu()
        self.wait.until(ec.element_to_be_clickable(self.LOGOUT_LINK)).click()
