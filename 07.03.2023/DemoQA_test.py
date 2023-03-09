'''
 Пожалуйста, сделайте этот тесткейс на языке python (займет час-полтора
 https://docs.google.com/spreadsheets/d/1zyN8MSUAD5pRDfu0t1ZZzLlgwa5fPBfGTYxMiXXI2cI/edit?usp=sharing)
 используя паттерн PageObject и библиотеку webdriver manager.
'''
from BasePage import CheckBoxPage, ElementsPage, MainPage
import pytest


class TestDemoQA:
    @pytest.fixture(scope='class', autouse=True)
    def prepare(self, request, browser):
        self = request.cls
        self.browser = browser
        self.main_page = MainPage(self.browser)
        self.checkbox_page = CheckBoxPage(self.browser)

    def test_open_demoqa(self):
        self.main_page.open('https://demoqa.com/')
        self.browser.set_page_load_timeout(30)
        assert self.browser.current_url == 'https://demoqa.com/', 'Incorrect  browser link'

    def test_category_cards(self):
        self.main_page.click_card('Elements')
        self.browser.set_page_load_timeout(30)
        assert self.browser.current_url == 'https://demoqa.com/elements'

    def test_elements_page(self):
        elementPage = ElementsPage(self.browser)
        group = elementPage.show_element_list('Elements')
        assert elementPage.is_element_list_shown('Elements')
        elementPage.click_menu_element('Check Box')
        self.browser.set_page_load_timeout(30)
        assert self.browser.current_url == 'https://demoqa.com/checkbox'

    def test_checkbox_page(self):
        assert self.checkbox_page.expand_tree('Home') is not None, f'No tree was opened'

    def test_checkbox_downloads(self):
        assert self.checkbox_page.expand_tree('Downloads') is not None, f'No tree was opened'

    def test_checkbox_result(self):
        self.checkbox_page.select_checkbox('Word File.doc')
        assert self.checkbox_page.get_text_result() == 'You have selected :wordFile'



