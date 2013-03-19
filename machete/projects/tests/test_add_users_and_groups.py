
from unittest import TestCase
from machete import snippets


class AddToProjectTest(TestCase):
    def setUp(self):
        self.project = snippets.create_project()
        assert self.project

    def test_add_user(self):
        user = snippets.create_user()
        self.project.add_user(user)

    def test_add_group(self):
        group = snippets.create_group()
        self.project.add_group(group)
