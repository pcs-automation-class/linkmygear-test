# Created by catalinak at 12/4/24
Feature: Forgot Password Automation

  Background:
    Given Open "dev" environment
    Then Verify the "login" page is displayed

  @forgot_pwd
  Scenario Outline: Successfully restoring a password
    Then Verify presence of element "forgot password link"
    Then Click "forgot password" element
    Then Verify presence of element "your email field"
    When The user enters a valid "catk.test@gmail.com" into the "Your Email" field
    And Click button "Send"
    Then A confirmation message appears
#    And CK the user receives a password reset email

    Examples:
      | email               |
      | catk.test@gmail.com |