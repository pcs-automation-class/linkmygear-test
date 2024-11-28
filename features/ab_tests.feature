# Created by andrey at 11/26/24
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Login with correct credentials
#    Given Login in "dev" env as "user"
    Given Open url "dev" env
    Then Fillout "Good user" credentials
    Then Click "login" button
    