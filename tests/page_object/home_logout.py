import time

from tests.page_object.locators_logout_page import locators_logout_page


class home_logout(locators_logout_page):

    def __init__(self):
        self.locator = self.locators_logout

    def successful_logout_home(self, context):
        button_burger = context.web.find_by_id_displayed(self.locators_logout["button_burger"])
        if button_burger is True:
            context.web.find_by_id(self.locators_logout["button_burger"]).click()
            time.sleep(1)
            button_logout = context.web.find_by_id_displayed(self.locators_logout["button_logout"])
            if button_logout is True:
                context.web.find_by_id(self.locators_logout["button_logout"]).click()
                return True
            return True
        return False

    def verify_label_logout(self, context, expected_message):
        msm_xpath = context.web.get_text_xpath(self.locators_logout["label_expected_logout"])
        if msm_xpath == expected_message:
            return True
        return False
