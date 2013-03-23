import thunderdome
from machete.base.models import BaseVertex, BaseEdge, CreatedBy
from machete.projects.models import HasProject, Project
from machete.users.models import User


class Issue(BaseVertex):
    """Represents an issue in machete and associated information."""
    name = thunderdome.String()
    description = thunderdome.String()
    open = thunderdome.Boolean()

    @classmethod
    def create(cls, user, name, description, project, severity, status, open=True):
        assert isinstance(project, Project)
        assert isinstance(severity, Severity)
        assert isinstance(status, Status)
        assert isinstance(user, User)

        issue = super(Issue, cls).create(name=name, description=description, open=open)

        HasProject.create(issue, project)
        HasStatus.create(issue, status)
        HasSeverity.create(issue, severity)
        CreatedBy.create(issue, user)

        return issue

    @property
    def severity(self):
        """
        Returns the severity associated with this issue

        :rtype: machete.issues.models.Severity or None
        
        """
        result = self.outV(HasSeverity)
        return result[0] if result else None

    @severity.setter
    def severity(self, severity):
        # if a severity is already set, set the new one, then break the old
        assert isinstance(severity, Severity)
        existing = self.outE(HasSeverity)
        new_severity = HasSeverity.create(self, severity)

        for x in existing:
            x.delete()


class IssueProxy(object):
    def __init__(self, user):
        self.user = user

class IssueList(object):
    def __init__(self):
        self.user = []
        self.limit = None
        self.status = []
        self._issues = []

    def __iter__(self):
        return self

    def next(self):
        return None

class Status(BaseVertex):
    """
    in a normal system, issues will just be opened or closed
    however there's complex workflows that use QA, Deployed, etc
    """
    name = thunderdome.String()
    level = thunderdome.Integer()


class HasStatus(BaseEdge):
    pass

        
class Severity(BaseVertex):
    """Indicates the severity of an issue"""
    name = thunderdome.String()

    @property
    def issues(self):
        """
        Return a list of issues associated with this severity.

        :rtype: list
        
        """
        return self.inV(HasSeverity)

        
class HasSeverity(BaseEdge):
    """Edge connecting an issue to its severity"""

    @property
    def severity(self):
        """
        Return the severity associated with this caliber.

        :rtype: machete.issues.models.Severity
        
        """
        return self.inV()
        

class AssignedTo(BaseEdge):
    """Edge associating an issue with a particular user or users"""
    pass
