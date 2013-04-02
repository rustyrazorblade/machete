from unittest import TestCase
from machete.wiki.models import Wiki, Page


class CreatePageTest(TestCase):
    def test_create_page(self):
        wiki = Wiki.create()
        page = wiki.create_page("test name [Some link]",
                                "/index.html",
                                u"this is a test")
        assert isinstance(page, Page)
        assert page.html == u'<p>this is a test</p>'

