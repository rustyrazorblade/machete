from uuid import uuid4
from machete.base.tests import IntegrationTestCase
from machete.sessions.models import Authenticates, Session
from machete.users.models import User

class SessionApiTestCase(IntegrationTestCase):

    def setUp(self):
        super(SessionApiTestCase, self).setUp(False)
        self.email = uuid4().hex + '@gmail.com'
        self.passwd = uuid4().hex
        self.user = User.create(self.email, self.passwd, 'Testo')

    def test_success_case(self):

        response = self.post('/login/', {'email':self.email, 'password': self.passwd})
        self.assertEquals(response.status_code, 302)

        sessions = self.user.inV(Authenticates, types=[Session])
        assert len(sessions) == 1
