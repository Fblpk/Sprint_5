import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
from data import REGISTERED_USER

class TestLogoutUser:

    def test_logout_user(self, driver):
        wait = WebDriverWait(driver, 10)

        login = REGISTERED_USER['login']
        password = REGISTERED_USER['password']
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(login)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGIN_SUBMIT_BUTTON)).click()


        wait.until(EC.element_to_be_clickable(AuthPageLocators.LOGOUT_BUTTON)).click()


        wait.until(EC.invisibility_of_element_located(AuthPageLocators.AVATAR_BUTTON))
        wait.until(EC.invisibility_of_element_located(AuthPageLocators.USER_NAME_H3))


        actual_avatar_visible = bool(driver.find_elements(*AuthPageLocators.AVATAR_BUTTON))
        assert actual_avatar_visible == False, "Аватар пользователя все еще отображается после выхода"

        actual_username_visible = bool(driver.find_elements(*AuthPageLocators.USER_NAME_H3))
        assert actual_username_visible == False, "Имя пользователя все еще отображается после выхода"

        actual_login_button_visible = bool(driver.find_elements(*MainPageLocators.LOGIN_BUTTON))
        assert actual_login_button_visible == True, "Кнопка 'Вход и регистрация' не отображается после выхода"
