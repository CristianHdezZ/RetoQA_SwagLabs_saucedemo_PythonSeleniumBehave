import time
from behave import when, then, given

from tests.page_object.home_login import home_login
from tests.page_object.home_logout import home_logout

global HOME


@given(u'The user enters the site')
def step_impl(context):
    context.web.open('https://www.saucedemo.com/')
    context.web.maximize()


@given(u'user wants to login in saucedemo page')
def step_impl(context):
    home = home_login()
    result = home.successful_login_home(context, "standard_user", "secret_sauce")
    assert result is True


@when(u'Buy a product "{firstname}" "{lastname}" "{postal_code}" "{product}"')
def step_impl(context, firstname, lastname, postal_code, product):
    home = home_login()
    home.successful_add_products(context, product)
    result_buy = home.buy_successfully(context, firstname, lastname, postal_code)
    assert result_buy is True


@then(u'Verify that the purchase successful "{result}"')
def step_impl(context, result):
    home = home_login()
    result = home.verify_label_finish(context, result)
    time.sleep(2)
    assert result is True


@when(u'logout session')
def step_impl(context):
    home = home_logout()
    home.successful_logout_home(context)


@then(u'verify end of session "{result}"')
def step_impl(context, result):
    home = home_logout()
    result_logout = home.verify_label_logout(context, result)
    time.sleep(2)
    assert result_logout is True


@when(u'login session with user "{testsUser}" and pass "{testsPass}"')
def step_impl(context, testsUser, testsPass):
    home = home_login()
    result = home.successful_login_home(context, testsUser, testsPass)
    assert result is True


@then(u'verify login session "{result}"')
def step_impl(context, result):
    home = home_login()
    result = home.verify_label_failed_login(context, result)
    time.sleep(2)
    assert result is True
