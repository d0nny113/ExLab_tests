from selenium.webdriver.common.by import By


class BaseLocators(object):

    LANDING_LINK = 'http://test.exlab.team/'
    LOGO_PIC_EXLAB = (By.XPATH, '//div[@id="logo_mobile"]')
    CONTAINER = (By.XPATH, '//div[@id="root"]')
    DARK_THEME = (By.XPATH, '//div[@class="sc-bczRLJ ckyTig"]')
    LIGHT_THEME = (By.XPATH, '//div[@class="sc-bczRLJ cxdoLY"]')
    dark_class = 'sc-bczRLJ ckyTig'
    light_class = 'sc-bczRLJ cxdoLY'


class HeaderDark(object):

    menu_group = (By.XPATH, '//div[@class="sc-breuTD eGIhIU"]')
    link_group = (By.XPATH, '//nav[@class="sc-kDDrLX bvKWar"]')
    logo_dark = 'sc-jqUVSM EnPDN'
    text_join = (By.XPATH, '//a[@class="sc-dkzDqf gpYSxm" and contains(text(), "Присоединиться")]')
    button_join = (By.XPATH, '//div[@class="sc-hAZoDl hrEelO"]')
    english_lang = (By.XPATH, '//div[@class="sc-fLlhyt ebHyXN"]')
    button_language = (By.XPATH, '//div[@class="sc-fEOsli iBrHKJ" and contains(text(), "EN")]')
    button_theme = (By.XPATH, '//div[@class="sc-fnykZs fEkGUM"]')
    link_startup = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "StartUp для")]')
    link_mentors = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "Менторы")]')
    link_projects = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "Проекты")]')
    link_o_nas = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "О нас")]')


class HeaderLight:

    logo_light = 'sc-jqUVSM FjAfx'
    button_theme = (By.XPATH, '//div[@class="sc-fnykZs lfkjFc"]')
    razdel_o_nas = (By.XPATH, '//p[@class="sc-cCsOjp cdaqyF"]')
    razdel_projects = (By.XPATH, '//p[@class="sc-cOFTSb.bNtNdQ.is-inview"]')


class OpportunityDark:

    logo_exlab = (By.XPATH, '//img[@class="sc-dIouRR iBavKg"]')
    header_opportunity = (By.CSS_SELECTOR, 'div.sc-kgflAQ.gupdxc')
    footer_opportunity = (By.XPATH, '//span[@class="sc-kLLXSd fHrUpO"]')
    text_opportunity = (By.XPATH, '//div[@class="sc-bBrHrO lmeoyY"]')


class AboutUsDark:

    header_o_nas = (By.CSS_SELECTOR, '#about div')
    text_o_nas = (By.XPATH, '//p[@class="sc-cCsOjp cdaqyF"]')
    why_exlab_header = (By.XPATH, '//div[@class="sc-bZnhIo CLhmH"]')
    why_exlab_text = (By.XPATH, '//ol[@class="sc-iAvgwm fQGFrP"]')
    why_exlab_join_button = (By.XPATH, '//a[@class="sc-dkzDqf gpYSxm"]')


class ProjectsDark:

    header_projects = (By.CSS_SELECTOR, '#projects div')
    logo_projects_pics = (By.XPATH, '//img[@class="sc-bBXxYQ hEflMO"]')
    projects_text = (By.XPATH, '//p[@class="sc-cOFTSb bNtNdQ is-inview"]')


class MentorsDark:

    header_projects = (By.CSS_SELECTOR, '#mentors div')
    mentors_card = (By.XPATH, '//div[@class="sc-jOhDuK jCfVZq"]')
    mentor_photo = (By.CSS_SELECTOR, 'div.sc-kIKDeO.hGmlWc img')
    mentor_text = (By.CSS_SELECTOR, 'div.sc-kIKDeO.hGmlWc ul')
    mentors_button = (By.CSS_SELECTOR, 'span')


class FooterDark:

    inst_link = (By.XPATH, '//li[@class="sc-dkdnUF fbGNMP"]')
