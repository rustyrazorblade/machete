from unittest import TestCase
from machete.wiki.models import Wiki


class CreateWikiTest(TestCase):

    def test_create_wiki(self):
        wiki = Wiki.create()

