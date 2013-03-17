from datetime import datetime

from flask.sessions import SessionInterface

from machete.sessions.models import Session

class SessionManager(SessionInterface):

    def open_session(self, app, request):
        """
        Called at the beginning of a request, either loads an existing session,
        or creates a new one. Nothing is saved here
        """
        vid = request.cookies.get(app.session_cookie_name)

        try:
            session = Session.get(vid)
            if session.is_expired:
                session.delete()
                session = Session()

            return session

        except Session.DoesNotExist:
            return Session()

    def save_session(self, app, session, response):
        """
        Saves the session object on a request
        """
        domain = self.get_cookie_domain(app)

        if session.user is None:
            session.delete()

        if session.deleted:
            if response:
                response.delete_cookie(
                    app.session_cookie_name,
                    domain=self.get_cookie_domain(app)
                )
            return

        session.refresh()

        if response:
            response.set_cookie(
                app.session_cookie_name,
                session.vid,
                expires=session.expires,
                httponly=False,
                domain=domain
            )
