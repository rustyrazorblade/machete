

from pyes.filters import TermFilter, ANDFilter, ORFilter
from pyes.query import *

import thunderdome

from machete.base.models import BaseVertex, BaseEdge, CreatedBy
from machete.projects.models import HasProject, Project
from machete.users.models import User

from machete.util import put_mapping, search

issue_mapping =\
    {
        "id": { "store":"yes", "type":"string", "index":"not_analyzed"},
        "name": {"store": "no", "type":"string", "index":"analyzed", "boost":1.5},
        "description": {"store":"no", "type":"string", "index":"analyzed"},
        "created_by_id": {"store":"no", "type":"string", "index":"not_analyzed"},
        "assigned_to_id": {"store":"no", "type":"string", "index":"not_analyzed"},
        "project_id": {"index":"not_analyzed", "type":"string"}
    }

put_mapping('issue', issue_mapping)


class InvalidSearchException(Exception):
    pass


class Issue(BaseVertex):
    """Represents an issue in machete and associated information."""
    name        = thunderdome.String()
    description = thunderdome.String()
    open        = thunderdome.Boolean()

    # cached properties to avoid dozens of extra lookups
    project_id  = thunderdome.String()
    severity_id = thunderdome.String()


    @classmethod
    def create(cls, user, name, description, project, severity, open=True):
        assert isinstance(project, Project)
        assert isinstance(severity, Severity)
        assert isinstance(user, User)

        issue = super(Issue, cls).create(name=name, description=description, open=open,
                                         project_id = project.id)

        CreatedBy.create(issue, user)
        HasProject.create(issue, project)
        issue.severity = severity

        issue.index()

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
        self.severity_id = severity.id
        self.save()

        for x in existing:
            x.delete()

    @property
    def project(self):
        return self.outV(HasProject)[0]

    @classmethod
    def search(self, projects=[], search_text = "", assigned=[], sort=None):
        """
        Search across projects, providing optional search text and other filters
        """

        if not projects:
            raise InvalidSearchException("projects are required")

        project_filters = ORFilter([TermFilter("project_id", p.id) for p in projects])

        # add assignment, lists, status, etc
        filters = project_filters

        if search_text:
            query = StringQuery(search_text, search_fields=["name", "description"])
        else:
            query = MatchAllQuery()

        query = FilteredQuery(query, filters)
        results = search.search(query=query, indices="machete")
        return results

    @property
    def created_by(self):
        return None

    @property
    def search_doc(self):
        tmp = {"name":self.name,
               "description":self.description,
               "project_id":self.project_id}
        return tmp

    def index(self):
        search.index(self.search_doc, 'machete', 'issue', self.id)


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




class AssignedTo(BaseEdge):
    """Edge associating an issue with a particular user or users"""
    pass
