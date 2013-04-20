from machete import snippets
from machete.base.tests import IntegrationTestCase
from machete.issues.models import Issue, AssignedTo,  Project

import unittest


class CreateTest(unittest.TestCase):
    """Unit-tests around the creation of issues"""

    def setUp(self):
        super(CreateTest, self).setUp()

    def test_should_be_able_to_create_new_issue(self):
        """Should be able to create a new issue and get all related objects"""
        user = snippets.create_user()
        project = Project.create(name="test project", user=user)

        issue = Issue.create(user, name="test issue",
                             description="Hey Jon, here's a bug for ya!",
                             project=project)

class CreateIntegrationTest(IntegrationTestCase):
    def test_create_issue(self):
        url = "/issues/"
        data = {"name":"some issue",
                "project": self.project.vid,
                "description":"shut up"}

        response = self.post(url, data)
        self.assert200(response)
        js = response.json['data']

        assert data['name'] == js['name']
        assert data['description'] == js['description']



