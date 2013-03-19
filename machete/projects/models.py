
import thunderdome
from machete.base import BaseVertex, BaseEdge
from machete.users.models import User, Group


class Project(BaseVertex):
    name = thunderdome.String()

    def add_user(self, user):
        assert isinstance(user, User)

    def add_group(self, group):
        assert isinstance(group, Group)

class HasProject(BaseEdge):
    pass
