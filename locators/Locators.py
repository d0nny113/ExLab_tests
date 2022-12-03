from selenium.webdriver.common.by import By


class BaseLocators(object):

    LANDING_LINK = 'https://exlab.team/'
    LOGO_PIC_EXLAB = (By.XPATH, '//div[@id="logo_mobile"]')
    CONTAINER = (By.XPATH, '//div[@id="root"]')
    dark_theme = 'sc-fnykZs fEkGUM'
    light_theme = 'sc-fnykZs lfkjFc'
    button_theme = (By.CSS_SELECTOR, '.sc-ksZaOG.bxLYUZ')


class HeaderDark(object):

    menu_group = (By.XPATH, '//div[@class="sc-breuTD eGIhIU"]')
    link_group = (By.XPATH, '//li[@class="sc-crXcEl ikVVqy"]')
    logo_dark = 'sc-jqUVSM EnPDN'
    text_join = (By.XPATH, '//a[@class="sc-dkzDqf gpYSxm" and contains(text(), "Присоединиться")]')
    button_join = (By.XPATH, '//div[@class="sc-hAZoDl hrEelO"]')
    english_lang = (By.XPATH, '//div[@class="sc-fLlhyt ebHyXN"]')
    button_language = (By.XPATH, '//div[@class="sc-fEOsli iBrHKJ" and contains(text(), "EN")]')
    button_theme = (By.XPATH, '//div[@class="sc-ksZaOG bxLYUZ"]')
    link_startup = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "StartUp для")]')
    link_mentors = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "Менторы")]')
    link_projects = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "Проекты")]')
    link_o_nas = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "О нас")]')
    link_o_nas2 = (By.XPATH, '//a[@class="sc-evZas hJsxZw" and contains(text(), "О нас")]')


class HeaderLight:

    logo_light = 'sc-jqUVSM FjAfx'
    button_theme = (By.XPATH, '//div[@class="sc-fnykZs lfkjFc"]')
    razdel_o_nas = (By.XPATH, '//p[@class="sc-cCsOjp cdaqyF"]')
    razdel_projects = (By.XPATH, '//p[@class="sc-cOFTSb.bNtNdQ.is-inview"]')


class OpportunityDark:

    logo_exlab = (By.CSS_SELECTOR, 'div.sc-jSMfEi.ktArbA')
    header_opportunity = (By.CSS_SELECTOR, 'div.sc-dmRaPn.ljhwJa')
    text_opportunity = (By.XPATH, '//div[@class="sc-kgflAQ gUFAgN"]')


class AboutUsDark:

    header_o_nas = (By.CSS_SELECTOR, '#about div')
    text_o_nas = (By.XPATH, '//p[@class="sc-himrzO bgsrpw"]')
    why_exlab_header = (By.XPATH, '//div[@class="sc-ciZhAO fBFmnR"]')
    why_exlab_text = (By.XPATH, '//ol[@class="sc-bZnhIo fYGDkJ"]')
    why_exlab_join_button = (By.XPATH, '//a[@class="sc-dkzDqf dEddqP"]')


class ProjectsDark:

    header_projects = (By.CSS_SELECTOR, '#projects div')
    logo_projects_pics = (By.CSS_SELECTOR, 'img.sc-jOrMOR.eGXkMj')
    projects_text = (By.XPATH, '//p[@class="sc-dPyBCJ elZmsx"]')


class HelpProjectDark:

    header = (By.CSS_SELECTOR, '.sc-jTYCaT.coDMnK')
    text = (By.XPATH, '//div[@class="sc-HzFiz fvqpxc"]')
    link_boosty = (By.XPATH, '//a[@class="sc-dkzDqf dEddqP" and contains(text(), "Boosty")]')
    link_patreon = (By.XPATH, '//a[@class="sc-hKMtZM etdNbW" and contains(text(), "Patreon")]')


class StayConnectedDark:

    header = (By.CSS_SELECTOR, '.sc-bhVIhj.uaVnA')
    text = (By.CSS_SELECTOR, '.sc-eGAhfa.cacMWv')


class MentorsDark:

    header_mentors = (By.CSS_SELECTOR, '#mentors div')
    mentors_card = (By.CSS_SELECTOR, '.sc-jIAOiI.eSpxWu')
    mentor_photo = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc img')

    mentor_text = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc ul')
    mentors_button = (By.CSS_SELECTOR, 'span')
    mentors_name = (By.CSS_SELECTOR, 'p.sc-jOhDuK.efeKUw')



class StartUpForDark:

    header = (By.CSS_SELECTOR, '#startup div')
    text = (By.XPATH, '//p[@class="sc-gFGZVQ eMPtDU"]')


class FooterDark:

    footer_links = (By.XPATH, '//li[@class="sc-dkdnUF fbGNMP"]')
    footer_logo = (By.CSS_SELECTOR, '.sc-fIavCj.fEzmxG')
    footer_text_under_logo = (By.CSS_SELECTOR, '.sc-gITdmR.hYaavu')
    link_lnkdn = (By.XPATH, '//a[@class="sc-WCkqM gwMRik" and contains(text(), "lnkdn")]')
    link_instgrm = (By.XPATH, '//a[@class="sc-WCkqM gwMRik" and contains(text(), "instgrm")]')
    link_tlgrm = (By.XPATH, '//a[@class="sc-WCkqM gwMRik" and contains(text(), "tlgrm")]')
    link_ytb = (By.XPATH, '//a[@class="sc-WCkqM gwMRik" and contains(text(), "ytb")]')
    mailto = (By.XPATH, '//a[@class="sc-ikjQzJ gjCqBu"]')

class TestTest:

    footer = (By.CSS_SELECTOR, '.sc-brCFrObGFIzb')
