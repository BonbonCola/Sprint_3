import locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAccount:
    # проверяем переход в личный кабинет
    def test_go_to_account_successful(self, driver_with_authorzed_user):
        # проверяем результат перехода
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver_with_authorzed_user.find_element(By.XPATH,
                                                locators.account_button).click()
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver_with_authorzed_user.find_element(By.XPATH, locators.profile_label)
        assert driver_with_authorzed_user.find_element(By.XPATH, locators.history_label)
        assert driver_with_authorzed_user.find_element(By.XPATH, locators.exit_button)
        driver_with_authorzed_user.quit()

    # проверяем gереход из личного кабинета в конструктор
    def test_go_to_constructor_header_link_successful(self, driver_with_authorzed_user):
        # проверяем результат перехода
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.constructor_link)))
        driver_with_authorzed_user.find_element(By.XPATH,
                                                locators.constructor_link).click()
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.burger_ing_list)))
        assert driver_with_authorzed_user.find_element(By.XPATH, locators.burger_ing_list)
        driver_with_authorzed_user.quit()

    # проверяем переход из личного кабинета в конструктор по тапу на логотип
    def test_go_to_constructor_logo_successful(self, driver_with_authorzed_user):
        # проверяем результат перехода
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.logo)))
        driver_with_authorzed_user.find_element(By.XPATH, locators.logo).click()
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.burger_ing_list)))
        assert driver_with_authorzed_user.find_element(By.XPATH, locators.burger_ing_list)
        driver_with_authorzed_user.quit()

    # проверяем выход из личного кабинета
    def test_exit_successful(self, driver_with_authorzed_user):
        # проверяем результат перехода
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver_with_authorzed_user.find_element(By.XPATH,
                                                locators.account_button).click()  # кликаем на кнопку Личный кабинет
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.exit_button)))
        driver_with_authorzed_user.find_element(By.XPATH, locators.exit_button).click()
        WebDriverWait(driver_with_authorzed_user, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.entrance_button)))
        assert driver_with_authorzed_user.find_element(By.XPATH, locators.entrance_button)
        driver_with_authorzed_user.quit()
