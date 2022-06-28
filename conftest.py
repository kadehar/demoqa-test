from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def open_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')