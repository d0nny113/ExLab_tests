from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.timeout = 30
        self.find_element = driver.find_element

    def wait_until_clickable(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 5).until(exp_cond.element_to_be_clickable(locator))

    def image_check(self, locator):
        return WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(locator))

    def is_element_displayed(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator), message=f'не вижу {locator}')
        except TimeoutException:
            return False
        return True

    def check_url(self, url):
        return WebDriverWait(self, 10).until(exp_cond.url_to_be(url), message=f'{url}, неправильный')

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

    def return_element(self, locator) -> WebElement:
        element = WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator))
        return element

    def scroll_to_elem(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def navigate_to(self, locator):
        element = WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator))
        return self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_clickable(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return True

    def is_elements_displayed(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.visibility_of_all_elements_located(locator))
        except TimeoutException:
            return False
        return True

    def click(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def waiting_page(self):
        return WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script
                                                    ('return document.readyState') == 'complete')



