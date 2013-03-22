from flask.ext.testing import TestCase
from uuid import uuid4
from machete import snippets
from machete.users.models import User


class IntegrationTestCase(TestCase):
    def setUp(self, create_user=True, create_project=True):
        super(IntegrationTestCase, self).setUp()
        if create_user:
            self.user = snippets.create_user()
            if create_project:
                self.project = snippets.create_project(self.user)

    def create_app(self):
        from api import app
        return app

    def get(self, *args, **kwargs):
        return self.client.get(*args, **kwargs)

    def post(self, path, data, *args, **kwargs):
        kwargs['path'] = path
        kwargs['data'] = data
        return self.client.post(*args, **kwargs)

    def put(self, path, data, *args, **kwargs):
        kwargs['path'] = path
        kwargs['data'] = data
        return self.client.put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.client.delete(*args, **kwargs)
