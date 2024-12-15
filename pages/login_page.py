from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

locators = {
    "LOGIN_PAGE_HEADER": (By.XPATH, "//h2[@class='title']"),
    "LOGIN_PAGE_TEXT": (By.XPATH, '//div[text()="For SSO log in via your configured provider"]'),
    "USERNAME_INPUT": (By.XPATH, '//input[@id="txtUserName"]'),
    "PASSWORD_INPUT": (By.XPATH, '//input[@id="Password"]'),
    "LOST_PASSWORD": (By.XPATH, '//span[@id="lostPassword"]'),
    "REMEMBER_ME": (By.XPATH, '//input[@id="KeepMeLoggedIn"]'),
    "STACKIFY_SERVICES": (By.XPATH, '//a[@title="Stackify Service Status"]'),
    "LOGIN_BUTTON": (By.XPATH, '//input[@value="Log In"]'),
    "LOGIN_VIA_SOS_BUTTON": (By.XPATH, '//input[@value="Log In via SSO"]')
}


class LoginPageAS:

    def __init__(self, driver):
        self.driver = driver

    def verify_login_page_header(self):
        time.sleep(10)
        Login_header = self.driver.find_element(*locators["LOGIN_PAGE_HEADER"]).is_displayed()
        Login_text = self.driver.find_element(*locators["LOGIN_PAGE_TEXT"]).is_displayed()
        Username = self.driver.find_element(*locators["USERNAME_INPUT"]).is_displayed()
        Password = self.driver.find_element(*locators["PASSWORD_INPUT"]).is_displayed()
        Lost_Password = self.driver.find_element(*locators["LOST_PASSWORD"]).is_displayed()
        Remember_me = self.driver.find_element(*locators["REMEMBER_ME"]).is_displayed()
        Stackify_Services = self.driver.find_element(*locators["STACKIFY_SERVICES"]).is_displayed()
        Login_Button = self.driver.find_element(*locators["LOGIN_BUTTON"]).is_displayed()
        Login_via_sos = self.driver.find_element(*locators["LOGIN_VIA_SOS_BUTTON"]).is_displayed()
        Login_Elements = [Login_header, Login_text, Username, Password, Lost_Password, Remember_me, Stackify_Services, Login_Button, Login_via_sos]
        if all(Login_Elements):
            print("Login Elements are displayed as expected")
        else:
            assert False, "Login Elements are not displayed as expected"