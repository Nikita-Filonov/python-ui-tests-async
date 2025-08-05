from playwright.async_api import Page

from components.chart_view_component import ChartViewComponent
from components.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navbar_component import NavbarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

    async def check_visible_students_chart(self):
        await self.students_chart_view.check_visible('Students')

    async def check_visible_courses_chart(self):
        await self.courses_chart_view.check_visible('Courses')

    async def check_visible_activities_chart(self):
        await self.activities_chart_view.check_visible('Activities')

    async def check_visible_scores_chart(self):
        await self.scores_chart_view.check_visible('Scores')
