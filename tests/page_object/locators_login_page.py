class locators_login_page:
    locators_login = {
        "input_user": "user-name",
        "input_pass": "password",
        "button_login": "login-button",
        "label_failed_login": "//*[@id='login_button_container']//button/.."
    }

    locators_buy = {
        "button_car": "//a[@class='shopping_cart_link']",
        "button_checkout": "checkout",
        "input_firstname": "first-name",
        "input_lastname": "last-name",
        "input_postal_code": "postal-code",
        "button_continue": "continue",
        "button_finish": "finish",
        "label_finish": "//h2[@class='complete-header']"
    }