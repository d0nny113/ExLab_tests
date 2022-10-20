from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.timeout = 30

    def wait_until_clickable(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 5).until(exp_cond.element_to_be_clickable(locator))

    def is_element_displayed(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def check_url(self, url):
        return WebDriverWait(self, 10).until(exp_cond.url_to_be(url))

    def is_element_present(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @staticmethod
    def location_of_element(element: WebElement):
        location = element.location
        return location

    def return_element(self, locator):
        element = WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        return element

    def scroll_to(self, locator):
        element = WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        return element.location_once_scrolled_into_view

    def is_element_clickable(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return True

    def check_link_href(self, locator, href):
        element = WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        element_href = element.get_property('href')
        if element_href == href:
            return True
        else:
            return False

    def is_elements_displayed(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.visibility_of_all_elements_located(locator))
        except TimeoutException:
            return False
        return True