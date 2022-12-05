import time
import pytest
from pages.LandingPage import LandingPage


class TestLanding:
    @pytest.fixture()
    def landing_page(self, browser):
        landing_page = LandingPage(browser)
        yield landing_page

    def test_test(self, landing_page):
        landing_page.navigate_to_switch_theme()
        landing_page.click_header_links('О нас')
        landing_page.click_join_button_header()
        time.sleep(3)




















