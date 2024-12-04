
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base import BasePage


class ProfilePage(BasePage):
    def __init__(self):
        super().__init__()
        self.page_my_profile = (By.XPATH, "//button[contains(text(), 'My Profile')]")
        self.first_name_field = (By.XPATH, "//div[text()='Please input first name']/preceding-sibling::div/"
                                           "/input[@class='el-input__inner']")
        self.last_name_field = (By.XPATH, "//div[text()='Please select last name']/preceding-sibling::div/"
                                          "/input[@class='el-input__inner']")
        self.email_field = (By.XPATH, "//div[@class='el-input__wrapper']//input[@class='el-input__inner' and "
                                      "@type='text' and @disabled]")
        self.add_phone_button = (By.XPATH, "//button[contains(text(), 'Add Phone')]")
        self.select_prefix = (By.XPATH, "//div[@class='el-select']/div[@class='el-select__wrapper is-filterable "
                                        "el-tooltip__trigger el-tooltip__trigger']")
        self.enter_phone = (By.XPATH, "//input[@type='text' and @placeholder='Enter Phone']")
        self.delete_phone = (By.XPATH, "//div[@class='repeater-input']//button[@type='button']")
        self.sms_checkbox = (By.XPATH, "//span[@class='el-checkbox__inner']")
        self.save_button = (By.XPATH, "//button[contains(text(), 'Save')]")
        self.current_password_field = (By.XPATH, "")
        self.new_password_field = (By.XPATH, "")
        self.confirm_password_field = (By.XPATH, "")
        self.change_password_button = (By.XPATH, "//button[contains(text(), 'Change password')]")

    def verify_page(self):
        super().verify_page(self.profile_header)

    def open_page_my_profile(self):
        self.locate_element(self.page_my_profile).click()

    def type_text(self, field_locator: tuple, text: str):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(field_locator))
        element.clear()
        element.send_keys(text)

    def click_element(self, element_locator: tuple):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element_locator))
        element.click()

    def toggle_sms_acceptance(self, accept: bool):
        checkbox = self.locate_element(self.sms_checkbox)
        if checkbox.is_selected() != accept:
            checkbox.click()