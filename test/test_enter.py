import locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestEntrance:
    # успешный вход cуществующим пользователем через кнопку Войти в аккаунт
    def test_click_entrance_to_account_button_user_exist_authorization_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.entrance_to_account_button)))  # ждем пока страница загрузится и кнопка входа будет видна
        driver.find_element(By.XPATH, locators.entrance_to_account_button).click()  # кликаем на кнопку Войти в аккаунт
        driver.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")  # вводим емейл
        driver.find_element(By.XPATH, locators.password_input).send_keys("123456")  # вводим пароль
        driver.find_element(By.XPATH, locators.entrance_button).click()  # жмем кнопку Войти
        # проверяем результат авторизации
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()

    # успешный вход cуществующим пользователем через кнопку Личный кабинет
    def test_click_account_button_user_exist_authorization_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))  # ждем пока страница загрузится и кнопка входа будет видна
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        driver.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")  # вводим емейл
        driver.find_element(By.XPATH, locators.password_input).send_keys("123456")  # вводим пароль
        driver.find_element(By.XPATH, locators.entrance_button).click()  # жмем кнопку Войти
        # проверяем результат авторизации
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()

    # успешный вход cуществующим пользователем на странице регистрации
    def test_entrance_in_registration_form_user_exist_authorization_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.registration_link).click()
        driver.find_element(By.XPATH, locators.entrance_link).click()
        driver.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")
        driver.find_element(By.XPATH, locators.password_input).send_keys("123456")
        driver.find_element(By.XPATH, locators.entrance_button).click()
        # проверяем результат авторизации
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.account_button).click()# кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()

    # успешный вход cуществующим пользователем на странице восстановления пароля
    def test_entrance_in_restore_form_user_exist_authorization_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.restore_password_link).click()
        driver.find_element(By.XPATH, locators.entrance_link).click()
        driver.find_element(By.XPATH, locators.email_input).send_keys("tacron@tqc-sheen.com")
        driver.find_element(By.XPATH, locators.password_input).send_keys("123")
        driver.find_element(By.XPATH, locators.entrance_button).click()
        # проверяем результат
        driver.find_element(By.XPATH, locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()