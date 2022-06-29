import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10


@pytest.fixture(scope='session', autouse=True)
def open_practice_form(setup):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.execute_script(script="document.querySelector('#app > footer').style.display='none'")
    browser.execute_script(script="document.querySelector('#fixedban').style.display='none'")
