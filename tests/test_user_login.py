import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators

class TestLoginUser:

    def test_login_user(self, driver_and_main_page, existing_user):
        driver = driver_and_main_page
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()

        login = existing_user['login']
        password = existing_user['password']

        email_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))
        email_input.send_keys(login)

        password_input = wait.until(EC.visibility_of_element_located(AuthPageLocators.PASSWORD_INPUT))
        password_input.send_keys(password)

        login_submit = wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_SUBMIT_BUTTON))
        login_submit.click()

        expected_url = "https://qa-desk.stand.praktikum-services.ru/login"
        wait.until(EC.url_to_be(expected_url))
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Конечная ссылка не соответствует ожидаемой: {actual_url}"

        avatar = wait.until(EC.visibility_of_element_located(AuthPageLocators.AVATAR_BUTTON))
        assert avatar.is_displayed() == True, "Аватар пользователя не отображается"

        user_name = wait.until(EC.visibility_of_element_located(AuthPageLocators.USER_NAME_H3))
        expected_user_name = "User."
        actual_user_name = user_name.text
        assert actual_user_name == expected_user_name, "Имя пользователя не соответствует ожидаемому"
