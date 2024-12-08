from time import sleep

from behave import step
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.login import LoginPage, login
from profile import ProfilePage


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
    elif page_name.lower() == "profile":
        context.profile.verify_page()
    else:
        assert False, f"Unknown page: {page_name}"


@step('Click element "{locator_name}"')
def step_impl(context, locator_name):
    profile_page = ProfilePage(context.driver)
    locator = getattr(profile_page, locator_name)
    profile_page.click_element(locator)


@step('Type "{text}" into "{field_name}"')
def step_impl(context, text, field_name):
    profile_page = ProfilePage(context.driver)
    field_locator = getattr(profile_page, field_name)
    profile_page.type_text(field_locator, text)


@step('Verify text "{expected_text}" is in "{field_name}"')
def step_impl(context, expected_text, field_name):
    profile_page = ProfilePage(context.driver)
    field_locator = getattr(profile_page, field_name)
    element = profile_page.locate_element(field_locator)
    assert element.get_attribute("value") == expected_text, f"Expected {expected_text}, but got {element.get_attribute('value')}"


@step('Toggle SMS acceptance to {state}')
def step_impl(context, state):
    profile_page = ProfilePage(context.driver)
    profile_page.toggle_sms_acceptance(state.lower() == "true")