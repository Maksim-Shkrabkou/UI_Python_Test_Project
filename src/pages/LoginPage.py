import allure

from src.pages.page import Page


class LoginPage(Page):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Open login page")
    def open(self):
        self.browser.open("/login")
        return self

    @allure.step("Login as {0} {1}")
    def login_as(self, username, password):
        self.browser.element("//input[@id='usernameOrEmail']").set_value(username)
        self.browser.element("//input[@id='password']").set_value(password)
        self.browser.element("//button[normalize-space()='Login']").click()
