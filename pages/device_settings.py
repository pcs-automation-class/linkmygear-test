from selenium.webdriver.common.by import By

from pages.base import BasePage


class DeviceSettings(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger = logger
        self.page_header = (By.XPATH, "//h5[text()='Login to Your Account']")
        self.device_name = (By.XPATH, "//td[@class='el-table_3_column_9 el-table__cell']//span")
        self.edit_device_name = (By.XPATH, "")

    def verify_page(self):
        super().verify_page(self.page_header)
