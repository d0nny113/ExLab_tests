from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self, url):
        self.driver.get(url)

    def is_element_clickable(self, element):  # Проверяем что элемент виден и активен, поэтому можно кликнуть на него
        try:
            WebDriverWait(self, 50).until(EC.element_to_be_clickable(element))
        except NoSuchElementException:
            return False
        return True

    def is_element_contains(self, locator, attribute):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_attribute_to_include((locator, attribute)))
        except NoSuchElementException:
            return False
        return True

    def is_element_present(self, locator):
        try:
            WebDriverWait(self, 10).until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            return False
        return True

    def is_element_displayed(self, element):
        try:
            WebDriverWait(self, 10).until(EC.visibility_of(element))
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            WebDriverWait(self, 10).until(EC.alert_is_present())
        except NoSuchElementException:
            return False
        return True
