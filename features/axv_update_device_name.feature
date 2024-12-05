# Created by Anna at 12/1/24
Feature: Update Devices

  Scenario: Update Device Name
    Given user Open "dev" environment
    Then user Fill out "user_x" credentials
    Then user Click "Login" button
    Then user Click "device_gear" button
    Then user Verify presence of Element "Device Settings"
    Then user select device to be edited
    Then user Click "Edit" button
    Then user Verify presence of element "Edit_Device"
    Then user Update Name
    Then user Click "Update" button
    # Enter steps here