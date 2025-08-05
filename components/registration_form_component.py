import allure
from playwright.async_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "registration-form-email-input", "Email")
        self.username_input = Input(page, "registration-form-username-input", "Username")
        self.password_input = Input(page, "registration-form-password-input", "Password")

    @allure.step("Fill registration form")
    async def fill(self, email: str, username: str, password: str):
        await self.email_input.fill(email)
        await self.email_input.check_have_value(email)

        await self.username_input.fill(username)
        await self.username_input.check_have_value(username)

        await self.password_input.fill(password)
        await self.password_input.check_have_value(password)

    @allure.step("Check visible registration form")
    async def check_visible(self, email: str, username: str, password: str):
        await self.email_input.check_visible()
        await self.email_input.check_have_value(email)

        await self.username_input.check_visible()
        await self.username_input.check_have_value(username)

        await self.password_input.check_visible()
        await self.password_input.check_have_value(password)
