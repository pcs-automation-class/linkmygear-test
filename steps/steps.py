from time import sleep

from behave import step
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.forgot_password import ForgotPasswordPage
from pages.login import LoginPage, login


@step('Open "{env}" environment')
def open_url(context, env):
    environments = {
        "dev": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com",
        "prod": "https://app.linkmygear.com",
    }

    context.driver.get(environments[env])
    context.login_page = LoginPage(context.driver)
    context.current_page = context.login_page

@step('Verify presence of element "{element_name}"')
def verify_element_presence(context, element_name):
    element = None

    if element_name.lower() == "forgot password link":
        element = context.current_page.forgot_password_link
    elif element_name.lower() == "your email field":
        element = context.current_page.your_email
    elif element_name.lower() == "send button":
        element = context.current_page.send
    else:
        assert False, f"Unknown element: {element_name}"

    assert context.current_page.locate_element(element).is_displayed(), f"Element '{element_name}' is not displayed"


@step('The user enters "{text}" into the "{field_name}" field')
def enter_text_into_field(context, text, field_name):
    if field_name.lower() == "your email":
        context.current_page.enter_text(context.current_page.your_email, text)
    else:
        assert False, f"Unknown field: {field_name}"

@step('Click button "{button_name}"')
def click_button(context, button_name):
    if button_name.lower() == "send":
        context.current_page.click_element(context.current_page.send)
    else:
        assert False, f"Unknown button: {button_name}"

@step('Click "{element_name}" element')
def click_element_by_name(context, element_name):
    if element_name.lower() == "forgot password":
        context.login_page.click_forgot_password()
        context.forgot_password_page = ForgotPasswordPage(context.driver)
        context.current_page = context.forgot_password_page
        context.forgot_password_page.verify_page()
    else:
        assert False, f"Unknown element: {element_name}"

