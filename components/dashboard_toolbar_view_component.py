import allure
from playwright.async_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Dashboard')

    @allure.step("Check visible dashboard toolbar view")
    async def check_visible(self):
        await self.title.check_visible()
        await self.title.check_have_text('Dashboard')
