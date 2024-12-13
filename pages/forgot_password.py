from selenium.webdriver.common.by import By
from pages.base import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger = logger
        self.link_my_gear_logo = (By.XPATH, "//a[@class='logo']")
        self.page_header = (By.XPATH, "//h5[text()='Restore Password']")
        self.enter_email_header = (By.XPATH, "//p[text()='Please enter your email']")
        self.your_email = (By.XPATH, "//input[@type='text']")
        self.send = (By.XPATH, "//button[contains(@class, 'btn-primary') and contains(@class, 'w-100')]")
        self.back_page = (By.XPATH, "//a[text()='Back to Login page']")
        self.confirmation_message = (By.XPATH, "(//h5[contains(@class, 'card-title') and contains(@class, 'text-center')])[2]")

    def verify_page(self):
        self.locate_element(self.page_header)

    def enter_email(self, email: str):
        self.enter_text(self.your_email, email)

    def click_send(self):
        self.click_element(self.send)

    def is_confirmation_message_displayed(self):
        return self.locate_element(self.confirmation_message).is_displayed()

    def click_back_to_login(self):
        self.click_element(self.back_page)

