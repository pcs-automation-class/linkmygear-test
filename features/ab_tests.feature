# Created by andrey at 11/26/24
Feature: # Enter feature name here
  # Enter feature description here

  @example
  Scenario: Login with correct credentials
    Given Login as "test_1" in "dev" environment
    Then Wait 1 seconds

  @example2
  Scenario: Test 2 correct credentials
    Given Login as "test_2" in "dev" environment
    Then Wait 1 seconds
