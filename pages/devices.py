from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
# from base import BasePage
from pages.base import BasePage


class DevicesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.device_settings = (By.XPATH, "//a[contains(@href, 'device-settings')]")
        self.device_name = (By.XPATH, "//div[@class='lmg-device__info']/h4")
        self.charge = (By.XPATH, "//span[@class='indicator']")
        self.device_state = (By.XPATH, "//span[@class='power']")
        self.show_on_map = (By.XPATH, "//button[contains(text(), 'Show on map')]")
        self.status_updated = (By.XPATH, "//*[contains(text(), 'Updated')]")
        self.demo_jump = (By.XPATH, "//button[contains(text(), 'Demo Jump')]")
        self.read_more = (By.XPATH, "//div[@class='lmg-news']//button[text()='Read more']")
        self.image = (By.XPATH, "")
        self.read_less = (By.XPATH, "")
        self.page_header = (By.XPATH, "//h3[@class='section-title']")
        self.news_label = (By.XPATH, "")
        self.charge_icon = (By.XPATH, "")
        self.device_state_icon = (By.XPATH, "")
        self.news_title = (By.XPATH, "")
        self.news_body = (By.XPATH, "")
        self.edit_button = (By.XPATH, "")
        self.edit_page_device_name = (By.XPATH, "")
        self.edit_page_update_button = (By.XPATH, "")

    def open_device_settings(self):
        self.locate_element(self.device_settings).click()

    def click_edit_button_by_name(self, name: str):
        pass

    def click_edit_button_by_imei(self, imei: str):
        pass

    def verify_page(self):
        super().verify_page(self.page_header)

    def rename_device_by_imei(self, imei: str, new_name: str):
        self.rename_device("imei", imei, new_name)

    def rename_device_by_name(self, old_name: str, new_name: str):
        self.rename_device("name", old_name, new_name)

    def rename_device(self, by: str, identifier: str, new_name):
        if by == "imei":
            self.click_edit_button_by_imei(identifier)
        elif by == "name":
            self.click_edit_button_by_name(identifier)
        else:
            raise

        self.enter_text(self.edit_page_device_name, new_name)
        self.click_element(self.edit_page_update_button)
