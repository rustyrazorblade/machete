from unittest import TestCase
from machete import snippets
from machete.util import search

from machete.issues.models import Issue

# to save time, we're only going to be using setUpClass here
# we should have an exhaustive list of all the types of searches
# we can perform

# testing issue search should occur nowhere else.

class TestSearch(TestCase):

    @classmethod
    def setUpClass(cls):

        """
        Project1: user1, user2, user3
        Project2: user1, user2
        Project3: user1, user3
        """
        super(TestSearch, cls).setUpClass()

        cls.user1 = snippets.create_user()
        cls.user2 = snippets.create_user()
        cls.user3 = snippets.create_user()

        cls.project1 = snippets.create_project(cls.user1)
        cls.project2 = snippets.create_project(cls.user1)
        cls.project3 = snippets.create_project(cls.user1)

        cls.project1.add_user(cls.user2)
        cls.project1.add_user(cls.user3)

        cls.project2.add_user(cls.user2)

        cls.project3.add_user(cls.user3)

        sev = cls.project1.severities[0]
        Issue.create(cls.user1, "some issue", "whatever dude", cls.project1, sev)
        Issue.create(cls.user1, "some other issue", "lamb on the ground", cls.project1, sev)

    def test_search_doc(self):
        assert self.issue1.search_doc

    def test_assignment(self):
        assert False

    def test_project_filter(self):
        assert False




