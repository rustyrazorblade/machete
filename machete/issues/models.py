

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
        "created_by_id": {"store":"yes", "type":"string", "index":"not_analyzed"},
        "assigned_to_id": {"store":"yes", "type":"string", "index":"not_analyzed"},
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

    # userid
    assigned_to_id = thunderdome.String()

    _assigned = None


    @classmethod
    def create(cls, user, name, description, project, assigned=None, open=True):
        assert isinstance(project, Project)
        assert isinstance(user, User)

        kwargs = {}
        if assigned:
            kwargs['assigned_to_id'] = assigned.id

        issue = super(Issue, cls).create(name=name, description=description, open=open,
                                         project_id = project.id, **kwargs)

        CreatedBy.create(issue, user)
        HasProject.create(issue, project)

        if assigned:
            AssignedTo.create(issue, assigned)


        issue.index()

        return issue

    @property
    def assigned(self):
        if self._assigned:
            return self._assigned
        try:
            tmp = self.outV(AssignedTo)[0]
            self._assigned = tmp
            return self._assigned
        except:
            return None


    @assigned.setter
    def assigned(self, user):
        # if an assigned edge exists, remove it
        existing = AssignedTo.get_between(self, user)
        map(lambda x: x.delete(), existing)

        # create new assigned edge
        AssignedTo.create(self, user)
        self.assigned_to_id = user.id
        self.save()
        self.index()


    @property
    def project(self):
        # TODO: memoize
        return self.outV(HasProject)[0]

    @classmethod
    def search(self, projects=[], search_text = "", assigned=[], sort=None):
        """
        Search across projects, providing optional search text and other filters

        Projects are required, even if filtering by user.

        At this level, we don't know who is performing the search, so we don't know
        the scope that they are allowed to see

        we treat lists of requirements as OR

        for instance, if multiple users are passed in for assigned, we return results matching any of the users
        in the list

        in the case of multiple arguments being passed in, we AND.  For instance, for a search on 2 users and
        2 projects:

        (project1 or project1) AND (user1 or user2)

        This lets people set up complex searches matching multiple criteria
        """

        if not projects:
            raise InvalidSearchException("projects are required")

        filters = ORFilter([TermFilter("project_id", p.id) for p in projects])

        if assigned and not isinstance(assigned, list):
            assigned = [assigned]

        if assigned:
            user_filters = ORFilter([TermFilter("assigned_to_id", u.id) for u in assigned])
            filters = ANDFilter([filters, user_filters])

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
        """
        generates a search doc for ES indexing
        """
        tmp = {"name":self.name,
               "description":self.description,
               "project_id":self.project_id}

        if self.assigned_to_id:
            tmp["assigned_to_id"] = self.assigned_to_id

        return tmp

    def index(self):
        search.index(self.search_doc, 'machete', 'issue', self.id)


class IssueProxy(object):
    def __init__(self, user):
        self.user = user

class IssueList(object):
    """
    provides a generic means of iterating over a list of issues
    built to support search
    """
    def __init__(self, ids, facets, total):
        self.user = []
        self.limit = None
        self.status = []
        self._issues = []
        self.total = 0

    def __iter__(self):
        return self

    def next(self):
        return None




class AssignedTo(BaseEdge):
    """Edge associating an issue with a particular user or users"""
    pass
