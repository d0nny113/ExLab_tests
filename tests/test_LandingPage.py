import pytest
from pages.LandingPage import LandingPage


class TestLanding:

    def test1(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.check_url(browser.current_url), \
            ' ↑ Лендинг ExLab доступен не по адресу http://test.exlab.team/'
        assert landing_page.is_element_present(landing_page.base_locators.DARK_THEME), \
            ' ↑ По умолчанию открывается не темная тема лендинга'

    def test2(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.base_locators.LOGO_PIC_EXLAB), \
            ' ↑ Ошибка отображения логотипа ExLab'

    def test3(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#about'
        assert landing_page.check_link_href(landing_page.header_locators.link_o_nas, href_link), \
            ' ↑ Ссылка не ведет на экран с заголовком О нас'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_o_nas),  \
            ' ↑ Ссылка не отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_o_nas), \
            ' ↑ Ссылка не кликабельна'

    def test4(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#projects'
        assert landing_page.check_link_href(landing_page.header_locators.link_projects, href_link), \
            ' ↑ Ссылка не ведет на экран с заголовком Проекты'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_projects),  \
            ' ↑ Ссылка не отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_projects),  \
            ' ↑ Ссылка не кликабельна'

    def test5(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#mentors'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_mentors), \
            ' ↑ Ссылка не отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_mentors), \
            ' ↑ Ссылка не кликабельна'
        assert landing_page.check_link_href(landing_page.header_locators.link_mentors, href_link), \
            ' ↑ Ссылка не ведет на экран с заголовком Менторы'

    def test6(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#startup'
        assert landing_page.check_link_href(landing_page.header_locators.link_startup, href_link), \
            ' ↑ Ссылка не ведет на экран с заголовком StartUp для'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_startup), \
            ' ↑ Ссылка не отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_startup), \
            ' ↑ Ссылка не кликабельна'

    def test7(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.header_locators.button_theme), \
            ' ↑ Проверка отображения кнопки переключения темы пользовательского интерфейса Sun Icon'
        landing_page.wait_until_clickable(landing_page.header_locators.button_theme).click()
        assert landing_page.is_element_displayed(landing_page.base_locators.LIGHT_THEME), \
            ' ↑ При нажатии на переключатель, тема сайта меняется на светлую'

    @pytest.mark.xfail   # ПАДАЮЩИЙ ТЕСТ, ФУНКЦИОНАЛ НЕ ЗАВЕЗЛИ
    def test8(self, browser):
        landing_page = LandingPage(browser)

    def test9(self, browser):
        landing_page = LandingPage(browser)
        href = 'https://t.me/ExLab_registration_bot'
        assert landing_page.is_element_displayed(landing_page.header_locators.button_join), \
            ' ↑ Отображение кнопки [Присоединиться]'
        assert landing_page.is_element_clickable(landing_page.header_locators.button_join), \
            ' ↑ Кнопка кликабельна'
        landing_page.wait_until_clickable(landing_page.header_locators.button_join).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, 'При нажатии на кнопку [Присоединиться] открывается форма регистрации'

    def test10(self, browser):
        landing_page = LandingPage(browser)
        q = landing_page.return_element(landing_page.header_locators.link_o_nas).location['y']
        w = landing_page.return_element(landing_page.header_locators.link_startup).location['y']
        e = landing_page.return_element(landing_page.header_locators.link_mentors).location['y']
        r = landing_page.return_element(landing_page.header_locators.link_projects).location['y']
        assert q == w == e == r, \
            ' ↑  ссылка О нас, Проекты, Менторы, StartUp для,  находятся на одной линии'

    def test11(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.opportunity_locators.logo_exlab), \
            ' ↑ Отображение логотипа  ExLab в блоке "Твоя возможность"'

    def test12(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.opportunity_locators.header_opportunity), \
            ' ↑ Отображение надписи Твоя возможность'
        assert landing_page.is_element_displayed(landing_page.opportunity_locators.text_opportunity), \
            ' ↑ Отображение текста под надписью Твоя возможность'

    def test13(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.about_us_locators.header_o_nas), \
            ' ↑ Отображение надписи О нас'
        assert landing_page.is_element_displayed(landing_page.about_us_locators.text_o_nas), \
            ' ↑ Отображение текста под надписью О нас'

    def test14(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_header), \
            ' ↑ Отображение надписи Почему ExLab?'
        assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_text), \
            ' ↑ Отображение текста под надписью Почему ExLab?'

    def test15(self, browser):
        landing_page = LandingPage(browser)
        href = 'https://t.me/ExLab_registration_bot'
        assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_join_button), \
            ' ↑ Отображение кнопки [Присоединиться]'
        assert landing_page.is_element_clickable(landing_page.about_us_locators.why_exlab_join_button), \
            ' ↑ Кнопка кликабельна'
        landing_page.wait_until_clickable(landing_page.about_us_locators.why_exlab_join_button).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, 'При нажатии на кнопку [Присоединиться] открывается форма регистрации'

    def test16(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.project_locators.header_projects), \
            ' ↑ Отображение надписи Проекты'

    def test17(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_elements_displayed(landing_page.project_locators.logo_projects_pics), \
            ' ↑ Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке'
        landing_page.scroll_to(landing_page.project_locators.header_projects)
        assert landing_page.is_elements_displayed(landing_page.project_locators.projects_text)















