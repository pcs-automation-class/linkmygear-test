# Created by catalinak at 12/4/24
Feature: Generate Demo Jump
  # Tests to validate the "Generate Demo Jump" functionality

  Background:
    Given Open "dev" environment
    And User is logged in
    Then Navigate to the Device Dashboard
    And Locate a device card with the name "<device_name>"
    Then Click the "Demo Jump" button on the located device card

  Scenario: Verify presence of the "Generate Demo Jump" modal
    Then Verify the presence of the "Generate Demo Jump" modal
    And Verify the presence of the "Event count" input field
    And Verify the presence of the "Event date" picker
    And Verify the presence of the "Generate demo jump" button
    And Verify the presence of the close ("X") button

  Scenario Outline: Fill out and submit the "Generate Demo Jump" form
    Given User enters "<event_count>" in the "Event count" input field
    And User selects "<event_date>" from the "Event date" picker
    When User clicks the "Generate demo jump" button
    Then Verify the "Demo Jump Success" message or confirmation

    Examples:
      | event_count | event_date        |
      | 60          | 2024-12-31 10:00 |
      | 10          | 2024-12-25 14:00 |
      | 100         | 2025-01-01 09:30 |

  Scenario: Validation for empty fields in the "Generate Demo Jump" form
    Given User leaves the "Event count" input field empty
    When User clicks the "Generate demo jump" button
    Then Verify the presence of the "Event count is required" error message

  Scenario: Validation for invalid event count
    Given User enters "0" in the "Event count" input field
    When User clicks the "Generate demo jump" button
    Then Verify the presence of the "Event count must be greater than 0" error message

  Scenario: Close the "Generate Demo Jump" modal
    Given The "Generate Demo Jump" modal is displayed
    When User clicks the close ("X") button
    Then Verify the "Generate Demo Jump" modal is no longer displayed
