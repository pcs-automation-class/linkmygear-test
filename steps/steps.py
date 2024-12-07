from time import sleep

from behave import step
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.login import LoginPage, login


@step('Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    context.driver.get(environments[env])


@step('Verify the "{page_name}" page is displayed')
def verify_page_is_displayed(context, page_name):
    # TODO add all other pages
    if page_name.lower() == "login":
        context.login_page.verify_page()
    elif page_name.lower() == "devices":
        context.devices.verify_page()
    elif page_name.lower() == "records":
        context.records.verify_page()
    elif page_name.lower() == "logbook":
        context.logbook.verify_page()
    else:
        assert False, f"Unknown page: {page_name}"
