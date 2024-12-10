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


def before_all(context):
    with open("setting.json", "r") as file:
        file_data = json.load(file)
        context.credentials = file_data["Users"]
        context.DeviceSettings = file_data["Project_settings"]


def before_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        if context.DeviceSettings["browser"] == "Chrome":
            chrome_options = ChromeOptions()
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                              options=chrome_options)
        elif context.DeviceSettings["browser"] == "Firefox":
            firefox_options = FirefoxOptions()
            context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                               options=firefox_options)
        else:
            assert False, "Unknown browser!"

        if context.DeviceSettings["maximize_window"]:  # Same as context.DeviceSettings["maximize_window"] is True
            context.driver.maximize_window()
        else:
            if context.DeviceSettings["screens"]["iPhone 14 Pro Max"]["portrait"]:
                screen_width = context.DeviceSettings["screens"]["iPhone 14 Pro Max"]["screen_width"]
                screen_height = context.DeviceSettings["screens"]["iPhone 14 Pro Max"]["screen_height"]
            else:
                screen_height = context.DeviceSettings["screens"]["iPhone 14 Pro Max"]["screen_width"]
                screen_width = context.DeviceSettings["screens"]["iPhone 14 Pro Max"]["screen_height"]

            context.driver.set_window_size(screen_width, screen_height)

        context.login_page = LoginPage()
        context.devices = DevicesPage()
        context.records = RecordsPage()
        context.logbook = LogBookPage()


def after_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        context.driver.quit()
