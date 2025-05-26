from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=5)

    def url(self) -> str:
        return self.driver.current_url

    def back(self):
        self.driver.back()
