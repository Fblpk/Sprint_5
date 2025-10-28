import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestCreateAdWithoutAuth:

    def test_create_ad_without_auth(self, driver_and_main_page):
        driver = driver_and_main_page
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)).click()

        heading = wait.until(
            EC.visibility_of_element_located(("xpath", "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")))
        expected_text = "Чтобы разместить объявление, авторизуйтесь"
        actual_text = heading.text
        assert actual_text == expected_text, "Текст уведомления не совпадает"