import pytest
from pages.Locators import BaseLocators
from pages.LandingPage import LandingPageDark


class TestLanding:

    def test_one(self, browser):
        page = LandingPageDark(browser)
        assert browser.current_url == BaseLocators.LANDING_LINK  # Лендинг ExLab доступен по правильному адресу
        assert page.is_element_clickable(page.theme_btn)
        assert page.theme.get_attribute('class') == BaseLocators.dark_class  # По умолчанию открывается темная тема

    def test_two(self, browser):  # Отображение логотипа ExLab
        page = LandingPageDark(browser)
        assert page.is_element_displayed(page.logo)  # логотип отображается

    def test_three(self, browser):  # Отображение ссылки О нас
        page = LandingPageDark(browser)
        assert page.is_element_clickable(page.o_nas_link)  # - Ссылка кликабельна
        assert page.o_nas_link.get_attribute('data-scroll-to') == "#about"  # - Ссылка ведет на экран О нас

    def test_four(self, browser):  # Отображение ссылки Проекты
        page = LandingPageDark(browser)
        assert page.is_element_clickable(page.project_link)  # - Ссылка кликабельна
        assert page.project_link.get_attribute('data-scroll-to') == "#projects"  # - Ссылка ведет на экран Проекты

    def test_five(self, browser):  # Отображение ссылки Менторы
        page = LandingPageDark(browser)
        assert page.is_element_clickable(page.mentors_link)  # - Ссылка кликабельна
        assert page.mentors_link.get_attribute('data-scroll-to') == "#mentors"  # - Ссылка ведет на экран Менторы

    def test_six(self, browser):  # Отображение ссылки StartUp для
        page = LandingPageDark(browser)
        assert page.is_element_clickable(page.startUP_link) # - Ссылка кликабельна
        assert page.startUP_link.get_attribute('data-scroll-to') == "#startup"  # - Ссылка ведет на экран StartUp для

    def test_seven(self, browser):  # Проверка кнопки переключения темы пользовательского интерфейса
        page = LandingPageDark(browser)
        assert page.is_element_displayed(page.theme_btn)  # Проверка отображения кнопки
        assert page.is_element_clickable(page.theme_btn)
        page.theme_btn.click()
        assert page.theme.get_attribute('class') == BaseLocators.light_class  # При нажатии тема меняется на светлую

    @pytest.mark.xfail
    def test_eight(self, browser):  # Падающий тест, функционал не завезли
        page = LandingPageDark(browser)
        assert page.is_element_displayed(page.eng_btn)  # Проверка отображения кнопки переключения языка

    def test_eleven(self, browser):  # проверка кнопки "Присоединиться"
        page = LandingPageDark(browser)
        assert page.is_element_displayed(page.join_btn)  # Отображение кнопки
        assert page.is_element_clickable(page.join_btn)  # Кнопка кликабельна
        assert page.join_btn.get_attribute('href') == "https://t.me/ExLab_registration_bot"
        page.join_btn.click()
        browser.implicitly_wait(3)
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == "https://t.me/ExLab_registration_bot"  # при нажатии на кнопку открывается форма

    def test_ten(self, browser):   # баловство
        page = LandingPageDark(browser)
        q = page.o_nas_link.location['y']
        w = page.project_link.location['y']
        e = page.mentors_link.location['y']
        r = page.startUP_link.location['y']
        assert q == w == e == r















