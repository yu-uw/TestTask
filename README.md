# Автотесты для сайта Saucedemo

Этот проект содержит автоматизированные тесты для проверки функционала аутентификации и авторизации на сайте [Saucedemo](https://www.saucedemo.com/).

## 📌 Стек технологий
- Python 3.10+
- Selenium WebDriver
- pytest (фреймворк для тестирования)
- Allure Framework (для генерации отчетов)

## 🚀 Установка и запуск

### Предварительные требования
1. Установите Python 3.10 или новее
### Установите и активируйте виртуальное окружение
```bash 
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
- Базовый запуск в локальном браузере Chrome (по умолчанию)
```bash
pytest tests/
```
- Запуск в локальном браузере Edge
```bash
pytest --browser=edge tests/
```
- Генерация Allure-отчета 
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Особенности реализации
- Использование паттерна Page Object Model для удобства поддержки
- Генерация детализированных Allure-отчетов со скриншотами шагов
- Проверка типов с помощью mypy в strict-режиме
- Форматирование кода с помощью ruff со строгими правилами

## Allure-отчет: 
![allure_report_main_page.PNG](docs%2Fimages%2Fallure_report_main_page.PNG)
![allure_report_test.PNG](docs%2Fimages%2Fallure_report_test.PNG)