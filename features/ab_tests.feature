Feature: Login tests

  @example
  Scenario: Login with correct credentials
    Given Login as "test_1" in "dev" environment
    Then Wait 1 seconds

  @example2
  Scenario: Test 2 correct credentials
    Given Login as "test_1" in "dev" environment
#    Then Verify presence of element "New"
    Then Wait 1 seconds
