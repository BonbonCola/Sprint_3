import locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    def test_registration_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.registration_link).click()
        driver.find_element(By.XPATH, locators.registration_name_input).send_keys("Auto test")
        driver.find_element(By.XPATH, locators.registration_email_input).send_keys("hellsdog@shurkou.com")
        driver.find_element(By.XPATH, locators.registration_password_input).send_keys("123456")
        driver.find_element(By.XPATH, locators.registration_button).click()
        # проверяем результат регистрации
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.entrance_button)))
        assert driver.find_element(By.XPATH, locators.entrance_button)
        driver.find_element(By.XPATH, locators.email_input).send_keys("hellsdog@shurkou.com")
        driver.find_element(By.XPATH, locators.password_input).send_keys("123456")
        driver.find_element(By.XPATH, locators.entrance_button).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.profile_label)))
        assert driver.find_element(By.XPATH, locators.profile_label)
        assert driver.find_element(By.XPATH, locators.history_label)
        assert driver.find_element(By.XPATH, locators.exit_button)
        driver.quit()

    def test_registration_invalid_password_unsuccessful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.registration_link).click()
        driver.find_element(By.XPATH, locators.registration_name_input).send_keys("Auto test")
        driver.find_element(By.XPATH, locators.registration_email_input).send_keys("someuser1793@greendike.com")
        driver.find_element(By.XPATH, locators.registration_password_input).send_keys("123")
        driver.find_element(By.XPATH, locators.registration_button).click()
        # проверяем результат регистрации
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.invalid_password_error_label)))
        assert driver.find_element(By.XPATH, locators.invalid_password_error_label)
        driver.quit()