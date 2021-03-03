import allure
from selene.core.entity import SeleneElement

from src.pages.page import Page


class MainPage(Page):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step
    def open(self):
        self.browser.open("/list")
        return self

    @allure.step
    def brand_name(self):
        return self.browser.element("//a[normalize-space()='QAGuild']")

    @allure.step
    def episode_name(self) -> SeleneElement:
        return self.browser.element("span.episode-name")
