from selenium.webdriver.common.by import By

from base import BasePage


class DeviceSettings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_header = (By.XPATH, "//h5[text()='Login to Your Account']")  # Device Settings

    def verify_page(self):
        super().verify_page(self.page_header)