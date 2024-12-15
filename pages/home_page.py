from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


locators = {
    "LOGO": (By.XPATH, "//a[@class='navbar-brand']"),
    "PRODUCT": (By.XPATH, "//a[contains(text(), 'Product')]"),
    "PRICING": (By.XPATH, "//a[contains(text(), 'Pricing')][1]"),
    "SOLUTIONS": (By.XPATH, "//a[contains(text(), 'Solutions')]"),
    "LEARN": (By.XPATH, "//a[contains(text(), 'Learn')]"),
    "LOGIN": (By.XPATH, "//a[contains(text(), 'Login')]"),
    "LANGUAGES_CONTENT": (By.XPATH, "//li[contains(@class, 'menu-item-has-children') and .//span[contains(text(), 'By Language')]]//ul[contains(@class, 'mega-menu__category-links')]//a[contains(text(), '{content}')]"),
    "RUBY": (By.XPATH, "//li[contains(@class, 'menu-item-has-children') and .//span[contains(text(), 'By Language')]]//ul[contains(@class, 'mega-menu__category-links')]//a[contains(text(), 'Ruby')]")
}


class HomePageAS:

    def __init__(self, driver):
        self.driver = driver

    def launch_application(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Stackify Application is launched Successfully")

    def validate_logo(self):
        Is_Logo_Displayed = self.driver.find_element(*locators["LOGO"]).is_displayed()
        if Is_Logo_Displayed:
            print("Logo Is Displayed In Application")
        else:
            assert False, "Logo Is Not Displayed In Application"

    def validate_url(self, url):
        current_url = self.driver.current_url
        print("Current Url launched : " + current_url)
        if url == current_url:
            print("Current Url Is As Expected")
        else:
            assert False, "Current Url Is Not As Expected"

    def validate_title(self, title):
        current_title = self.driver.title
        print("Current Url launched : " + current_title)
        if title == current_title:
            print("Current Title Is As Expected")
        else:
            assert False, "Current Title Is Not As Expected"

    def verify_header_menu_options(self):
        Product = self.driver.find_element(*locators["PRODUCT"]).is_displayed()
        Pricing = self.driver.find_element(*locators["PRICING"]).is_displayed()
        Solutions = self.driver.find_element(*locators["SOLUTIONS"]).is_displayed()
        Learn = self.driver.find_element(*locators["LEARN"]).is_displayed()
        Login = self.driver.find_element(*locators["LOGIN"]).is_displayed()
        Header_Menu_Items = [Product, Pricing, Solutions, Learn, Login]
        if all(Header_Menu_Items):
            print("All Header Menu Items Are Displayed As Expected")
        else:
            assert False, "Header Menu Items Are Not Displayed As Expected"

    def validate_content_under_solutions(self):
        actions = ActionChains(self.driver)
        Solutions = self.driver.find_element(*locators["SOLUTIONS"])
        actions.move_to_element(Solutions).perform()
        language_links_expected = [".NET", "Java", "PHP", "Node.js", "Ruby", "Python"]
        content_displayed = []
        for i in language_links_expected:
            print(i)
            by, value = locators["LANGUAGES_CONTENT"]
            format_value = value.format(content=i)
            print(format_value)
            element_found = self.driver.find_element(by, format_value).is_displayed()
            content_displayed.append(element_found)
        print(content_displayed)
        if all(content_displayed):
            print("All Contents Under Languages are Displayed As Expected")
        else:
            assert False, "Contents Under Languages are Not Displayed As Expected"

    def click_on_ruby(self):
        actions = ActionChains(self.driver)
        Solutions = self.driver.find_element(*locators["SOLUTIONS"])
        actions.move_to_element(Solutions).perform()
        self.driver.find_element(*locators["RUBY"]).click()
        time.sleep(5)
        current_url = self.driver.current_url
        print("Current Url launched : " + current_url)
        if "ruby" in current_url:
            print("Current Url Has Ruby Text As Expected")
        else:
            assert False, "Current Url Doesn't Have Ruby Text As Expected"

    def click_on_login(self):
        self.driver.find_element(*locators["LOGIN"]).click()
        time.sleep(5)


