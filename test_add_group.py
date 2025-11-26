
from playwright.sync_api import Playwright, sync_playwright, expect
from group import Group
from application import Application
import time, unittest
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # ---------------------
    context.close()
    browser.close()

def login_lks(app):
    self.app.login(username='Guskov-AV', passwd='Kotopes1')

with sync_playwright() as playwright:
    run(playwright)

