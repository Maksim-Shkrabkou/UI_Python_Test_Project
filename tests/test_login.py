from selene import have


# def test_can_login_with_valid_credentials(browser):
#     browser.open("/login")
#     browser.element("//input[@id='usernameOrEmail']").set_value("admin")
#     browser.element("//input[@id='password']").set_value("123456")
#     browser.element("//button[normalize-space()='Login']").click()
#     browser.element("//a[normalize-space()='QAGuild']").should(have.exact_text("QAGuild"))


def test_can_login_with_valid_credentials_obj(app):
   app.login_page()\
        .open()\
        .login_as("admin", "123456")

   app.main_page() \
       .brand_name() \
       .should(have.exact_text("QAGuild"))
