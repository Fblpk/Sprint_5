import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators

class TestUserRegistration:

    def test_registration(self, driver_and_main_page, random_email):
        driver = driver_and_main_page
        wait = WebDriverWait(driver, 10)

        # Открываем форму входа/регистрации
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()

        # Переход к регистрации
        wait.until(EC.element_to_be_clickable(AuthPageLocators.NO_ACCOUNT_BUTTON)).click()

        # Ввод данных
        login = random_email
        password = "12345678"
        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(login)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.SUBMIT_PASSWORD).send_keys(password)

        # Создание аккаунта
        driver.find_element(*AuthPageLocators.REGISTER_SUBMIT_BUTTON).click()

        # Проверка: avatar и имя пользователя отображаются
        avatar = wait.until(EC.visibility_of_element_located(AuthPageLocators.AVATAR_BUTTON))
        user_name = wait.until(EC.visibility_of_element_located(AuthPageLocators.USER_NAME_H3))

        # Ассерты
        assert avatar.is_displayed() == True, "Аватар пользователя не отображается"
        assert user_name.is_displayed() == True, "Имя пользователя не отображается"