
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
        Permission.create(project, user)
        return project

    @classmethod
    def create_with_defaults(cls, name, user):
        from machete.issues.models import Status, HasStatus, Severity, HasSeverity

        project = cls.create(name, user)
        default_status = ["Open", "Closed"]

        for name in default_status:
            status = Status.create(name=name)
            HasStatus.create(project, status)

        default_severity = {"Low":10, "Medium":50, "High":90}
        for name,level in default_severity.iteritems():
            status = Severity.create(name=name, level=level)
            HasSeverity.create(project, status)

        return project

    def add_user(self, user):
        assert isinstance(user, User)

    def add_group(self, group):
        assert isinstance(group, Group)

    @property
    def severities(self):
        from machete.issues.models import HasSeverity
        return self.outV(HasSeverity)


class HasProject(BaseEdge):
    pass


class Permission(BaseEdge):
    pass

