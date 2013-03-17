from uuid import uuid4
from flask.ext.testing import TestCase
from machete.sessions.models import Authenticates, Session
from machete.users.models import User

class SessionApiTestCase(TestCase):

    def setUp(self):
        super(SessionApiTestCase, self).setUp()
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


    def test_success_case(self):

        response = self.post('/login/', {'email':self.email, 'password': self.passwd})
        self.assertEquals(response.status_code, 302)

        sessions = self.user.inV(Authenticates, types=[Session])
        assert len(sessions) == 1
