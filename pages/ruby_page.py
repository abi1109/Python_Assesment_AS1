from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


locators = {
    "RETARCE_HEADER": (By.XPATH, "//h3[@class='section-title' and text()='How Retrace for Ruby on Rails Works']"),
    "TEXT": (By.XPATH, "(//p[contains(@class, 'elementor-heading-title')]//span[contains(text(), 'Retrace uses')])[1]"),
    "LOW_APPLICATION_OVERHEAD": (By.XPATH, "//li[contains(@class, 'elementor-icon-list-item') and span[contains(text(), 'Low application overhead')]]"),
    "PRODUCTION_USAGE": (By.XPATH, "//li[contains(@class, 'elementor-icon-list-item') and span[contains(text(), 'Safe for production usage')]]"),
    "SAAS_SOLUTION": (By.XPATH, "//li[contains(@class, 'elementor-icon-list-item') and span[contains(text(), 'SaaS based solution')]]"),
    "FOOTER_TEXT": (By.XPATH, "//em[contains(text(), 'Our monitoring agent is installed')]"),
    "FOOTER_HYPERLINK": (By.XPATH, "//em/a[contains(text(), 'review our docs')]"),
    "TEXT_BOLD": (By.XPATH, "//p[contains(@class, 'elementor-heading-title')]//b[contains(text(), 'lightweight profiling')]"),
    "START_A_TRIAL_BUTTON": (By.XPATH, "//div[@class='button-warpper']/a[contains(text(), 'Start Free Trial')]"),
    "REQUEST_A_DEMO": (By.XPATH, "//a[contains(@class, 'btn-outline-white') and contains(text(), 'Request a Demo')]")   
}


class RubyPageAS:

    def __init__(self, driver):
        self.driver = driver

    def verify_retrace_content(self):
        Header = self.driver.find_element(*locators["RETARCE_HEADER"])
        self.driver.execute_script("arguments[0].scrollIntoView();", Header)
        time.sleep(3)
        Retrace_uses = self.driver.find_element(*locators["TEXT"]).is_displayed()
        if Retrace_uses:
            Character_Bold = self.driver.find_element(*locators["TEXT_BOLD"]).is_displayed()
            if Character_Bold:
                print("'lightweight profiling' is in bold under text content retrace uses")
            else:
                assert False, "'lightweight profiling' is not in bold under text content retrace uses"
        Application_overhead = self.driver.find_element(*locators["LOW_APPLICATION_OVERHEAD"]).is_displayed()
        Production_usage = self.driver.find_element(*locators["PRODUCTION_USAGE"]).is_displayed()
        Saas_solution = self.driver.find_element(*locators["SAAS_SOLUTION"]).is_displayed()
        Footer_text = self.driver.find_element(*locators["FOOTER_TEXT"]).is_displayed()
        if Footer_text:
            Hyperlink = self.driver.find_element(*locators["FOOTER_HYPERLINK"]).is_displayed()
            if Hyperlink:
                print("'review our docs' is hyperlinked in footer text")
            else:
                assert False, "'review our docs' is hyperlinked in footer text"
        if all([Retrace_uses, Application_overhead, Production_usage, Saas_solution, Footer_text]):
            print("Retrace contents are displayed as expected in Ruby page")
        else:
            assert False, "Retrace contents are not displayed as expected in Ruby page"

    def verify_start_a_trial_and_request_demo(self):
        Start_trail = self.driver.find_element(*locators["START_A_TRIAL_BUTTON"])
        actions = ActionChains(self.driver)
        actions.move_to_element(Start_trail).perform()
        Request_demo_button = self.driver.find_element(*locators["REQUEST_A_DEMO"]).is_displayed()
        if Request_demo_button and Start_trail is not None:
            print("Start a train and request demo button is displayed at the bottom of the ruby page")
        else:
            assert False, "Start a train and request demo button is not displayed at the bottom of the ruby page"

    def click_on_request_demo_button(self):
        Request_demo = self.driver.find_element(*locators["REQUEST_A_DEMO"])
        Request_demo.click()
        print("Request a demo button is clicked")
        time.sleep(10)
