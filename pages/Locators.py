from selenium.webdriver.common.by import By


class BaseLocators:

    LANDING_LINK = 'http://test.exlab.team/#'
    LOGO_PIC_EXLAB = (By.XPATH, '//div[@id="logo_mobile"]')
    CONTAINER = (By.XPATH, '//div[@id="root"]')
    DARK_THEME = (By.XPATH, '//div[@class="sc-bczRLJ ckyTig"]')
    LIGHT_THEME = (By.XPATH, '//div[@class="sc-bczRLJ cxdoLY"]')
    dark_class = 'sc-bczRLJ ckyTig'
    light_class = 'sc-bczRLJ cxdoLY'


class LPLD:

    menu_group = (By.XPATH, '//div[@class="sc-breuTD eGIhIU"]')
    link_group = (By.XPATH, '//nav[@class="sc-kDDrLX bvKWar"]')

    text_join = (By.XPATH, '//a[@class="sc-dkzDqf gpYSxm" and contains(text(), "Присоединиться")]')
    button_join = (By.XPATH, '//a[@class="sc-dkzDqf gpYSxm"]')
    english_lang = (By.XPATH, '//div[@class="sc-fLlhyt ebHyXN"]')
    button_language = (By.XPATH, '//div[@class="sc-fEOsli iBrHKJ" and contains(text(), "EN")]')
    button_theme = (By.XPATH, '//div[@class="sc-fnykZs fEkGUM"]')
    link_startup = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "StartUp для")]')
    link_mentors = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "Менторы")]')
    link_projects = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "Проекты")]')
    link_o_nas = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "О нас")]')
    razdel_o_nas = (By.XPATH, '//p[@class="sc-cCsOjp cdaqyF"]')
    razdel_projects = (By.XPATH, '//p[@class="sc-cOFTSb.bNtNdQ.is-inview"]')


class LPLL:

    button_theme = (By.XPATH, '//div[@class="sc-fnykZs lfkjFc"]')