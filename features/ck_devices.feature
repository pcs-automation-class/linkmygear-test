# Created by catalinak at 12/4/24
Feature: Device Dashboard Tests
  # Tests to validate the device dashboard functionality and elements

  Background:
    Given Open "dev" environment
    Then Verify the presence of the "Your device" page

  Scenario: Verify device cards
    Then Verify that each device card has a name displayed
    Then Verify that each device card has a battery percentage displayed
    Then Verify that each device card has a power status (On/Off) displayed
    Then Verify that each device card has an "Updated" timestamp displayed
    Then Verify that each device card has a "Show on map" button

  Scenario: Perform actions on a device card
    Given Locate a device card with the name "<device_name>"
    Then Click the "Show on map" button on the located device card
    Then Verify that the map is displayed for the selected device

  Scenario Outline: Validate Demo Jump functionality
    Given Locate a device card with the name "<device_name>"
    Then Verify the presence of the "Demo Jump" button on the located device card
    Then Click the "Demo Jump" button
    Then Verify the demo jump page or action is triggered

    Examples:
      | device_name     |
      | John            |
      | Romie           |
      | Catalina        |

  Scenario: Validate settings link
    Then Click the settings icon
    Then Verify that the settings page is displayed

  Scenario: Validate all device cards
    Then Verify that all device cards are clickable and display detailed information when clicked
