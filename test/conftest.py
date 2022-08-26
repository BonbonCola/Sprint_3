import pytest
import generate
import locators

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

@pytest.fixture
def driver_with_authorzed_user():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # запустили драйвер
    d.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(d, 20).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.entrance_to_account_button)))  # ждем пока страница загрузится и кнопка входа будет видна
    d.find_element(By.XPATH, locators.entrance_to_account_button).click()  # кликаем на кнопку Войти в аккаунт
    d.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")  # вводим емейл
    d.find_element(By.XPATH, locators.password_input).send_keys("123456")  # вводим пароль
    d.find_element(By.XPATH, locators.entrance_button).click()  # жмем кнопку Войти
    return d