# Created by catalinab at 11/27/24
Feature: Records Page Automation

  Background:
    Given Open "dev" environment

  Scenario: Verify filtering and interaction with records
    When User navigates to the "Records" page
    When User filters by device "Device A"
    And User filters by date range from "2024-11-01" to "2024-11-30"
    Then User verifies record "Catalina 21:14 Jump #1" is displayed
    When User clicks "Details" for "Catalina 21:14 Jump #1"
    Then User sees the details page for "Catalina 21:14 Jump #1"
    When User clicks "Group Jumps"
    Then User performs grouping successfully
    When User clicks "Log out"
    Then User is logged out successfully
