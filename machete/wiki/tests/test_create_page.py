from unittest import TestCase
from machete.wiki.models import Wiki, Page


class CreatePageTest(TestCase):
    def test_create_page(self):
        wiki = Wiki.create()
        page = wiki.create_page("test name",
                                "/index.html",
                                "this is a test")
        assert isinstance(page, Page)

