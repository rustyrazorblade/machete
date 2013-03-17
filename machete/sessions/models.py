from datetime import datetime, timedelta

from flask.sessions import SessionMixin
import thunderdome

from machete.base import BaseVertex, BaseEdge
from machete.users.models import User

class Authenticates(BaseEdge):
    """
    Connects a session to a user
    """

# length of session in seconds
# TODO: put this in a config file
SESSION_LENGTH = 60*60*24

def _get_session_expiration():
    return datetime.now() + timedelta(seconds=SESSION_LENGTH)

class Session(BaseVertex, SessionMixin):

    expires = thunderdome.DateTime(required=True, default=_get_session_expiration)
    data    = thunderdome.Dictionary(required=False)

    def __init__(self, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.deleted = False

    @property
    def is_expired(self):
        return datetime.now() >= self.expires

    @property
    def user(self):
        if self.eid is None: return None
        users = self.outV(Authenticates, types=[User])
        return users[0] if users else None

    @user.setter
    def user(self, val):
        if val is not None and not isinstance(val, User):
            raise TypeError('user must be a User instance')

        current_obj = self.user
        if current_obj == val: return
        if current_obj is not None:
            for edge in Authenticates.get_between(self, current_obj):
                edge.delete()

        if val is not None:
            Authenticates.create(self, val)

    def refresh(self):
        self.expires = _get_session_expiration()
        self.save()

    def delete(self):
        super(Session, self).delete()
        self.deleted = True

    def __getitem__(self, item):
        self.data = self.data or {}
        return self.data[item]

    def __setitem__(self, key, value):
        self.data = self.data or {}
        self.data[key] = value
