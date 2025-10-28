import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import MainPageLocators, AuthPageLocators, CreateAdPageLocators


@pytest.fixture
def driver_and_main_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def random_email():
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(letters, k=8)) + "@mail.ru"

@pytest.fixture
def random_ad_name():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=8))

@pytest.fixture
def existing_user():
    return {'login': 'moxifloxi@bk.ru',
                'password': '1287975'}
