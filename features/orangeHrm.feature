
@Sto001
Feature: OrangeHrm Logo

  Scenario: Logo Presence on OrangeHrm home Page
    Given Launch Chrome browser
    When Open Orange hrm homepage
    Then Verify that the logo present on page
    And close browser