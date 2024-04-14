import uuid
import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from settings import valid_password
from settings import valid_email
from locators import AuthLocator


chromedriver_autoinstaller.install()
base_url = "https://www.avito.ru/avito-care/eco-impact"


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def screenshot_name(request):
    return f"output\{request.function.__name__}_" + str(uuid.uuid4()) + ".png"


@pytest.fixture(autouse=False)
def base_page(driver):
    driver.implicitly_wait(20)
    return driver.get(base_url)


@pytest.fixture(autouse=False)
def auth_by_valid_email_password(driver, request):
    driver.implicitly_wait(20)
    driver.get(base_url + "#login?next=authCallbackEcoImpact")
    try:
        email = driver.find_element(*AuthLocator.email)
        email.clear()
        email.send_keys(valid_email)
        password = driver.find_element(*AuthLocator.password)
        password.clear()
        password.send_keys(valid_password)
        entrance = driver.find_element(*AuthLocator.entrance)
        entrance.submit()
        try:
            driver.find_element(*AuthLocator.my_ads)
            return driver.get(base_url)

        except NoSuchElementException:
            print('\nПопытка авторизации вызвала появление "капчи" или введены неверные email/пароль!')
            return driver.get_screenshot_as_file(f"output\capcha_{request.function.__name__}_" + str(uuid.uuid4()) + ".png")
    except TypeError:
        print('\nEmail и пароль не введены')
        return driver.get_screenshot_as_file(f"output\\not_auth_{request.function.__name__}_" + str(uuid.uuid4()) + ".png")