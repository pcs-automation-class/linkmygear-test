# Created by catalinak at 12/4/24
Feature: Create Account

  Background:
    Given Open "dev" environment

  Scenario: Open Create Account page
    Then Verify the presence of the Create Account page

  Scenario Outline: Create Account with invalid inputs
    Then Enter "<email>" in the email field
    Then Accept the Terms and Conditions checkbox: <agree_terms>
    Then Click the Register button
    Then Verify the error message "<error_message>"

    Examples:
      | email                 | agree_terms | error_message                                |
      | testemail@gmail.com   | false       | Please agree to Terms and Conditions         |
      | invalidemail          | true        | Invalid email format                         |
      |                       | true        | Email is required                            |

  Scenario: Create Account successfully
    Then Enter a valid email in the email field
    Then Accept the Terms and Conditions checkbox: true
    Then Click the Register button
    Then Verify the success message

  Scenario: Navigate back to Login page
    Then Click the "Log in" link
    Then Verify the presence of the Login page
