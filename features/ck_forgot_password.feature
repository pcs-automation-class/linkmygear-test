# Created by catalinak at 12/4/24
Feature: Forgot Password Automation

  Background:
    Given Open "dev" environment
    Then Verify the "login" page is displayed

  Scenario Outline: Successfully restoring a password
    Then Verify presence of element "forgot password link"
    Then Click "forgot password" element
    Then Verify presence of element "your email"
    When The user enters a valid "catk.test@gmail.com" into the "Your Email" field
    And Click button "Send"
    Then A confirmation message appears
#    And CK the user receives a password reset email

  Examples:
    | email                  |
    | catk.test@gmail.com    |

  Scenario Outline: Attempting to restore a password with an empty email field
    Then Verify presence of element "forgot password link"
    Then Click "forgot password" element
    Then Verify presence of element "your email"
    When The user leaves the "your email" field empty
    And Click button "Send"
    Then An error message for empty email field appears

  Examples:
    | email                  |
    | none                   |

  Scenario Outline: Change Device Name
    Then Open Device Settings
    Then Change Device Name
