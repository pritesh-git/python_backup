import pytest
from.basetest import BaseTest

from pages.searchpage import TexIncSearchPeople

class TestCase(BaseTest):

    def search_people_to_tex(self,browser):
        search_page = TexIncSearchPeople(browser)
        search_page.load()


