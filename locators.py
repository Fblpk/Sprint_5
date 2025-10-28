from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Вход и регистрация']")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")

class AuthPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD = (By.NAME, "submitPassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[normalize-space(text())="Создать аккаунт"]')
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    AVATAR_BUTTON = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME_H3 = (By.XPATH, "//h3[text()='User.']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    ERROR_SPAN = (By.XPATH, "//span[text()='Ошибка']")
    INPUT_ERROR_DIVS = (By.CLASS_NAME, "input_inputError__fLUP9")

class CreateAdPageLocators:
    NAME_INPUT = (By.NAME, "name")
    CATEGORY_DROPDOWN_BUTTON = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CITY_DROPDOWN_BUTTON = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CATEGORY_OPTION_AUTO = (By.XPATH, "//span[text()='Авто']")
    CATEGORY_OPTION_TECH = (By.XPATH, "//span[text()='Технологии']")
    CITY_OPTION_SPB = (By.XPATH, "//span[text()='Санкт-Петербург']")
    ITEM_STATUS_BUTTON = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    AD_TITLE_H2_TEMPLATE = "//h2[contains(text(), '{}')]"
    RIGHT_ARROW_BUTTON = (By.XPATH, "//button[@class='arrowButton arrowButton--right undefined']")