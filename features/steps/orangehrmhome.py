import time

import behave
from selenium import webdriver
from behave import given, when, then
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'Open Orange hrm homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(2)


@then(u'Verify that the logo present on page')
def Logo(context):
    status = context.driver.find_element_by_xpath("(//DIV[@id='divLogo']//IMG)").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
