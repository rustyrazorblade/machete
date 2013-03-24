
from flask.ext.testing import TestCase
from machete import snippets


class IntegrationTestCase(TestCase):
    def setUp(self, create_user=True, login=True, create_project=True):
        super(IntegrationTestCase, self).setUp()
        if create_user:
            self.user = snippets.create_user()
            if create_project:
                self.project = snippets.create_project(self.user)
            if login:
                self.login()

    def create_app(self):
        from api import app
        app.config['TESTING'] = True
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

    def login(self):
        return self.post("/login/", {'email':self.user.email, 'password': snippets.password})

