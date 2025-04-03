import allure
from selenium.webdriver.remote.webdriver import WebDriver

def take_screenshot(driver: WebDriver, step_name:str) -> None: # noqa: ANN001,ANN201
    allure.attach(
        driver.get_screenshot_as_png(),
        name=f"Шаг: {step_name}",
        attachment_type=allure.attachment_type.PNG
    )
