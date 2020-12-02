@configTagTest
Feature: Checking user data

  Scenario: Return list of articles
    Given return list of articles using baseURL
    When "GET" http returns 200
    Then return single article url