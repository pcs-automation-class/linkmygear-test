# Created by Anna at 12/1/24
Feature: Update Devices Names

  Scenario: Update Device Name
    Given Open "dev" environment
    Then Fill out "user" credentials
    Then Click "Login" button
    Then Click "device_gear" button
    Then Verify presence of Element "Device Settings"
    Then Select device to be edited
    Then Click "Edit" button
    Then Verify presence of element "Edit_Device"
    Then Update Name
    Then Click "Update" button
    And Verify Device name is updated
    # Enter steps here