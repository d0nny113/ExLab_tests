import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        self.timeout = 30
        self.find_element = driver.find_element

    def wait_until_clickable(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 5).until(exp_cond.element_to_be_clickable(locator))

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

    def check_link_href(self, locator, href):
        element = WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        element_href = element.get_property('href')
        if element_href == href:
            return True
        else:
            return False

    def is_elements_displayed(self, locator):
        try:
            WebDriverWait(self, 10).until(exp_cond.presence_of_all_elements_located(locator))
        except TimeoutException:
            return False
        return True

    def find_elem(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, 10).until(self.driver.find_elements(locator))

    def what_about_color(self, color: str):
        removed_chars = ['(', ',', ')', 'r', 'g', 'b', 'a']
        chars = set(removed_chars)
        color = ''.join(c for c in color if c not in chars)
        res = list(color.split(' '))
        r, g, b = res[0], res[1], res[2]
        answer = [r, g, b]
        return answer

    def click(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def wait_load_wind(self):
        return WebDriverWait(self.driver, 5).until(exp_cond.new_window_is_opened(self.driver.window_handles))

    def alert(self):
        if WebDriverWait(self.driver, 5).until(exp_cond.alert_is_present()):
            return True
        else:
            return False

    def element_text(self, how, what):
        elements = self.driver.find_elements(how, what)
        print(f'Количество элементов {len(elements)} \n')
        elm_count = 1
        for element in elements:
            if element.text:
                print(f'успешно проверен {elm_count} элемент, внутри тега {element.tag_name} есть текст \n')
            elm_count += 1
        else:
            print(f'внутри {elm_count} текста нет')


