import time


import pytest
import allure
from allure_commons.types import AttachmentType
import urllib.request
from pages.LandingPage import LandingPage
from PIL import Image


class TestLanding:

    @pytest.fixture()
    def landing_page(self, browser):
        landing_page = LandingPage(browser)

        yield landing_page

    @allure.feature("БИГ СМОУК")
    def test_smoke(self, browser, landing_page):
        with allure.step('Лендинг ExLab доступен по правильному адресу'):
            assert landing_page.check_url(browser.current_url)
        with allure.step('По умолчанию открывается темная тема лендинга'):
            assert landing_page.check_theme() == 'Dark'

    @allure.feature('Header')
    @allure.story('Логотипы')
    def test_logo_header(self, landing_page):
        with allure.step('Отображение логотипа ExLab'):
            assert landing_page.image_check(landing_page.base_locators.LOGO_PIC_EXLAB)

    @allure.feature('Header')
    @allure.story('Линки в header')
    def test_link_o_nas(self, landing_page):
        href_link = landing_page.base_locators.LANDING_LINK + '#about'
        landing_page.find_element(*landing_page.header_locators.link_o_nas).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='link_o_nas', attachment_type=AttachmentType.JPG)
        with allure.step('Ссылка О нас ведет на экран с заголовком О нас'):
            assert landing_page.check_link_href(landing_page.header_locators.link_o_nas, href_link)
        with allure.step('Ссылка О нас отображается'):
            assert landing_page.is_element_displayed(landing_page.header_locators.link_o_nas)
        with allure.step('Ссылка О нас кликабельна'):
            assert landing_page.is_element_clickable(landing_page.header_locators.link_o_nas)

    @allure.feature('Header')
    @allure.story('Линки в header')
    def test_link_project(self, landing_page):
        href_link = landing_page.base_locators.LANDING_LINK + '#projects'
        landing_page.find_element(*landing_page.header_locators.link_projects).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='link_project', attachment_type=AttachmentType.JPG)
        with allure.step('Ссылка Проекты ведет на экран с заголовком Проекты'):
            assert landing_page.check_link_href(landing_page.header_locators.link_projects, href_link)
        with allure.step('Ссылка Проекты отображается'):
            assert landing_page.is_element_displayed(landing_page.header_locators.link_projects)
        with allure.step('Ссылка Проекты кликабельна'):
            assert landing_page.is_element_clickable(landing_page.header_locators.link_projects)

    @allure.feature('Header')
    @allure.story('Линки в header')
    def test_link_mentors(self, landing_page):
        href_link = landing_page.base_locators.LANDING_LINK + '#mentors'
        landing_page.find_element(*landing_page.header_locators.link_mentors).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='link_mentors', attachment_type=AttachmentType.JPG)
        with allure.step('Ссылка Менторы отображается'):
            assert landing_page.is_element_displayed(landing_page.header_locators.link_mentors)
        with allure.step('Ссылка Менторы кликабельна'):
            assert landing_page.is_element_clickable(landing_page.header_locators.link_mentors)
        with allure.step('Ссылка Менторы ведет на экран с заголовком Менторы'):
            assert landing_page.check_link_href(landing_page.header_locators.link_mentors, href_link)

    @allure.feature('Header')
    @allure.story('Линки в header')
    def test_link_startup(self, landing_page):
        href_link = landing_page.base_locators.LANDING_LINK + '#startup'
        landing_page.find_element(*landing_page.header_locators.link_startup).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='link_startup', attachment_type=AttachmentType.JPG)
        with allure.step('Ссылка StartUP ведет на экран с заголовком StartUp для'):
            assert landing_page.check_link_href(landing_page.header_locators.link_startup, href_link)
        with allure.step('Ссылка StartUP отображается'):
            assert landing_page.is_element_displayed(landing_page.header_locators.link_startup)
        with allure.step('Ссылка StartUP кликабельна'):
            assert landing_page.is_element_clickable(landing_page.header_locators.link_startup)

    @allure.feature('Header')
    @allure.story('Кнопки')
    def test_theme_color_button(self, landing_page):
        landing_page.find_element(*landing_page.header_locators.button_theme).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='button_theme', attachment_type=AttachmentType.JPG)
        with allure.step('Проверка отображения кнопки переключения темы пользовательского интерфейса Sun Icon'):
            assert landing_page.is_element_displayed(landing_page.header_locators.button_theme)
        with allure.step('При нажатии на переключатель, тема сайта меняется на светлую'):
            landing_page.wait_until_clickable(landing_page.header_locators.button_theme).click()
            assert landing_page.check_theme() == 'Light'

    @allure.feature('Падающие тесты без функционала')
    @pytest.mark.xfail   # ПАДАЮЩИЙ ТЕСТ, ФУНКЦИОНАЛ НЕ ЗАВЕЗЛИ
    def test_what_test(self, browser):
        landing_page = LandingPage(browser)

    @allure.feature('Header')
    @allure.story("Кнопки", 'Переход на сторонний ресурс')
    def test_join_button(self, browser, landing_page):   # нужно поправить для FireFox
        href = 'https://t.me/ExLab_registration_bot'
        landing_page.find_element(*landing_page.header_locators.button_join).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='button_join', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение кнопки [Присоединиться] в шапке сайта'):
            assert landing_page.is_element_displayed(landing_page.header_locators.button_join)
        with allure.step('Кнопка кликабельна'):
            assert landing_page.is_element_clickable(landing_page.header_locators.button_join)
        with allure.step('При нажатии на кнопку [Присоединиться] в шапке сайта открывается форма регистрации'):
            landing_page.wait_until_clickable(landing_page.header_locators.button_join).click()
            browser.switch_to.window(browser.window_handles[1])
            assert browser.current_url == href

    @allure.feature("Header")
    @allure.story("Линки в header")
    def test_link_position(self, landing_page):
        q = landing_page.return_element(landing_page.header_locators.link_o_nas).location['y']
        w = landing_page.return_element(landing_page.header_locators.link_startup).location['y']
        e = landing_page.return_element(landing_page.header_locators.link_mentors).location['y']
        r = landing_page.return_element(landing_page.header_locators.link_projects).location['y']
        with allure.step('О нас, Проекты, Менторы, StartUp для,  находятся на одной линии'):
            assert q == w == e == r

    @allure.feature('Блоки лендинга')
    @allure.story("Логотипы")
    def test_logo_opportunity_block(self, landing_page):
        time.sleep(15)  # ждем загрузки лого
        landing_page.image_check(landing_page.opportunity_locators.logo_exlab).screenshot('temp.jpg')
        with allure.step('Отображение логотипа  ExLab в блоке "Твоя возможность"'):
            assert landing_page.is_element_displayed(landing_page.opportunity_locators.logo_exlab)
            allure.attach.file('temp.jpg', name='logo', attachment_type=AttachmentType.JPG)

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки', 'Текст в блоке')
    def test_opportunity_block(self, landing_page):
        landing_page.find_element(*landing_page.opportunity_locators.header_opportunity).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='opportunity_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение надписи Твоя возможность'):
            assert landing_page.is_element_displayed(landing_page.opportunity_locators.header_opportunity)
        landing_page.find_element(*landing_page.opportunity_locators.text_opportunity).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='opportunity_text', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение текста под надписью Твоя возможность'):
            assert landing_page.is_element_displayed(landing_page.opportunity_locators.text_opportunity)

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки', 'Текст в блоке')
    def test_o_nas_block(self, browser, landing_page):
        browser.find_element(*landing_page.about_us_locators.header_o_nas).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='o_nas_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение надписи О нас'):
            assert landing_page.is_element_displayed(landing_page.about_us_locators.header_o_nas)
        browser.find_element(*landing_page.about_us_locators.text_o_nas).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='o_nas_text', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение текста под надписью О нас'):
            assert landing_page.is_element_displayed(landing_page.about_us_locators.text_o_nas)

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки', 'Текст в блоке')
    def test_why_exlab_block(self, landing_page):
        landing_page.find_element(*landing_page.about_us_locators.why_exlab_header).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='why_ex_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение надписи "Почему ExLab?" '):
            assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_header)
        texts = landing_page.find_elements(*landing_page.about_us_locators.why_exlab_text)
        for text in texts:
            text.screenshot('temp.jpg')
            allure.attach.file('temp.jpg', name='why_ex_text', attachment_type=AttachmentType.JPG)
            with allure.step('Отображение текста под надписью "Почему ExLab?" '):
                assert text.is_displayed()

    @allure.feature('Блоки лендинга')
    @allure.story("Кнопки", 'Переход на сторонний ресурс')
    def test_why_exlab_button_join(self, browser, landing_page):
        href = 'https://t.me/ExLab_registration_bot'
        landing_page.find_element(*landing_page.about_us_locators.why_exlab_join_button).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='why_ex_butt', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение кнопки [Присоединиться] в разделе "Почему ExLab?" '):
            assert landing_page.is_element_displayed(landing_page.about_us_locators.why_exlab_join_button)
        with allure.step('Кнопка кликабельна'):
            assert landing_page.is_element_clickable(landing_page.about_us_locators.why_exlab_join_button)
        landing_page.wait_until_clickable(landing_page.about_us_locators.why_exlab_join_button).click()
        browser.switch_to.window(browser.window_handles[1])
        with allure.step('При нажатии на кнопку [Присоединиться] открывается форма регистрации'):
            assert browser.current_url == href

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки')
    def test_project_block_header(self, landing_page):
        landing_page.find_element(*landing_page.project_locators.header_projects).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='project_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение надписи Проекты'):
            assert landing_page.is_element_displayed(landing_page.project_locators.header_projects)

    @allure.feature('Блоки лендинга')
    @allure.story('Логотипы', 'Текст в блоке')
    def test_project_block_logo_and_text(self, landing_page, browser):
        logos = landing_page.find_elements(*landing_page.project_locators.logo_projects_pics)
        for logo in logos:
            browser.implicitly_wait(1)
            logo.screenshot('temp.jpg')

            img = urllib.request.urlopen(logo.get_attribute('src')).read()
            out = open("logo.jpg", "wb")
            out.write(img)
            allure.attach.file('logo.jpg', name='project_logo', attachment_type=AttachmentType.JPG)
            with allure.step('Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке'):
                assert logo.is_displayed()
        texts = landing_page.find_elements(*landing_page.project_locators.projects_text)
        for text in texts:
            text.screenshot('temp.jpg')
            allure.attach.file('temp.jpg', name='project_text', attachment_type=AttachmentType.JPG)
            with allure.step('Отображение текста в описании проекта ExLab, HealthyLife, Easyhelp'):
                assert text.is_displayed()

    @allure.feature('Блоки лендинга')
    @allure.story("Выпадающие страницы менторов")
    def test_mentors_cards(self, landing_page, browser):  # тест не доделан, кнопка никуда не ведет!!
        href = landing_page.base_locators.LANDING_LINK + '#'
        mentors_card = landing_page.find_elements(*landing_page.mentors_locators.mentors_card)
        for mentor in mentors_card:
            mentor.find_element(*landing_page.mentors_locators.mentors_button).screenshot('temp.jpg')
            button = mentor.find_element(*landing_page.mentors_locators.mentors_button)

            landing_page.click(button)

            with allure.step('При нажатии на область ментора (при закрытом спойлере) спойлер открывается'):
                assert button.get_attribute('class').split(' ')[1] == 'gGHWQo'

            mentor.find_element(*landing_page.mentors_locators.mentor_photo).screenshot('temp.jpg')
            with allure.step('Фотография ментора  отображается'):
                assert landing_page.is_element_displayed(landing_page.mentors_locators.mentor_photo)

                img = urllib.request.urlopen(mentor.find_element(*landing_page.mentors_locators.mentor_photo)
                                             .get_attribute('src')).read()
                out = open("img.jpg", "wb")
                out.write(img)
                mentor_photo = Image.open('img.jpg')
                mentor_photo.resize((220, 260))
                mentor_photo.save('img.jpg')
                allure.attach.file('img.jpg', name='mentor_photo', attachment_type=AttachmentType.JPG)
            mentor.find_element(*landing_page.mentors_locators.mentor_text_box).screenshot('temp.jpg')
            texts = mentor.find_elements(*landing_page.mentors_locators.mentor_text)
            with allure.step('При открытом спойлере отображается информации о менторе'):
                for text in texts:
                    text.screenshot('temp.jpg')
                    allure.attach.file('temp.jpg', name='mentor_text', attachment_type=AttachmentType.JPG)
                    assert text.is_displayed()
            mentor.find_element(*landing_page.mentors_locators.mentors_button).screenshot('temp.jpg')
            landing_page.click(button)
            with allure.step('При нажатии на область ментора (при развернутом спойлере) спойлер закрывается'):
                assert button.get_attribute('class').split(' ')[1] == 'cFcyNJ'
        landing_page.find_element(*landing_page.mentors_locators.stand_mentors_but).screenshot('temp.jpg')
        with allure.step('Кнопка "Стать ментором" ????? '):
            assert landing_page.check_link_href(landing_page.mentors_locators.stand_mentors_but, href)

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки', 'Текст в блоке', 'Кнопки')
    def test_startup_block(self, landing_page):   # тест не доделан, кнопка никуда не ведет!!
        href = landing_page.base_locators.LANDING_LINK + '#'
        landing_page.find_element(*landing_page.start_up_locators.header).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='start_up_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение заголовка StartUp для'):
            assert landing_page.is_element_displayed(landing_page.start_up_locators.header)
        texts_jun = landing_page.find_elements(*landing_page.start_up_locators.text_juniors)
        text_hr = landing_page.find_elements(*landing_page.start_up_locators.text_hr)
        for text in texts_jun:
            text.screenshot('temp.jpg')
            allure.attach.file('temp.jpg', name='text_jun', attachment_type=AttachmentType.JPG)
            with allure.step('Отображение текста Juniors'):
                assert text.is_displayed()
        for text in text_hr:
            text.screenshot('temp.jpg')
            allure.attach.file('temp.jpg', name='text_rec', attachment_type=AttachmentType.JPG)
            with allure.step('Отображение текста в рекрутеров'):
                assert text.is_displayed()
        landing_page.find_element(*landing_page.start_up_locators.find_specialist_but).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='find_spec_but', attachment_type=AttachmentType.JPG)
        with allure.step('Кнопка "Найти специалиста" ???????? '):
            assert landing_page.check_link_href(landing_page.start_up_locators.find_specialist_but, href)

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки', 'Текст в блоке')
    def test_help_project_block(self, landing_page):
        landing_page.find_element(*landing_page.help_project_locators.header).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='help_proj_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение заголовка Помочь проекту'):
            assert landing_page.is_element_displayed(landing_page.help_project_locators.header)
        texts = landing_page.find_elements(*landing_page.help_project_locators.text)
        for text in texts:
            text.screenshot('temp.jpg')
            allure.attach.file('temp.jpg', name='help_proj_text', attachment_type=AttachmentType.JPG)
            with allure.step('Отображение текста в блоке'):
                assert text.is_displayed()

    @allure.feature('Блоки лендинга')
    @allure.story("Кнопки", 'Переход на сторонний ресурс')
    def test_button_boosty(self, browser, landing_page):
        href = 'https://boosty.to/exlab_startup'
        landing_page.find_element(*landing_page.help_project_locators.link_boosty).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='boosty_but', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение кнопки [Boosty]'):
            assert landing_page.is_element_displayed(landing_page.help_project_locators.link_boosty)
        button = landing_page.return_element(landing_page.help_project_locators.link_boosty)
        landing_page.click(button)
        browser.switch_to.window(browser.window_handles[1])
        with allure.step('При нажатии на кнопку  [Boosty] открывается страница ExLab на сайте Boosty'):
            assert browser.current_url == href

    @allure.feature('Блоки лендинга')
    @allure.story('Заголовки', 'Текст в блоке')
    def test_stay_tune_block(self, landing_page):
        landing_page.find_element(*landing_page.stay_connected.header).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='stay_tune_head', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение надписи Оставайся на связи'):
            assert landing_page.is_element_displayed(landing_page.stay_connected.header)
        landing_page.find_element(*landing_page.stay_connected.text).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='stay_tune_text', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение текста в блоке '):
            assert landing_page.is_element_displayed(landing_page.stay_connected.text)

    @allure.feature('Footer')
    @allure.story('Логотипы', 'Текст в блоке')
    def test_logo_footer(self, landing_page):
        landing_page.find_element(*landing_page.footer_locators.footer_logo).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='logo_footer', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение логотипа ExLab'):
            assert landing_page.is_element_displayed(landing_page.footer_locators.footer_logo)
        landing_page.find_element(*landing_page.footer_locators.footer_text_under_logo).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='text_under_logo', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение текста под логотипом ExLab'):
            assert landing_page.is_element_displayed(landing_page.footer_locators.footer_text_under_logo)

    @allure.feature('Footer')
    @allure.story("Линки в footer", 'Переход на сторонний ресурс')
    def test_link_linkedin(self, browser, landing_page):  # нужно доделать, тест проверяет только переход в LinkdIn
        href = 'https://www.linkedin.com/company/exlab-start-up'
        landing_page.find_element(*landing_page.footer_locators.link_lnkdn).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='linkd_link', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение ссылки LNKDN'):
            assert landing_page.is_element_displayed(landing_page.footer_locators.link_lnkdn)
        landing_page.click_footer_link('LNKDN')
        browser.switch_to.window(browser.window_handles[1])
        with allure.step('При нажатии попадаем на  LinkedIn'):
            assert browser.current_url.startswith('https://www.linkedin.com/')

    @allure.feature('Footer')
    @allure.story("Линки в footer", 'Переход на сторонний ресурс')
    def test_link_instagram(self, browser, landing_page):
        href = 'https://www.instagram.com/exlab_startup/'
        landing_page.find_element(*landing_page.footer_locators.link_instgrm).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='instgrm_link', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение ссылки INSTGRM'):
            assert landing_page.is_element_displayed(landing_page.footer_locators.link_instgrm)
        landing_page.click_footer_link('INSTGRM')
        browser.switch_to.window(browser.window_handles[1])
        with allure.step('При нажатии попадаем на страницу ExLab в Instagram'):
            assert browser.current_url == href

    @allure.feature('Footer')
    @allure.story("Линки в footer", 'Переход на сторонний ресурс')
    def test_link_telegram(self, browser, landing_page):
        href = 'https://t.me/ExLabChannel'
        landing_page.find_element(*landing_page.footer_locators.link_tlgrm).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='tlgrm_link', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение ссылки TLGRM'):
            assert landing_page.is_element_displayed(landing_page.footer_locators.link_tlgrm)
        landing_page.click_footer_link('TLGRM')
        browser.switch_to.window(browser.window_handles[1])
        with allure.step('При нажатии попадаем на страницу ExLab в Telegram'):
            assert browser.current_url == href

    @allure.feature('Footer')
    @allure.story("Линки в footer", 'Переход на сторонний ресурс')
    def test_link_youtube(self, browser, landing_page):
        href = 'https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA'
        landing_page.find_element(*landing_page.footer_locators.link_ytb).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='ytb_link', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение ссылки YTB'):
            assert landing_page.is_element_displayed(landing_page.footer_locators.link_ytb)
        landing_page.click_footer_link('YTB')
        browser.switch_to.window(browser.window_handles[1])
        with allure.step('При нажатии попадаем на страницу ExLab в Youtube'):
            assert browser.current_url == href

    @allure.feature('Footer')
    @allure.story("Линки в footer")
    def test_link_mail_to(self, landing_page):
        landing_page.find_element(*landing_page.footer_locators.mailto).screenshot('temp.jpg')
        allure.attach.file('temp.jpg', name='mail_to_link', attachment_type=AttachmentType.JPG)
        with allure.step('Отображение ссылки info@exlab.team'):
            assert(landing_page.is_element_displayed(landing_page.footer_locators.mailto))



























