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

import logging
import os


def before_all(context):
    with open("setting.json", "r") as file:
        file_data = json.load(file)
        context.credentials = file_data["Users"]
        context.settings = file_data["Project_settings"]

    log_file = "logs/my_log.log"

    if os.path.exists(log_file):
        os.remove(log_file)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s- %(levelname)s - %(message)s',
        filemode='w'
    )

    context.logger = logging.getLogger(__name__)


def before_scenario(context, scenario):
    context.logger.info(f"SCENARIO: {scenario.name} Run")
    if "EMULATE" not in scenario.name:
        if context.settings["browser"] == "Chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
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

        context.login_page = LoginPage(context.driver, context.logger)
        context.devices = DevicesPage(context.driver, context.logger)
        context.records = RecordsPage(context.driver, context.logger)
        context.logbook = LogBookPage(context.driver, context.logger)
        context.forgot_password = ForgotPasswordPage(context.driver, context.logger)
        context.profile = ProfilePage(context.driver, context.logger)
        context.device_settings = DeviceSettings(context.driver, context.logger)

        context.current_page = context.login_page


def before_step(context, step):
    context.logger.info(f"STEP: {step.name} run")


def after_step(context, step):
    status = step.status.name
    if status == 'passed':
        context.logger.info(f"STEP: {step.name} is PASSED")
    else:
        context.logger.warning(f"STEP: {step.name} is FAILED")


def after_scenario(context, scenario):
    status = scenario.status.name
    if status == 'passed':
        context.logger.info(f"SCENARIO: {scenario.name} is PASSED")
    else:
        context.logger.warning(f"SCENARIO: {scenario.name} is FAILED")
    if "EMULATE" not in scenario.name:
        context.driver.quit()
