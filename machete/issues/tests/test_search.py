from unittest import TestCase
from machete import snippets
from machete.base.tests import IntegrationTestCase
from machete.util import search

from machete.issues.models import Issue, InvalidSearchException, IssueList

# to save time, we're only going to be using setUpClass here
# we should have an exhaustive list of all the types of searches
# we can perform

# testing issue search should occur nowhere else.

from machete.util import search

class SearchTestMixin(object):

    @classmethod
    def setUpClass(cls):

        """
        Project1: user1, user2, user3
        Project2: user1, user2
        Project3: user1, user3
        """
        super(SearchTestMixin, cls).setUpClass()

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

        cls.issue1 = Issue.create(cls.user1, "first issue", "whatever dude", cls.project1, assigned=cls.user1)
        cls.issue2 = Issue.create(cls.user1, "second issue", "lamb on the ground", cls.project1, assigned=cls.user2)

        cls.issue3 = Issue.create(cls.user1, "friendly hello", "hey there dude", cls.project2, assigned=cls.user1)
        cls.issue4 = Issue.create(cls.user1, "big problem", "pizza on the ground", cls.project2)


        search.refresh() # to ensure our stuff is going to be there when we search


class TestSearch(SearchTestMixin, TestCase):
    def test_search_doc(self):
        assert self.issue1.search_doc

    def test_assignment(self):
        results = Issue.search(projects=[self.project1, self.project2], assigned=[self.user1])

        for x in results:
            self.assertEqual(self.user1.id, x.assigned_to_id)
            self.assertEqual(self.user1, x.assigned)

        self.assertEqual(results.total, 2)

        results = Issue.search(projects=[self.project1], assigned=[self.user1])
        self.assertEqual(results.total, 1)

        with self.assertRaises(InvalidSearchException):
            results = Issue.search(assigned=[self.user2])


    def test_project_filter(self):
        # should return 2 issues created on project1
        results = Issue.search(projects=[self.project1])
        self.assertEquals(results.total, 2)

    def test_multiple_projects_filter(self):
        results = Issue.search(projects=[self.project1, self.project2])
        self.assertEquals(results.total, 4)

    def test_text_filter(self):
        results = Issue.search(projects=[self.project1], search_text="whatever")
        self.assertEquals(results.total, 1)

        results = Issue.search(projects=[self.project1], search_text="first")
        self.assertEquals(results.total, 1)


class IssueListTest(SearchTestMixin, TestCase):

    @classmethod
    def setUpClass(cls):
        super(IssueListTest, cls).setUpClass()
        cls.issues = Issue.search(projects=[cls.project1])

    def test_issue_list_type(self):
        self.assertTrue(isinstance(self.issues, IssueList))

    def test_json(self):
        js = self.issues.json
        assert 'issues' in js
        assert 'facets' in js


class IntegrationTest(SearchTestMixin, IntegrationTestCase):
    def test_search_all_for_project(self):
        response = self.get('/issues/search?projects={}'.format(self.project1.id))
        self.assert200(response)
        js = response.json['data']
        assert 'facets' in js
        assert 'issues' in js

