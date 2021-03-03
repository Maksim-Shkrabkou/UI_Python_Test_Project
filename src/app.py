import allure
from selene import Browser

from src.pages.LoginPage import LoginPage
from src.pages.MainPage import MainPage


class Application(object):

    def __init__(self, browser: Browser):
        self.browser = browser

    def auth(self):
        self.browser.driver. \
            execute_script('window.localStorage.setItem(arguments[0], arguments[1]);', "access_token",
                           "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjE0Mjk0Mzk1LCJleHAiOjE2MTQ4OTkxOTV9.O3N_WD5m8rvBIbOgS6ra4eYYdNHclj5f5B8eYtG8N6lNaiCp1I4cyNgMydkjDLN-89UiBXKfuJQNVMUDCiYCkQ")

        # self.browser.driver.add_cookie({
        #     'name': 'access_token',
        #     'value': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjE0Mjk0Mzk1LCJleHAiOjE2MTQ4OTkxOTV9.O3N_WD5m8rvBIbOgS6ra4eYYdNHclj5f5B8eYtG8N6lNaiCp1I4cyNgMydkjDLN-89UiBXKfuJQNVMUDCiYCkQ'})

    @allure.step
    def login_page(self):
        return LoginPage(self.browser)

    @allure.step
    def main_page(self):
        return MainPage(self.browser)
