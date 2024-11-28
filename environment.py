from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json
# from pages.login import LoginPage
from pages.devices import DevicesPage
from pages.records import RecordsPage


def before_all(context):
    with open("setting.json", "r") as file:
        file_data = json.load(file)
        context.credentials = file_data["Users"]
        context.settings = file_data["Project_settings"]


def before_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        if context.settings["browser"]  == "Chrome":
            chrome_options = ChromeOptions()
            context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                              options=chrome_options)
        elif context.settings["browser"]  == "Firefox":
            firefox_options = FirefoxOptions()
            context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                               options=firefox_options)
        else:
            assert False, "Unknown browser!"

        # TODO add in settings maximize_window or not
        # if maximize_window == True
        context.driver.maximize_window()

        # context.login_page = LoginPage(context.driver)
        context.devices = DevicesPage()
        context.records = RecordsPage()


def after_scenario(context, scenario):
    if "EMULATE" not in scenario.name:
        context.driver.quit()

#
# press button run
#
# def before_all
#
# def before_feature
#
# def before_scenario
#
#     run scenario
#
# def before_step
#
#     run step Given Login in "dev" env as "user"
#
# def after_step
#
# def before_steps
#
#     run Given Open url "dev" env
#
# def after_steps
#
# def before_steps
#
#     run Then Fillout "Good user" credentials
#
# def after_steps
#
# def before_step
#     run Then Click "login" button
#
# def after_steps
#
# def after_scenario
#
# def after_feature
#
# def after_all
