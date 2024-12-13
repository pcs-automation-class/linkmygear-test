from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
# from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger = logger
        self.page_header = (By.XPATH, "//h5[text()='Login to Your Account']")
        self.email = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[contains(text(), 'Login')]")
        self.forgot_password_link = (By.XPATH, "//a[text()='Forgot password?']")
        self.click_create_account = (By.XPATH, "//a[text()='Create an account']")

    def verify_page(self):
        self.locate_element(self.page_header)

    def type_email(self, email: str):
        self.locate_element(self.email).send_keys(email)

    def type_password(self, password: str):
        self.locate_element(self.password).send_keys(password)

    def clean_email(self):
        element = self.locate_element(self.email)
        element.click()
        element.send_keys(Keys.COMMAND + 'a')
        element.send_keys(Keys.DELETE)

    def click_login(self):
        self.click_element(self.login_button)

    def click_forgot_password(self):
        self.click_element(self.forgot_password_link)

    def click_create_account(self):
        pass


def login():
    return None