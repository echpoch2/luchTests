Feature: Promo
    Scenario: Input incorrect promo
        Given I am on https://luch.by/cart page
        When I type QWERTY to PROMO_INPUT
        When I press PROMO_BUTTON
        Then I should see label with error message