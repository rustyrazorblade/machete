import thunderdome
from machete.base import BaseVertex, BaseEdge




class Issue(BaseVertex):
    """Represents an issue in machete and associated information."""
    description = thunderdome.String()

    @classmethod
    def create(cls, description, project, severity, status):
        assert project
        assert severity
        assert status

        issue = super(Issue, cls).create(description=description)

        HasProject.create(issue, project)
        HasStatus.create(issue, status)
        HasSeverity.create(issue, severity)

        return issue

    @property
    def severity(self):
        """
        Returns the severity associated with this issue

        :rtype: machete.issues.models.Severity or None
        
        """
        result = self.outV(HasSeverity)
        return result[0] if result else None

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

    @classmethod
    def create(cls, issue, severity):
        """
        Create a new edge associating and issue with a severity. Raises an
        exception if there is already a severity associated with the given
        issue. (functional edge)

        :rtype: machete.issues.models.HasSeverity
        
        """
        if issue.severity is not None:
            raise ValueError(
                'issue {} already has an associated severity'.format(issue)
            )
        return super(HasSeverity, cls).create(issue, severity)
        
    @property
    def issue(self):
        """
        Return the issue associated with this caliber.

        :rtype: machete.issues.models.Issue
                
        """
        return self.outV()

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
