from selenium.webdriver.common.by import By

from base import BasePage

class RecordsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.header = (By.XPATH, "")

    def verify_page(self):
        super().verify_page(self.header)
