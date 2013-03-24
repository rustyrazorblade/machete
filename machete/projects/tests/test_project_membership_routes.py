from machete import snippets
from machete.base.tests import IntegrationTestCase


class AddUserToProjectTest(IntegrationTestCase):
    def test_add_user(self):
        user = snippets.create_user()
        url = "/projects/{}/members/".format(self.project.id)
        response = self.post(url, {"user":user.id})
        self.assert200(response)

