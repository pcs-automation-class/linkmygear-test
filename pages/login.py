from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
# from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.page_header = (By.XPATH, "//h5[text()='Login to Your Account']")
        self.email = (By.XPATH, "")

    def verify_page(self):
        super().verify_page(self.page_header)

    def type_email(self, email: str):
        # element = self.locate_element(self.email)
        # element.send_keys(email)
        self.locate_element(self.email).send_keys(email)

    def clean_email(self):
        element = self.locate_element(self.email)
        element.click()
        element.send_keys(Keys.COMMAND + 'a')
        element.send_keys(Keys.DELETE)

    def click_login(self):
        pass

    def click_forgot_password(self):
        pass

    def click_create_account(self):
        pass
