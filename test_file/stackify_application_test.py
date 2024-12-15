import pytest
from pages.home_page import HomePageAS
from pages.login_page import LoginPageAS
from pages.ruby_page import RubyPageAS
from pages.request_demo_page import RequestDemoPageAS


@pytest.mark.usefixtures("browser_cbt")
class TestStackifyApplicationAS:

    def test_stackify_application_as(self, readJson):
        HomePage = HomePageAS(self.driver)
        LoginPage = LoginPageAS(self.driver)
        RubyPage = RubyPageAS(self.driver)
        Request_demo = RequestDemoPageAS(self.driver)
        HomePage.launch_application(readJson['stackify_url'])
        HomePage.validate_logo()
        HomePage.validate_url(readJson['stackify_url'])
        HomePage.validate_title(readJson['expected_title'])
        HomePage.verify_header_menu_options()
        HomePage.validate_content_under_solutions()
        HomePage.click_on_ruby()
        RubyPage.verify_retrace_content()
        RubyPage.verify_start_a_trial_and_request_demo()
        RubyPage.click_on_request_demo_button()
        Request_demo.click_on_schedule_demo()
        Request_demo.validate_error_message()
        Request_demo.enter_details(readJson)
        Request_demo.verify_checkbox_is_not_selected()
        HomePage.click_on_login()
        LoginPage.verify_login_page_header()
        #self.driver.close()