from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
from base import BasePage


class DevicesPage(BasePage):
    def __init__(self):
        super().__init__()
        self.device_settings = (By.XPATH, "//a[contains(@href, 'device-settings')]")
        self.device_name = (By.XPATH, "//div[@class='lmg-device__info']/h4")
        self.charge = (By.XPATH, "//span[@class='indicator']")
        self.device_state = (By.XPATH, "//span[@class='power']")
        self.show_on_map = (By.XPATH, "")
        self.status_updated = (By.XPATH, "")
        self.demo_jump = (By.XPATH, "")
        self.read_more = (By.XPATH, "")
        self.image = (By.XPATH, "")
        self.read_less = (By.XPATH, "")
        self.your_device_label = (By.XPATH, "//h3[@class='section-title']")
        self.news_label = (By.XPATH, "")
        self.charge_icon = (By.XPATH, "")
        self.device_state_icon = (By.XPATH, "")
        self.news_title = (By.XPATH, "")
        self.news_body = (By.XPATH, "")

    def open_device_settings(self):
        self.locate_element(self.device_settings).click()

    def verify_page(self):
        super().verify_page(self.your_device_label)
