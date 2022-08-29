import locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
   # проверяем успешную регистарцию
    def test_registration_successful(self, driver, user_email_password):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.registration_link).click()
        # поле ввода имени и емейла - одинаковые, я не нашла за что зацепиться для каждого поля отдельно не используя индексы элементов из dom((
        # возможно, в продакшене можно как то договориться с фронтами, чтобы такого не было. Но здесь это проект студента Практикума на курсе «React-разработчик».
        name_and_email = driver.find_elements(By.XPATH, locators.registration_name_input)
        name_and_email[0].send_keys("Auto test")
        name_and_email[1].send_keys(user_email_password[0])
        driver.find_element(By.XPATH, locators.registration_password_input).send_keys(user_email_password[1])
        driver.find_element(By.XPATH, locators.registration_button).click()
        # проверяем результат регистрации
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.entrance_button)))
        assert driver.find_element(By.XPATH, locators.entrance_button)
        driver.find_element(By.XPATH, locators.email_input).send_keys(user_email_password[0])
        driver.find_element(By.XPATH, locators.password_input).send_keys(user_email_password[1])
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

    # проверяем ошибку при некорректном пароле
    def test_registration_invalid_password_unsuccessful(self, driver, user_email_password):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_button)))
        driver.find_element(By.XPATH, locators.account_button).click()
        driver.find_element(By.XPATH, locators.registration_link).click()
        driver.find_element(By.XPATH, locators.registration_name_input).send_keys(user_email_password[0])
        driver.find_element(By.XPATH, locators.registration_email_input).send_keys(user_email_password[1])
        driver.find_element(By.XPATH, locators.registration_password_input).send_keys("123")
        driver.find_element(By.XPATH, locators.registration_button).click()
        # проверяем результат
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.invalid_password_error_label)))
        assert driver.find_element(By.XPATH, locators.invalid_password_error_label)
        driver.quit()
