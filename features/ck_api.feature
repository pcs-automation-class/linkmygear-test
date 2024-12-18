# Created by catalinak at 12/4/24
Feature: Test API
  # Not tests. Scenarios send messages to emulate device behaviour

  Scenario: EMULATE Add device message
    Given Create new record for device with following data
      | key       | value           |
      | imei      | 333333333333351 |
      | date      | 20241115        |
      | jump      | 2               |
      | latitude  | -18.3           |
      | longitude | 133.5243937     |


  Scenario: EMULATE Device heartbeat message
    Given Create new heartbeat message for device with following data
      | key       | value           |
      | imei      | 333333333333351 |
      | date      | 20241122        |
      | latitude  | 37.770198       |
      | longitude | -121.641856     |
      | battery   | 80              |
#      states: idle, on, off
      | state     | idle            |
