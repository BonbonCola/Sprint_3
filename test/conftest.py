import pytest
import generate

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# перед стартом каждого теста создаем новый экземпляр драйвера
@pytest.fixture
def driver():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # запустили драйвер
    d.get("https://stellarburgers.nomoreparties.site/")
    return d

# перед стартом каждого теста генерируем логин и пароль для тестового пользователя
@pytest.fixture
def user_email_password():
    return [generate.email(), generate.password()]