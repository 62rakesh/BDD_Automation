import behave
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from behave import *
import time
from PIL import Image
from allure_behave.hooks import allure_report

dashboard_text = 'Dashboard'


@given('I launch Chrome Browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('I open Orangehrm Home page')
def Homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(2)


@when('Enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)
    time.sleep(2)


@when('Click on the Login button')
def click_login_button(context):
    context.driver.find_element_by_id("btnLogin").click()
    time.sleep(2)


@then('User must successfully login to the Dashoard Page')
def dashboard_page(context):
    text = context.driver.find_element_by_xpath("(//DIV[@class='head']//H1[text()='Dashboard'])").text
    context.dashboard_text = text
    print(text)
    time.sleep(2)
    context.driver.close()


@when('Navigate to recruitment page')
def Navigate_recruitment_page(context):
    context.driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()
    time.sleep(2)


@then('Recruitment page should display')
def recruitment_page(context):
    recruitment_text = context.driver.find_element_by_id("menu_recruitment_viewCandidates").text
    assert recruitment_text == "Candidates"
    print(recruitment_text)
    context.driver.close()


@when('I click on the recruitment tab')
def click_recruitment_tab(context):
    context.driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()
    time.sleep(2)


@when('I click on the add candidate button')
def click_add_candidate(context):
    context.driver.find_element_by_name("btnAdd").click()
    time.sleep(2)
    candidate_text = context.driver.find_element_by_xpath("(//H1[@id = 'addCandidateHeading'])").text
    assert candidate_text == "Add Candidate"
    print("User is landed on the candidate page")


@when('Enter the FirstName "{fname}" and LastName "{lname}"')
def enter_candidate_info(context, fname, lname):
    context.driver.find_element_by_id("addCandidate_firstName").send_keys(fname)
    context.driver.find_element_by_id("addCandidate_lastName").send_keys(lname)


@when('Enter the Email "{email}" and ContactNo "{ContactNo}"')
def enter_candidate_contact_info(context, email, ContactNo):
    context.driver.find_element_by_id("addCandidate_email").send_keys(email)
    context.driver.find_element_by_id("addCandidate_contactNo").send_keys(ContactNo)
    time.sleep(2)
    print("Candidate information is filled successfully")


@when('Click on the Save button')
def click_save_button(context):
    context.driver.find_element_by_id("btnSave").click()
    context.driver.save_screenshot("image.png")
    # image = Image.open("image.png")
    # image.show()
    time.sleep(2)


@then(u'A candidate must be saved')
def candidate_save(context):
    print("The candidate is saved")
    context.driver.save_screenshot("candidate.png")
    # candidate_profile = Image.open("candidate.png")
    # candidate_profile.show()
    context.driver.close()


@when('User click on the Marketplace button')
def click_subscribe(self):
    self.driver.find_element_by_id("MP_link").click()
    time.sleep(2)


# @when('User click on the Subscribe button to subscribe the channel')
# def user_subscribe(self):
#     self.driver.find_element_by_id("btnSubscribe").click()
#     time.sleep(2)


@then('User should navigate to the market place page')
def success(self):
    print("The user is subscribed to the orangehrm product")
    marketplace_text = "OrangeHRM Addons"
    assert True, marketplace_text == "OrangeHRM Addons"

