import time
import locators

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestEntrance:
    # перед стартом каждого теста создаем новый экземпляр драйвера
    @pytest.fixture
    def driver(self):
        d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # запустили драйвер
        d.get("https://stellarburgers.nomoreparties.site/")
        return d

    # успешный вход cуществующим пользователем через кнопку Войти в аккаунт
    def test_click_entrance_to_account_button_user_exist_authorization_successful(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.entrance_to_account_button)))  # ждем пока страница загрузится и кнопка входа будет видна
        driver.find_element(By.XPATH, locators.entrance_to_account_button).click()  # кликаем на кнопку Войти в аккаунт
        driver.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")  # вводим емейл
        driver.find_element(By.XPATH, locators.password_input).send_keys("123456")  # вводим пароль
        driver.find_element(By.XPATH, locators.entrance_button).click()  # жмем кнопку Войти
        # проверяем результат авторизации
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()

    # успешный вход cуществующим пользователем через кнопку Личный кабинет
    def test_click_account_button_user_exist_authorization_successful(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))  # ждем пока страница загрузится и кнопка входа будет видна
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        driver.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")  # вводим емейл
        driver.find_element(By.XPATH, locators.password_input).send_keys("123456")  # вводим пароль
        driver.find_element(By.XPATH, locators.entrance_button).click()  # жмем кнопку Войти
        # проверяем результат авторизации
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()
