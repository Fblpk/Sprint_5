import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
from data import REGISTERED_USER

class TestUserRegistration:

    def test_registration_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()

        wait.until(EC.element_to_be_clickable(AuthPageLocators.NO_ACCOUNT_BUTTON)).click()


        login = REGISTERED_USER['login']
        password = REGISTERED_USER['password']
        email_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))
        email_input.send_keys(login)
        password_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.PASSWORD_INPUT))
        password_input.send_keys(password)
        confirm_password_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.SUBMIT_PASSWORD))
        confirm_password_input.send_keys(password)
        driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()


        expected_border_color = "rgb(255, 105, 114)"
        error_divs = wait.until(EC.presence_of_all_elements_located(AuthPageLocators.INPUT_ERROR_DIVS))
        for div in error_divs:
            actual_border_color = div.value_of_css_property("border-color")
            assert actual_border_color == expected_border_color, f"Рамка вокруг полей не подсвечена красным, {actual_border_color=}"

        error_span = wait.until(EC.visibility_of_element_located(AuthPageLocators.ERROR_SPAN))
        actual_text = error_span.text
        assert actual_text == "Ошибка", "Текст ошибки не совпадает"