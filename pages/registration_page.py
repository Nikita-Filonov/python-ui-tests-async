import re

from playwright.async_api import Page

from components.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.login_link = Link(page, "registration-page-login-link", "Login")
        self.registration_button = Button(page, "registration-page-registration-button", "Registration")

    async def click_registration_button(self):
        await self.registration_button.click()
        await self.check_current_url(re.compile(".*/#/dashboard"))
