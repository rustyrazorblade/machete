from machete.base.tests import BaseIntegrationTestCase
from machete.sessions.models import Authenticates, Session

class SessionApiTestCase(BaseIntegrationTestCase):

    def test_success_case(self):

        response = self.post('/login/', {'email':self.email, 'password': self.passwd})
        self.assertEquals(response.status_code, 302)

        sessions = self.user.inV(Authenticates, types=[Session])
        assert len(sessions) == 1
