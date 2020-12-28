Feature: Email subscribe
    Scenario: Subscribe with incorrect email
        Given I am on https://luch.by/ page
        When I type asd@asd to EMAIL_INPUT
        When I press SUBSCRIBE_BUTTON
        Then I should see popup with error message
    Scenario: Subscribe with correct email
        Given I am on https://luch.by/ page
        When I type ivanov@mail.ru to EMAIL_INPUT
        When I press SUBSCRIBE_BUTTON
        Then I should see popup with success message