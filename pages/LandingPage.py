from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond
from pages.BasePage import BasePage
from locators.Locators import BaseLocators, HeaderDark, OpportunityDark, HeaderLight, HelpProjectDark
from locators.Locators import AboutUsDark, ProjectsDark, MentorsDark, FooterDark, StartUpForDark, StayConnectedDark


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, BaseLocators.LANDING_LINK)
        self.driver.get(BaseLocators.LANDING_LINK)
        self.current_url = driver.current_url
        self.find_element = driver.find_element
        self.find_elements = driver.find_elements
        self.execute_script = driver.execute_script
        self.base_locators = BaseLocators
        self.header_locators = HeaderDark
        self.opportunity_locators = OpportunityDark
        self.about_us_locators = AboutUsDark
        self.project_locators = ProjectsDark
        self.mentors_locators = MentorsDark
        self.start_up_locators = StartUpForDark
        self.help_project_locators = HelpProjectDark
        self.footer_locators = FooterDark
        self.stay_connected = StayConnectedDark

    def click_join_button_header(self):
        """ Метод возвращает нажатие на кнопку присоединиться в шапке сайта """
        return self.find_element(*HeaderDark.button_join).click()

    def navigate_to_switch_theme(self):
        """ Метод возвращает нажатие на икноку переключения темы  """
        return self.find_element(*BaseLocators.button_theme).click()

    def check_theme(self):
        """ Метод возвращает проверку цвета темы лендинга """
        theme = self.find_element(*BaseLocators.button_theme)
        color = theme.find_element(By.CSS_SELECTOR, 'div')
        if color.get_attribute('class') == BaseLocators.light_theme:
            return 'Light'
        elif color.get_attribute('class') == BaseLocators.dark_theme:
            return 'Dark'
        else:
            return 'locator Error'

    def click_join_button_why_exlab(self):
        """ Метод возвращает нажатие на кнопку присоединиться в разделе О нас """
        return self.find_element(*AboutUsDark.why_exlab_join_button).click()

    def click_footer_link(self, link_name):
        """ Метод возвращает нажатие на линк в подвале сайта если он есть
                и возвращает ошибку с текстом если ссылки с таким именем нет   """
        footer_links = self.driver.find_elements(*FooterDark.footer_links)
        if not any(i.text == link_name for i in footer_links):
            raise NoSuchElementException('Ссылки с таким именем нет')
        for link in footer_links:
            if link.text == link_name:
                click_link = link.find_element(By.CSS_SELECTOR, 'a')
                self.driver.execute_script("arguments[0].click();", click_link)

    def click_header_links(self, link_name):
        """ Метод возвращает нажатие на линк в шапке сайта если он есть
               и возвращает ошибку с текстом если ссылки с таким именем нет  """
        header_links = self.driver.find_elements(*HeaderDark.link_group)
        if not any(i.text == link_name for i in header_links):
            raise NoSuchElementException('Ссылки с таким именем нет')
        for link in header_links:
            if link_name == link.text:
                link.find_element(By.LINK_TEXT, link_name).click()

    def what_about_color(self, color: str):
        """ Метод цифры цвета R, G, B   """
        removed_chars = ['(', ',', ')', 'r', 'g', 'b', 'a']
        chars = set(removed_chars)
        color = ''.join(c for c in color if c not in chars)
        res = list(color.split(' '))
        r, g, b = res[0], res[1], res[2]
        answer = [r, g, b]
        return answer

    def element_text(self, how, what):  # писал как пример для кого-то и забыл для кого
        """ ?????  """
        elements = self.driver.find_elements(how, what)
        print(f'Количество элементов {len(elements)} \n')
        elm_count = 1
        for element in elements:
            if element.text:
                print(f'успешно проверен {elm_count} элемент, внутри тега {element.tag_name} есть текст \n')
            elm_count += 1
        else:
            print(f'внутри {elm_count} текста нет')

    def check_link_href(self, locator, href):
        """ Метод проверяет аттрибут href у элемента по заданному локатору"""
        element = WebDriverWait(self, 10).until(exp_cond.presence_of_element_located(locator))
        element_href = element.get_property('href')
        if element_href == href:
            return True
        else:
            return False




























