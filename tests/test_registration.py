import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from tools.routes import AppRoute


@pytest.mark.asyncio
@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @allure.title("Successful registration")
    async def test_successful_registration(
            self,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        await registration_page.visit(AppRoute.REGISTRATION)
        await registration_page.registration_form.check_visible(email="", username="", password="")
        await registration_page.registration_form.fill(
            email="user@example.com",
            username="Playwright",
            password="qwerty"
        )
        await registration_page.click_registration_button()

        await dashboard_page.navbar.check_visible("Playwright")
        await dashboard_page.dashboard_toolbar_view.check_visible()
        await dashboard_page.check_visible_scores_chart()
        await dashboard_page.check_visible_courses_chart()
        await dashboard_page.check_visible_students_chart()
        await dashboard_page.check_visible_activities_chart()
