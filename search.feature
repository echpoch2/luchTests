Feature: Search
    Scenario: Search with empty query
        Given I am on https://luch.by/ page
        When I don't type to SEARCH_INPUT
        When I press SEARCH_BUTTON
        Then I should see label with error message about empty query
    Scenario: Search with incorrect query
        Given I am on https://luch.by/ page
        When I type КРОССОВКИ to SEARCH_INPUT
        When I press SEARCH_BUTTON
        Then I should see label with error message about empty result
    Scenario: Search with correct query
        Given I am on https://luch.by/ page
        When I type ЧАСЫ to SEARCH_INPUT
        When I press SEARCH_BUTTON
        Then I should see search results