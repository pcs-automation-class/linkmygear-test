# Created by catalinak at 12/4/24
Feature: Forgot Password Automation

  Background:
    Given Open "dev" environment

  Scenario Outline: Successfully restoring a password
    Then Open window "Forgot password?"
    Then Verify presence of element "Your email"
    When The user enters a valid "catk.test@gmail.com" into the "Your Email" field
    And Click button "Send"
    Then A confirmation message appears
#    And CK the user receives a password reset email

  Examples:
    | email                  |
    | catk.test@gmail.com    |