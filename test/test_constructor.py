import locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:
    def test_go_to_nachinki_bulki_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.burger_ing_list)))
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, locators.nachinki).click()
        assert driver.find_element(By.XPATH, locators.nachinki_header)
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, locators.bulki).click()
        assert driver.find_element(By.XPATH, locators.bulki_header)
        WebDriverWait(driver, 2)
        driver.quit()

    def test_go_to_soys_successful(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.burger_ing_list)))
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, locators.nachinki).click()
        assert driver.find_element(By.XPATH, locators.nachinki_header)
        WebDriverWait(driver, 2)
        driver.find_element(By.XPATH, locators.soys).click()
        assert driver.find_element(By.XPATH, locators.soys_header)
        WebDriverWait(driver, 2)
        driver.quit()