import pytest
from locators import AuthLocator


def test_1_water_counter_not_user(driver, base_page, screenshot_name):
    """EXP-1 Делаем скриншот счётчика воды без авторизации пользователя"""
    water_counter = driver.find_element(*AuthLocator.water_counter)
    assert water_counter.screenshot(screenshot_name)


def test_2_co2_counter_not_user(driver, base_page, screenshot_name):
    """EXP-2 Делаем скриншот счётчика CO2 без авторизации пользователя"""
    co2_counter = driver.find_element(*AuthLocator.co2_counter)
    assert co2_counter.screenshot(screenshot_name)


def test_3_energy_counter_not_user(driver, base_page, screenshot_name):
    """EXP-3 Делаем скриншот счётчика энергии без авторизации пользователя"""
    energy_counter = driver.find_element(*AuthLocator.energy_counter)
    assert energy_counter.screenshot(screenshot_name)


def test_4_water_counter_with_auth_user(driver, auth_by_valid_email_password, screenshot_name):
    """EXP-4 Делаем скриншот счётчика воды у авторизованного пользователя"""
    if type(auth_by_valid_email_password) == bool:
        print("\nТребуется авторизация пользователя!")
    else:
        water_counter = driver.find_element(*AuthLocator.water_counter)
        assert water_counter.screenshot(screenshot_name)


def test_5_co2_counter_with_auth_user(driver, auth_by_valid_email_password, screenshot_name):
    """EXP-5 Делаем скриншот счётчика CO2 у авторизованного пользователя"""
    if type(auth_by_valid_email_password) == bool:
        print("\nТребуется авторизация пользователя!")
    else:
        co2_counter = driver.find_element(*AuthLocator.water_counter)
        assert co2_counter.screenshot(screenshot_name)


def test_6_energy_counter_with_auth_user(driver, auth_by_valid_email_password, screenshot_name):
    """EXP-6 Делаем скриншот счётчика CO2 у авторизованного пользователя"""
    if type(auth_by_valid_email_password) == bool:
        print("\nТребуется авторизация пользователя!")
    else:
        energy_counter = driver.find_element(*AuthLocator.water_counter)
        assert energy_counter.screenshot(screenshot_name)

