from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json
from pages.login import LoginPage
from pages.devices import DevicesPage
from pages.records import RecordsPage
from pages.logbook import LogBookPage
from pages.profile import ProfilePage
from pages.forgot_password import ForgotPasswordPage
from pages.device_settings import DeviceSettings


def before_all(context):
    with open("setting.json", "r") as file:
        file_data = json.load(file)
        context.credentials = file_data["Users"]
        context.settings = file_data["Project_settings"]


def before_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        if context.settings["browser"] == "Chrome":
            chrome_options = ChromeOptions()
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                              options=chrome_options)
        elif context.settings["browser"] == "Firefox":
            firefox_options = FirefoxOptions()
            context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                               options=firefox_options)
        else:
            assert False, "Unknown browser!"

        if context.settings["maximize_window"]:  # Same as context.settings["maximize_window"] is True
            context.driver.maximize_window()
        else:
            if context.settings["screens"]["iPhone 14 Pro Max"]["portrait"]:
                screen_width = context.settings["screens"]["iPhone 14 Pro Max"]["screen_width"]
                screen_height = context.settings["screens"]["iPhone 14 Pro Max"]["screen_height"]
            else:
                screen_height = context.settings["screens"]["iPhone 14 Pro Max"]["screen_width"]
                screen_width = context.settings["screens"]["iPhone 14 Pro Max"]["screen_height"]

            context.driver.set_window_size(screen_width, screen_height)

        context.login_page = LoginPage(context.driver)
        context.devices = DevicesPage(context.driver)
        context.records = RecordsPage(context.driver)
        context.logbook = LogBookPage(context.driver)
        context.forgot_password = ForgotPasswordPage(context.driver)
        context.profile = ProfilePage(context.driver)


        context.current_page = context.login_page


def after_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        context.driver.quit()
