Feature: LogBook page verification
   Background:
     Given Open "dev" environment
     Then Fillout "Good user" credentials
     Then Click "login" button

  Scenario: Verify UI of the LogBook page
     Then I navigate to LogBook page
     And I should see the page header
     And I should see the "Clear filters" icon
     And I should see the "Select device" dropdown
     And I should see the "Start date" field
     And I should see the "End date" field
     And I should see the "Select dropzone" dropdown
     And I should see the "Add new jump" button


  Scenario: View jump statistics for selected device within a date range
     Then I navigate to LogBook page
     Then I select device
     And I set the start date
     And I set the end date
     Then I see the total number of jumps
     And I see the jumps for the month
     And I see the jumps listed by date


 Scenario: View information about a jump
    Then I navigate to the LogBook page
    When I select a jump and click on the "View" button
    Then I should see the "Jump info" window
    And I should see the date of the jump
    And I should see the jump number
    And I should see the device name
    Then I should see the question "Maybe you want to sign your jump?"
    And I should see the "Sign jump" button
    When I click on the "three dots" button
    Then I should see a dropdown menu with options for the jump



