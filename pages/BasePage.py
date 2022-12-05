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
        self.find_elements = driver.find_elements

    def is_element_displayed(self, locator):
        """ Проверяем видимость элемента по его локатору """
        try:
            WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator), message=f'не вижу {locator}')
        except TimeoutException:
            return False
        return True

    def check_url(self, url):
        """ Сравниваем текущий URL с входящим в функцию"""
        return WebDriverWait(self, 10).until(exp_cond.url_to_be(url), message=f'{url}, неправильный')

    def is_element_present(self, locator):
        """ Проверяем наличие элемента в DOM по его локатору"""
        try:
            WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @staticmethod
    def location_of_element(element: WebElement):
        """ Возвращаем координаты элемента на странице """
        return element.location

    def return_element(self, locator) -> WebElement:
        """ Возвращаем WebElement """
        return WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator))

    def scroll_to_elem(self, element):
        """ Скролл при помощи Java к элементу"""
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def navigate_to(self, locator):
        """ Скролл при помощи Java к элементу по его локатору"""
        element = WebDriverWait(self, 10).until(exp_cond.visibility_of_element_located(locator))
        return self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_clickable(self, locator):
        """ Проверяем кликабельность элемента"""
        try:
            WebDriverWait(self, 10).until(exp_cond.element_to_be_clickable(locator))
        except NoSuchElementException:
            return False
        return True

    def check_element_attribute(self, locator, attribute):
        """ Проверяем нужный аттрибут у элемента"""
        element = WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        element_attribute = element.get_property(f'{attribute}')
        if element_attribute == attribute:
            return True
        else:
            return False

    def is_elements_displayed(self, locator):
        """ Ожидаем загрузку всех элементов"""
        try:
            WebDriverWait(self, 10).until(exp_cond.visibility_of_all_elements_located(locator))
        except TimeoutException:
            return False
        return True

    def click(self, element):
        """ Кликаем Java по элементу"""
        return self.driver.execute_script("arguments[0].click();", element)





