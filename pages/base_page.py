import allure
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=5)

    def url(self) -> str:
        return self.driver.current_url

    def go_back(self) -> None:
        self.driver.back()
        self.take_screenshot("Go_back")

    def take_screenshot(self, name: str) -> None: # noqa: ANN001,ANN201
        """Делает скриншот и прикрепляет его к Allure-отчёту."""
        screenshot_path = f"screenshots/{name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)  # Создаём папку, если её нет
        self.driver.save_screenshot(screenshot_path)

        # Прикрепляем скриншот к Allure
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
