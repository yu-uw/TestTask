import sys
from typing import Generator

import psutil
import pytest
from _pytest.config import Parser
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--browser",
        default="chrome",
        help="Браузер для тестов: chrome|edge",
        choices=("chrome", "edge"),  # Ограничиваем допустимые значения
    )


@pytest.fixture
def browser(request: FixtureRequest) -> Generator[webdriver.Chrome | webdriver.Edge, None, None]:
    browser_name = request.config.getoption("--browser").lower()
    driver: webdriver.Chrome | webdriver.Edge | None = None

    try:
        if browser_name == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--inprivate")  # Режим инкогнито
            options.add_argument("--user-data-dir=C:/temp/edge_profile")  # Новый профиль
            options.add_experimental_option("prefs", {
                "credentials_enable_service": False,  # Отключает сервис сохранения паролей
                "profile.password_manager_enabled": False  # Отключает встроенный менеджер паролей
            })
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        if not driver:
            pytest.exit(reason='driver is shit')
        driver.maximize_window()
        yield driver


    finally:
        if driver is not None:
            driver.quit()
            # Встроенная очистка для Edge (без отдельной функции)
            if browser_name == "edge" and sys.platform == "win32":
                for proc in psutil.process_iter(["name"]):
                    if proc.info["name"] == "msedge.exe":
                        proc.kill()

@pytest.fixture
def base_url() -> str:
    return "https://www.saucedemo.com"
