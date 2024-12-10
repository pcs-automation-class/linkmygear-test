from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import element_to_be_selected
# from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage


class LogBookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_logbook = (By.XPATH, "//a[contains(text(), 'LogBook')]")
        self.page_header = (By.XPATH, "//h1[@class='section-left-tite']")
        self.log_clear_icon = (By.XPATH, "//button[@class='logb-filters__clear']")
        self.select_device = (By.XPATH, "//span[contains(text(), 'Select device')]")
        self.start_date = (By.XPATH, "//input[@placeholder='Start date']")
        self.end_date = (By.XPATH, "//input[@placeholder='End date']")
        self.select_dropzone = (By.XPATH, "//span[contains(text(),'Select dropzone')]")
        self.add_new_jump = (By.XPATH, "//span[contains(text(),'Add new jump')]")
        self.jump_number = (By.XPATH, "")
        self.view_button = (By.XPATH, "//button[contains(text(), 'View')]")
        self.parachute_icon = (By.XPATH, "")
        self.total_jumps = (By.XPATH, "//span[@class='sep']")
        self.month_jumps = (By.XPATH, "//div[@class='record-pack month']")
        self.date_jumps = (By.XPATH, "//div[@class='timeline-card']")
        self.jump_info_page = (By.XPATH, "//h4[contains(text(), 'Jump info')]")
        self.three_dots = (By.XPATH, "//button[@class='action-btn-3dot__trigger']")
        self.question = (By.XPATH, "//h3[contains(text(),'May be you want to sign your jump?')]")
        self.sign_jump_button = (By.XPATH, "//button[contains(text(),'Sign jump')]")

    def verify_logbook_page(self):
        self.locate_element(self.page_logbook).click()

    def open_logbook_page(self):
        self.locate_element(self.page_logbook).click()

    def verify_page(self):
        super().verify_page(self.page_header)

