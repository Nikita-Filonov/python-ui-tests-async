import uuid

import allure
import pytest_asyncio
from playwright.async_api import Page, expect, async_playwright

from config import Settings
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest_asyncio.fixture
async def chromium_page(settings: Settings) -> Page:
    async with async_playwright() as playwright:
        expect.set_options(timeout=settings.expect_timeout)

        browser = await playwright.chromium.launch(headless=settings.headless)
        context = await browser.new_context(
            base_url=f"{settings.app_url}/",
            record_video_dir=settings.videos_dir
        )
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        yield page

        video_file = await page.video.path()
        tracing_file = settings.tracing_dir.joinpath(f'{uuid.uuid4()}.zip')
        await context.tracing.stop(path=tracing_file)
        await browser.close()

        allure.attach.file(tracing_file, name='trace', extension='zip')
        allure.attach.file(video_file, name='video', attachment_type=allure.attachment_type.WEBM)


@pytest_asyncio.fixture
async def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest_asyncio.fixture
async def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)
