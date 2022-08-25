import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# перед стартом каждого теста создаем новый экземпляр драйвера
@pytest.fixture
def driver():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # запустили драйвер
    d.get("https://stellarburgers.nomoreparties.site/")
    return d