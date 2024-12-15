from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

locators = {
    "SCHEDULE_DEMO_BUTTON": (By.XPATH, "//input[@value='Schedule Demo']"),
    "ERROR_MESSAGE": (By.XPATH, "//label[text()='Please complete this required field.']"),
    "FIRST_NAME": (By.XPATH, "//input[@name='firstname']"),
    "LAST_NAME": (By.XPATH, "//input[@name='lastname']"),
    "EMAIL": (By.XPATH, "//input[@name='email']"),
    "PHONE": (By.XPATH, "//input[@name='phone']"),
    "JOB_ROLE": (By.XPATH, "//option[@value='{}']"),
    "INDUSTRY": (By.XPATH, "//option[@value='{}']"),
    "COMPANY_SIZE": (By.XPATH, "//option[@value='{}']"),
    "PERFORMANCE_MONITORING": (By.XPATH, "//option[@value='{}']"),
    "PERFORMANCE_MONITORING_NAME": (By.XPATH, "//input[@name='what_application_performance_monitoring_tool_are_you_using_']"),
    "TIMELINE": (By.XPATH, "//option[@value='{}']"),
    "NOTES": (By.XPATH, "//textarea[@name='note__is_there_anything_else_we_should_know__']"),
    "CHECKBOX": (By.XPATH, "//input[@name='LEGAL_CONSENT.subscription_type_1283425']")
}


class RequestDemoPageAS:

    def __init__(self, driver):
        self.driver = driver

    def click_on_schedule_demo(self):
        Schedule_Demo = self.driver.find_element(*locators["SCHEDULE_DEMO_BUTTON"])
        actions = ActionChains(self.driver)
        actions.move_to_element(Schedule_Demo).perform()
        Schedule_Demo.click()
        time.sleep(3)

    def validate_error_message(self):
        Error_Message = self.driver.find_elements(*locators["ERROR_MESSAGE"])
        if Error_Message:
            print("Enter input error message is diplayed for inpur fields : " + str(len(Error_Message)))
        else:
            assert False, "Enter input error message is not diplayed"

    def enter_details(self, readJson):
        First_name = self.driver.find_element(*locators["FIRST_NAME"])
        actions = ActionChains(self.driver)
        actions.move_to_element(First_name).perform()
        First_name.send_keys(readJson['First_Name'])
        self.driver.find_element(*locators["LAST_NAME"]).send_keys(readJson['Last_Name'])
        self.driver.find_element(*locators["EMAIL"]).send_keys(readJson['Email'])
        self.driver.find_element(*locators["PHONE"]).send_keys(readJson['Phone'])
        self.driver.find_element(locators["JOB_ROLE"][0], locators["JOB_ROLE"][1].format(readJson['Job_Role'])).click()
        self.driver.find_element(locators["INDUSTRY"][0], locators["INDUSTRY"][1].format(readJson['Industry'])).click()
        self.driver.find_element(locators["COMPANY_SIZE"][0], locators["COMPANY_SIZE"][1].format(readJson['Company_Size'])).click()
        self.driver.find_element(locators["PERFORMANCE_MONITORING"][0], locators["PERFORMANCE_MONITORING"][1].format(readJson['Performance_Monitoring'])).click()
        self.driver.find_element(*locators['PERFORMANCE_MONITORING_NAME']).send_keys(readJson['Performance_Monitoring_Name'])
        self.driver.find_element(locators["TIMELINE"][0], locators["TIMELINE"][1].format(readJson['Timeline'])).click()
        self.driver.find_element(*locators['NOTES']).send_keys(readJson['Notes'])
        print("Entered all details")
        time.sleep(5)

    def verify_checkbox_is_not_selected(self):
        Checkbox = self.driver.find_element(*locators["CHECKBOX"])
        actions = ActionChains(self.driver)
        actions.move_to_element(Checkbox).perform()
        Checkbox_status = Checkbox.is_selected()
        if Checkbox_status:
            assert False, "Checkbox is seleted by default"
        else:
            print("Checkbox is not selected by default")
        time.sleep(3)