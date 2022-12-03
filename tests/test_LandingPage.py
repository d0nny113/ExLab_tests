import time
import pytest
from pages.LandingPage import LandingPage


class TestLanding:

    def test1(self, browser, time_delta):
        landing_page = LandingPage(browser)
        assert landing_page.check_url(browser.current_url), \
            ' ↑ Лендинг ExLab доступен по адресу http://test.exlab.team/'
        assert landing_page.check_theme() == 'Dark', \
            ' ↑ По умолчанию открывается темная тема лендинга'

    def test2(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.base_locators.LOGO_PIC_EXLAB), \
            ' ↑ Отображение логотипа ExLab'

    def test3(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#about'
        assert landing_page.check_link_href(landing_page.header_locators.link_o_nas, href_link), \
            ' ↑ Ссылка О нас ведет на экран с заголовком О нас'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_o_nas),  \
            ' ↑ Ссылка О нас отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_o_nas), \
            ' ↑ Ссылка О нас кликабельна'

    def test4(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#projects'
        assert landing_page.check_link_href(landing_page.header_locators.link_projects, href_link), \
            ' ↑ Ссылка Проекты ведет на экран с заголовком Проекты'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_projects),  \
            ' ↑ Ссылка Проекты отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_projects),  \
            ' ↑ Ссылка Проекты кликабельна'

    def test5(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#mentors'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_mentors), \
            ' ↑ Ссылка Менторы отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_mentors), \
            ' ↑ Ссылка Менторы кликабельна'
        assert landing_page.check_link_href(landing_page.header_locators.link_mentors, href_link), \
            ' ↑ Ссылка Менторы ведет на экран с заголовком Менторы'

    def test6(self, browser):
        landing_page = LandingPage(browser)
        href_link = landing_page.base_locators.LANDING_LINK + '#startup'
        assert landing_page.check_link_href(landing_page.header_locators.link_startup, href_link), \
            ' ↑ Ссылка StartUP ведет на экран с заголовком StartUp для'
        assert landing_page.is_element_displayed(landing_page.header_locators.link_startup), \
            ' ↑ Ссылка StartUP отображается'
        assert landing_page.is_element_clickable(landing_page.header_locators.link_startup), \
            ' ↑ Ссылка StartUP кликабельна'

    def test7(self, browser):
        landing_page = LandingPage(browser)
        assert landing_page.is_element_displayed(landing_page.header_locators.button_theme), \
            ' ↑ Проверка отображения кнопки переключения темы пользовательского интерфейса Sun Icon'
        landing_page.wait_until_clickable(landing_page.header_locators.button_theme).click()
        assert landing_page.check_theme() == 'Light', \
            ' ↑ При нажатии на переключатель, тема сайта меняется на светлую'

    @pytest.mark.xfail   # ПАДАЮЩИЙ ТЕСТ, ФУНКЦИОНАЛ НЕ ЗАВЕЗЛИ
    def test8(self, browser):
        landing_page = LandingPage(browser)

    def test9(self, browser):   # нужно поправить для FireFox
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
        browser.find_element(*landing_page.opportunity_locators.logo_exlab).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.opportunity_locators.logo_exlab), \
            ' ↑ Отображение логотипа  ExLab в блоке "Твоя возможность"'

    def test12(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.opportunity_locators.header_opportunity).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.opportunity_locators.header_opportunity), \
            ' ↑ Отображение надписи Твоя возможность'
        browser.find_element(*landing_page.opportunity_locators.text_opportunity).screenshot('124.jpg')
        assert landing_page.is_element_displayed(landing_page.opportunity_locators.text_opportunity), \
            ' ↑ Отображение текста под надписью Твоя возможность'

    def test13(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.about_us_locators.header_o_nas).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.about_us_locators.header_o_nas), \
            ' ↑ Отображение надписи О нас'
        browser.find_element(*landing_page.about_us_locators.text_o_nas).screenshot('124.jpg')
        assert landing_page.is_element_displayed(landing_page.about_us_locators.text_o_nas), \
            ' ↑ Отображение текста под надписью О нас'

    def test14(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.about_us_locators.why_exlab_header).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_header), \
            ' ↑ Отображение надписи Почему ExLab?'
        browser.find_element(*landing_page.about_us_locators.why_exlab_text).screenshot('124.jpg')
        assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_text), \
            ' ↑ Отображение текста под надписью Почему ExLab?'

    def test15(self, browser):
        landing_page = LandingPage(browser)
        href = 'https://t.me/ExLab_registration_bot'
        browser.find_element(*landing_page.about_us_locators.why_exlab_join_button).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_join_button), \
            ' ↑ Отображение кнопки [Присоединиться]'
        assert landing_page.is_element_clickable(landing_page.about_us_locators.why_exlab_join_button), \
            ' ↑ Кнопка кликабельна'
        landing_page.wait_until_clickable(landing_page.about_us_locators.why_exlab_join_button).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, 'При нажатии на кнопку [Присоединиться] открывается форма регистрации'

    def test16(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.project_locators.header_projects).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.project_locators.header_projects), \
            ' ↑ Отображение надписи Проекты'

    def test17(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.project_locators.logo_projects_pics).screenshot('123.jpg')
        assert landing_page.is_elements_displayed(landing_page.project_locators.logo_projects_pics), \
            ' ↑ Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке'
        browser.find_element(*landing_page.project_locators.projects_text).screenshot('124.jpg')
        assert landing_page.is_elements_displayed(landing_page.project_locators.projects_text), \
            ' ↑ Отображение текста в описании проекта ExLab, HealthyLife, Easyhelp'

    def test18(self, browser, time_delta):
        landing_page = LandingPage(browser)
        mentors_card = browser.find_elements(*landing_page.mentors_locators.mentors_card)
        for mentor in mentors_card:
            button = mentor.find_element(*landing_page.mentors_locators.mentors_button)
            landing_page.click(button)
            assert button.get_attribute('class').split(' ')[1] == 'gGHWQo', \
                ' ↑ При нажатии на область ментора (при закрытом спойлере) спойлер открывается'
            browser.find_element(*landing_page.mentors_locators.mentor_photo).screenshot('123.jpg')
            assert landing_page.is_element_displayed(landing_page.mentors_locators.mentor_photo), \
                ' ↑  Фотография ментора  отображается'
            browser.find_element(*landing_page.mentors_locators.mentor_text).screenshot('124.jpg')
            assert landing_page.is_element_displayed(landing_page.mentors_locators.mentor_text), \
                ' ↑ При открытом спойлере отображается информации о менторе '
            landing_page.click(button)
            assert button.get_attribute('class').split(' ')[1] == 'cFcyNJ', \
                ' ↑ При нажатии на область ментора (при развернутом спойлере) спойлер закрывается'

    def test19(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.start_up_locators.header).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.start_up_locators.header), \
               '↑ Отображение заголовка StartUp для'
        browser.find_element(*landing_page.start_up_locators.text).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.start_up_locators.text), \
               '↑ Отображение текста в блоке'

    def test20(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.help_project_locators.header).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.help_project_locators.header), \
               '↑ Отображение заголовка Помочь проекту'
        browser.find_elements(*landing_page.help_project_locators.text)
        assert landing_page.is_elements_displayed(landing_page.help_project_locators.text), \
               '↑ Отображение текста в блоке'

    def test21(self, browser):
        href = 'https://boosty.to/exlab_startup'
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.help_project_locators.link_boosty).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.help_project_locators.link_boosty), \
               '↑ Отображение кнопки [Boosty]'
        button = landing_page.return_element(landing_page.help_project_locators.link_boosty)
        landing_page.click(button)
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, \
            'При нажатии на кнопку  [Boosty] открывается страница ExLab на сайте Boosty'

    def test22(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.stay_connected.header).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.stay_connected.header), \
               '↑ Отображение надписи Оставайся на связи'
        browser.find_element(*landing_page.stay_connected.text).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.stay_connected.text), \
            '↑ Отображение текста в блоке '

    def test23(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.footer_locators.footer_logo).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.footer_logo), \
            '↑ Отображение логотипа ExLab'
        browser.find_element(*landing_page.footer_locators.footer_text_under_logo).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.footer_text_under_logo), \
            '↑ Отображение текста под логотипом ExLab'

    def test24(self, browser):  # идет редирект на вход, тест падает нужно доделать
        href = 'https://www.linkedin.com/company/exlab-start-up'
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.footer_locators.link_lnkdn).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.link_lnkdn), \
            '↑ Отображение ссылки LNKDN'
        landing_page.click_footer_link('LNKDN')
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(3)
        assert browser.current_url.startswith('https://www.linkedin.com/'), \
            '↑ При нажатии попадаем на  LinkedIn'

    def test25(self, browser):
        href = 'https://www.instagram.com/exlab_startup/'
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.footer_locators.link_instgrm).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.link_instgrm), \
            '↑ Отображение ссылки INSTGRM'
        landing_page.click_footer_link('INSTGRM')
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, \
            '↑ При нажатии попадаем на страницу ExLab в Instagram'

    def test26(self, browser):
        href = 'https://t.me/ExLabChannel'
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.footer_locators.link_tlgrm).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.link_tlgrm), \
            '↑ Отображение ссылки TLGRM'
        landing_page.click_footer_link('TLGRM')
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, \
            '↑ При нажатии попадаем на страницу ExLab в Telegram'

    def test27(self, browser):
        href = 'https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA'
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.footer_locators.link_ytb).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.link_ytb), \
            '↑ Отображение ссылки YTB'
        landing_page.click_footer_link('YTB')
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == href, \
            '↑ При нажатии попадаем на страницу ExLab в Youtube'

    def test28(self, browser):
        landing_page = LandingPage(browser)
        browser.find_element(*landing_page.footer_locators.mailto).screenshot('123.jpg')
        assert landing_page.is_element_displayed(landing_page.footer_locators.mailto), \
            '↑ Отображение ссылки info@exlab.team '






















