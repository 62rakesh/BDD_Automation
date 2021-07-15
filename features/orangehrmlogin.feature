@Sto002
@Author:-Rakesh
Feature: OrangeHRM Login

  Background: common steps
    Given I launch Chrome Browser
    When I open Orangehrm Home page
    And Enter username "admin" and password "admin123"
    And Click on the Login button


@Step1
  Scenario: Login to Orangehrm with valid credentials
    Then User must successfully login to the Dashoard Page

#  Scenario Outline: Login to Orangehrm with valid credentials
#    Then User must successfully login to the Dashoard Page
#
#    Examples:
#      | username | password |
#      | admin    | admin123 |

@Step2
  Scenario: Recruitment tab navigation
    When Navigate to recruitment page
    Then Recruitment page should display

@Step3
  Scenario: Add candidate
    When I click on the recruitment tab
    And I click on the add candidate button
    And Enter the FirstName "RakeshTest" and LastName "DemoTest"
    And Enter the Email "test_rakesh@gmail.com" and ContactNo "9910768233"
    And Click on the Save button
    Then A candidate must be saved

