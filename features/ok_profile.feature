Feature: Profile Page Testing

  Scenario: My profile
    Given Open "dev" environment
    Then Click element "//button[contains(@class, 'profile-btn') and contains(@class, 'profile-btn--msg') and contains(@class, 'hidden-on-tablet')]"
    Then Click element "page_my_profile"
    Then Type "John" into "first_name_field"
    Then Type "Kennedy" into "last_name_field"
    Then Verify text "houseattheocean@gmail.com" is in "email_field"
    Then Click element "add_phone_button"
    Then Choose "+1" in "select_prefix"
    Then Type "550-55-50" into "enter_phone"
    Then Toggle SMS acceptance to True
    Then Click element "save_button"
    Then Verify presence of "change_password_button"
    Then Type "mCtwAtjpizSTWEz7" into "current_password_field"
    Then Type "7563259BuyaCat" into "new_password_field"
    Then Type "7563259BuyaCat" into "confirm_password_field"
    Then Click element "change_password_button"











