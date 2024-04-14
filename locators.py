from selenium.webdriver.common.by import By


class AuthLocator:
    water_counter = (By.XPATH, "//div[@class= 'desktop-impact-item-eeQO3'][4]")
    co2_counter = (By.XPATH, "//div[@class= 'desktop-impact-item-eeQO3'][2]")
    energy_counter = (By.XPATH, "//div[@class= 'desktop-impact-item-eeQO3'][6]")
    email = (By.XPATH, "//input[@data-marker='login-form/login/input']")
    password = (By.XPATH, '//input[@data-marker="login-form/password/input"]')
    entrance = (By.XPATH, '//button[@data-marker="login-form/submit"]')
    my_ads = (By.LINK_TEXT, "Мои объявления")