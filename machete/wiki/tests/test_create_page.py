from unittest import TestCase
from machete.base.tests import IntegrationTestCase
from machete.wiki.models import Wiki, Page


class CreatePageTest(TestCase):
    def test_create_page(self):
        wiki = Wiki.create()
        page = wiki.create_page("test name [Some link]",
                                "/index.html",
                                u"this is a test")
        assert isinstance(page, Page)
        assert page.html == u'<p>this is a test</p>'


class PageIntegrationTest(IntegrationTestCase):
    def test_create_page(self):
        url = "/projects/{}/wiki/".format(self.project.vid)
        response = self.post(url, {"url":"TestPage",
                                   "name":"Whatever bro",
                                   "text":"this is a test"})
        self.assert200(response)

        url = "/projects/{}/wiki/TestPage".format(self.project.vid)
        response = self.get(url)
        self.assert200(response)

        url = "/projects/{}/wiki/".format(self.project.vid)
        response = self.get(url)
        self.assert200(response)

