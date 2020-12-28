Feature: Adding
    Scenario: Adding one item
        Given I am on https://luch.by/kollektsii/80-s/740257587/ page
        When I add item to cart
        Then I should see 1 items in my cart
    Scenario: Adding one more item
        Given I am on https://luch.by/kollektsii/80-s/740257588/ page
        When I add item to cart
        Then I should see 2 items in my cart
    Scenario: Check total cost
        Given I am on https://luch.by/cart page
        Then Sum of each item cost should be equals to total cost