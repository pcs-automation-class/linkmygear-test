from selenium.webdriver.common.by import By

from base import BasePage


class DeviceSettings(BasePage):
    def __init__(self):
        super().__init__()
        self.header = (By.XPATH, "")  # Device Settings


    def __init__(self):
        super().__init__()
        self.page_header = (By.XPATH, "//h5[text()='Login to Your Account']")
        self.email = (By.XPATH, "")

    def verify_page(self):
        super().verify_page(self.header)