from tests.page_object.locators_login_page import locators_login_page


class home_login(locators_login_page):

    def __init__(self):
        self.locator = self.locators_login

    def successful_login_home(self, context, user, pwd):
        user_name = context.web.find_by_id_displayed(self.locators_login["input_user"])
        password = context.web.find_by_id_displayed(self.locators_login["input_pass"])

        if user_name is True and password is True:
            context.web.find_by_id(self.locators_login["input_user"]).send_keys(user)
            context.web.find_by_id(self.locators_login["input_pass"]).send_keys(pwd)
            context.web.find_by_id(self.locators_login["button_login"]).click()
            return True
        return False

    @staticmethod
    def successful_add_products(context, product):
        for product_in in product.split(','):
            context.web.find_by_xpath("//div[contains(text(),'" + product_in + "')]/../../../div/button").click()

    def buy_successfully(self, context, firstname, lastname, postal_code):
        button_car = context.web.find_by_xpath_displayed(self.locators_buy["button_car"])

        if button_car is True:
            context.web.find_by_xpath(self.locators_buy["button_car"]).click()
            button_checkout = context.web.find_by_id_displayed(self.locators_buy["button_checkout"])
            if button_checkout is True:
                context.web.find_by_id(self.locators_buy["button_checkout"]).click()
                firstname_user = context.web.find_by_id_displayed(self.locators_buy["input_firstname"])
                lastname_user = context.web.find_by_id_displayed(self.locators_buy["input_lastname"])
                postal_code_user = context.web.find_by_id_displayed(self.locators_buy["input_postal_code"])
                button_continua = context.web.find_by_id_displayed(self.locators_buy["button_continue"])

                if firstname_user is True and lastname_user is True and postal_code_user is True and button_continua is True:
                    context.web.find_by_id(self.locators_buy["input_firstname"]).send_keys(firstname)
                    context.web.find_by_id(self.locators_buy["input_lastname"]).send_keys(lastname)
                    context.web.find_by_id(self.locators_buy["input_postal_code"]).send_keys(postal_code)
                    context.web.find_by_id(self.locators_buy["button_continue"]).click()
                    context.web.find_by_id(self.locators_buy["button_finish"]).click()
                    return True
        return False

    def verify_label_finish(self, context, expected_message):
        msm_xpath = context.web.get_text_xpath(self.locators_buy["label_finish"])
        if msm_xpath == expected_message:
            return True
        return False

    def verify_label_failed_login(self, context, expected_message):
        msm_xpath = context.web.get_text_xpath(self.locators_login["label_failed_login"])
        if msm_xpath == expected_message:
            return True
        return False
