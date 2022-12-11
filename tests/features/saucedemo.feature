@Tests
Feature: Buy product at saucedemo.com
  As a user of saucedemo.com
  I enter saucedemo.com
  To buy a product

  Background: Login to page saucedemo
    Given The user enters the site
    And User wants to login in saucedemo page

  @Successful_Purchase
  Scenario Outline: successful purchase of a product
    When Buy a product "<firstname>" "<lastname>" "<postal_code>" "<product>"
    Then Verify that the purchase successful "THANK YOU FOR YOUR ORDER"

    Examples:
    |firstname|lastname|postal_code|product|
    |Cristian|Hernandez|55450|Sauce Labs Backpack,Sauce Labs Bike Light,Sauce Labs Bolt T-Shirt|

  @logout
  Scenario: successful logout
    When logout session
    Then verify end of session "Accepted usernames are:"

  @failed_login
  Scenario: failed login
    When logout session
    And login session with user "testsUser" and pass "testsPass"
    Then verify login session "Epic sadface: Username and password do not match any user in this service"