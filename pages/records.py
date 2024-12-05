from base import BasePage


class RecordsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.records_tab = "//a[contains(text(), 'Records')]"
        self.select_device = (
            "//div[contains(@class, 'el-select') and contains(@class, 'is-transparent')]"
        )
        self.start_date = (
            "//input[contains(@placeholder, 'Start date') and contains(@class, 'el-range-input')]"
        )
        self.end_date = (
            "//input[contains(@placeholder, 'End date') and contains(@class, 'el-range-input')]"
        )
        self.month_section = (
            "//div[@class='record-pack month']//time[@class='month' and contains(text(), 'November, 2024')]"
        )
        self.today_date = (
            "//span[@class='format' and not(ancestor::button[@style='display: none;'])]"
        )
        self.parachute_icon = (
            "//div[contains(@class, 'el-timeline-item__content')]"
            "//button[contains(@class, 'timeline-card__day')]"
            "//*[name()='svg' and contains(@viewBox, '0 0 30 30')]"
        )
        self.number_jumps = ""  # Placeholder for now
        self.timeline_card_box = (
            "//div[@class='record-pack month']//div[contains(@class, 'timeline-card__box')]"
        )
        self.details_button = (
            "//div[@class='record-card']//a[contains(@class, 'lmg-btn') and contains(text(), 'Details')]"
        )
        self.record_card_name = "//div[@class='record-card__info']//h4"
        self.record_time_jump = ""  # Placeholder for now
        self.jump_number = "//div[@class='record-card__info']//dd"
        self.group_jumps_button = "//a[contains(text(), 'Group Jumps')]"
        self.logout_button = (
            "//a[contains(@class, 'hidden-on-tablet') and contains(@class, 'lmg-btn')]"
        )
        self.page_header = "//div[@class='lmg-header__box']"

    def verify_page(self):
        super().verify_page(self.header)

    def filter_by_device(self, device_name: str):
        filter_element = self.locate_element(self.filter_device)
        filter_element.click()
        device_option = (By.XPATH, f"//li[contains(text(), '{device_name}')]")
        self.locate_element(device_option).click()

    def filter_by_date(self, start_date: str, end_date: str):
        self.locate_element(self.filter_date).send_keys(start_date)
        self.locate_element(self.filter_date).send_keys(end_date)

    def click_details(self):
        self.locate_element(self.details_button).click()
