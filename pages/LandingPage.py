from pages.BasePage import BasePage
from locators.Locators import BaseLocators, HeaderDark, OpportunityDark
from locators.Locators import AboutUsDark, ProjectsDark, MentorsDark, FooterDark


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, BaseLocators.LANDING_LINK)
        self.driver.get(BaseLocators.LANDING_LINK)
        self.current_url = driver.current_url
        self.find_element = driver.find_element
        self.find_elements = driver.find_elements
        self.base_locators = BaseLocators
        self.header_locators = HeaderDark
        self.opportunity_locators = OpportunityDark
        self.about_us_locators = AboutUsDark
        self.project_locators = ProjectsDark
        self.mentors_locators = MentorsDark
        self.footer_locators = FooterDark










