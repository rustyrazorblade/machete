
import thunderdome
from machete.base import BaseVertex, BaseEdge, CreatedBy
from machete.users.models import User, Group


class Project(BaseVertex):
    name = thunderdome.String()

    @classmethod
    def create(cls, name, user):
        assert isinstance(user, User)
        project = super(Project, cls).create(name=name)
        CreatedBy.create(project, user)
        Permission.create(project, user)
        return project

    def add_user(self, user):
        assert isinstance(user, User)

    def add_group(self, group):
        assert isinstance(group, Group)


class HasProject(BaseEdge):
    pass


class Permission(BaseEdge):
    pass

