# Created by catalinak at 12/4/24
Feature: Rename devices Automation
  # Enter feature description here

  Scenario Outline: Rename Device
    Given Login as "test_1" in "dev" environment
    Then Open window "Device Settings"
    Then Wait 2 seconds
    Then Click button "Edit"
    Then Rename "Name" to "<new_name>"
    Then Click button "Update"
    Then Verify pop-up message for "<new_name>"
    Then Verify updated device name presence "<new_name>"
    Then Verify device name is updated to "<new_name>"
    Examples:
      | new_name                             |
      | John                                 |
