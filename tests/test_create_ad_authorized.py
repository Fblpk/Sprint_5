from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from locators import MainPageLocators, AuthPageLocators, CreateAdPageLocators

class TestCreateAd:

    def test_create_ad(self, driver_and_main_page, random_ad_name, existing_user):
        driver = driver_and_main_page

        login = existing_user['login']
        password = existing_user['password']

        # Авторизация пользователя
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(login)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Страница создания объявления
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located(AuthPageLocators.AVATAR_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()
        publish_button = driver.find_element(*CreateAdPageLocators.PUBLISH_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", publish_button)

        # Ввод названия объявления
        driver.find_element(*CreateAdPageLocators.NAME_INPUT).send_keys(random_ad_name)

        # Выбор категории
        driver.find_element(*CreateAdPageLocators.CATEGORY_DROPDOWN_BUTTON).click()
        driver.find_element(*CreateAdPageLocators.CATEGORY_OPTION_TECH).click()

        # Выбор состояния товара
        driver.find_element(*CreateAdPageLocators.ITEM_STATUS_BUTTON).click()

        # Выбор города
        driver.find_element(*CreateAdPageLocators.CITY_DROPDOWN_BUTTON).click()
        driver.find_element(*CreateAdPageLocators.CITY_OPTION_SPB).click()

        # Ввод описания
        driver.find_element(*CreateAdPageLocators.DESCRIPTION_TEXTAREA).send_keys("Инженерное чудо без единого чипа!")

        # Ввод цены
        driver.find_element(*CreateAdPageLocators.PRICE_INPUT).send_keys("6999")

        # Публикация объявления
        driver.find_element(*CreateAdPageLocators.PUBLISH_BUTTON).click()


        # Проверка, что объявление отображается в профиле
        driver.execute_script("window.scrollTo(0, 0);")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(CreateAdPageLocators.RIGHT_ARROW_BUTTON))
        driver.find_element(*AuthPageLocators.AVATAR_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(CreateAdPageLocators.RIGHT_ARROW_BUTTON))
        right_arrow_button = driver.find_element(*CreateAdPageLocators.RIGHT_ARROW_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", right_arrow_button)

        # Локатор, соответствующий названию объявления
        ad_title_locator = (By.XPATH, f"//h2[contains(text(), '{random_ad_name}')]")
        ad_title_text = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(ad_title_locator)
        ).text

        assert ad_title_text == random_ad_name, "Название объявления не совпадает"