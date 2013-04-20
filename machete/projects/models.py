
import thunderdome
from machete.base.models import BaseVertex, BaseEdge, CreatedBy
from machete.users.models import User, Group


class Project(BaseVertex):
    name = thunderdome.String()

    @classmethod
    def create(cls, name, user):

        assert isinstance(user, User)
        project = super(Project, cls).create(name=name)
        CreatedBy.create(project, user)
        project.add_user(user)

        # create wiki
        from machete.wiki.models import Wiki, HasWiki
        wiki = Wiki.create()
        HasWiki.create(project, wiki)

        return project

    @property
    def wiki(self):
        from machete.wiki.models import Wiki, HasWiki
        return self.outV(HasWiki)[0]

    @classmethod
    def create_with_defaults(cls, name, user):
        project = cls.create(name, user)
        return project

    def add_user(self, user):
        assert isinstance(user, User)
        Permission.create(self, user)

    def remove_user(self, user):
        assert isinstance(user, User)
        tmp = Permission.get_between(self, user)
        tmp.delete()

    def add_group(self, group):
        assert isinstance(group, Group)



class HasProject(BaseEdge):
    pass


class Permission(BaseEdge):

    pass

