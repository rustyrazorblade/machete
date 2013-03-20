
from unittest import TestCase, skip
from machete import snippets


class AddToProjectTest(TestCase):
    def setUp(self):
        self.user = snippets.create_user()
        self.project = snippets.create_project(self.user)
        assert self.project

    def test_add_user(self):
        user = snippets.create_user()
        self.project.add_user(user)

    @skip
    def test_add_group(self):
        group = snippets.create_group()
        self.project.add_group(group)
