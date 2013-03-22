from flask.ext.testing import TestCase
from uuid import uuid4
from machete.users.models import User


class BaseIntegrationTestCase(TestCase):
    def setUp(self):
        super(BaseIntegrationTestCase, self).setUp()
        self.email = uuid4().hex + '@gmail.com'
        self.passwd = uuid4().hex
        self.user = User.create(self.email, self.passwd, 'Testo')

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
