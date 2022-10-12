from pages.BasePage import BasePage
from pages.Locators import BaseLocators, LPLD
from selenium.common import NoSuchElementException


class LandingPageDark(BasePage):

    def __init__(self, driver):
        super().__init__(driver, BaseLocators.LANDING_LINK)
        self.driver.get(BaseLocators.LANDING_LINK)
        self.o_nas_link = driver.find_element(*LPLD.link_o_nas)
        self.project_link = driver.find_element(*LPLD.link_projects)
        self.mentors_link = driver.find_element(*LPLD.link_mentors)
        self.theme_btn = driver.find_element(*LPLD.button_theme)
        self.theme = driver.find_element(*BaseLocators.DARK_THEME)
        self.startUP_link = driver.find_element(*LPLD.link_startup)
        self.join_btn = driver.find_element(*LPLD.button_join)
        # self.eng_btn = driver.find_element(*LPLD.english_lang)
        self.logo = driver.find_element(*BaseLocators.LOGO_PIC_EXLAB)
        self.razdel_o_nas = driver.find_element(*LPLD.razdel_o_nas)
        # self.razdel_projects = driver.find_element(*LPLD.razdel_projects)










