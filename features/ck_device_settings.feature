# Created by catalinak at 12/4/24
Feature: Device Settings Automation

  Background:
    Given Login as "<username>" in "<environment>" environment
    And Navigate to "Device Settings" page

  Scenario Outline: Rename Device
#    When Click button "Edit" for the device "<current_name>"
    And Rename the device with name "<current_name>" to "<new_name>"
#    And Rename the device with imei "<imei>" to "<new_name>"
    And Click button "Update"
    Then Verify success pop-up message contains "<new_name>"
    And Verify the updated device name "<new_name>" is displayed in the list

    Examples:
      | username  | environment | current_name | new_name         |
      | test_1    | dev         | John         | NewDeviceName1   |
      | test_2    | dev         | Romie        | NewDeviceName2   |

  Scenario Outline: Delete Device
    When Click button "Delete" for the device "<device_name>"
    And Confirm the deletion in the pop-up
    Then Verify the device "<device_name>" is no longer in the list

    Examples:
      | username  | environment | device_name  |
      | test_1    | dev         | John         |
      | test_2    | dev         | Romie        |

  Scenario Outline: Add New Device
    When Click button "Add new device"
    And Enter IMEI "<imei>" and Name "<new_name>"
    And Click button "Register"
    Then Verify the new device "<new_name>" with IMEI "<imei>" is added to the list

    Examples:
      | username  | environment | imei            | new_name         |
      | test_3    | dev         | 999992951664148 | TestDevice1      |
      | test_4    | dev         | 888881234567890 | TestDevice2      |
