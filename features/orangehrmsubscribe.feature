@Sto003
@Author:-Rakesh
Feature: OrangeHRM user subscribe

  Background: common steps
    Given I launch Chrome Browser
    When I open Orangehrm Home page
    And Enter username "admin" and password "admin123"
    And Click on the Login button


@Step2
  Scenario: User subscription
    When User click on the Subscribe button
    And User click on the Subscribe button to subscribe the channel
    Then User should be subscribed