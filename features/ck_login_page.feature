# Created by catalinak at 12/4/24
Feature: Login Page Tests

  Background:
    Given Open "dev" environment
    Then Verify the Login page is displayed

  Scenario Outline: Login with correct credentials
    Then Enter email "valid_user_email" into the email field
    Then Enter password "valid_user_password" into the password field
    Then Click the Login button
    Then Verify the Home page is displayed

    Examples:
      | valid_user_email      | valid_user_password |
      | catk.test@gmail.com   | strongpassword      |

  Scenario Outline: Login with incorrect username
    Then Enter email "<username>" into the email field
    Then Enter password "valid_user_password" into the password field
    Then Click the Login button
    Then Verify error message "Invalid username or password"

    Examples:
      | username               |
      | catk.tes@gmail.com     |
      | catk.test@gmail.co     |
      | catk.testgmail.com     |

  Scenario Outline: Login with incorrect password
    Then Enter email "valid_user_email" into the email field
    Then Enter password "<password>" into the password field
    Then Click the Login button
    Then Verify error message "Invalid username or password"

    Examples:
      | password   |
      | strong     |
      | password   |

  Scenario Outline: Login with empty fields
    Then Enter email "<username>" into the email field
    Then Enter password "<password>" into the password field
    Then Click the Login button
    Then Verify error message "Invalid username or password"

    Examples:
      | username            | password       |
      | none                | strongpassword |
      | catk.test@gmail.com | none           |
      | none                | none           |