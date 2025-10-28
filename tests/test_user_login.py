import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
from data import REGISTERED_USER, EXPECTED_URL

class TestLoginUser:

    def test_login_user(self, driver):
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()

        login = REGISTERED_USER['login']
        password = REGISTERED_USER['password']

        email_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))
        email_input.send_keys(login)

        password_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.PASSWORD_INPUT))
        password_input.send_keys(password)

        login_submit = wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_SUBMIT_BUTTON))
        login_submit.click()

        wait.until(EC.url_to_be(EXPECTED_URL))
        actual_url = driver.current_url
        assert actual_url == EXPECTED_URL, f"Конечная ссылка не соответствует ожидаемой: {actual_url}"

        avatar = wait.until(EC.visibility_of_element_located(AuthPageLocators.AVATAR_BUTTON))
        assert avatar.is_displayed() == True, "Аватар пользователя не отображается"

        user_name = wait.until(EC.visibility_of_element_located(AuthPageLocators.USER_NAME_H3))
        expected_user_name = "User."
        actual_user_name = user_name.text
        assert actual_user_name == expected_user_name, "Имя пользователя не соответствует ожидаемому"
