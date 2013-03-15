
import thunderdome
from machete.base import BaseVertex, BaseEdge

class Issue(BaseVertex):
    description = thunderdome.String()

class Severity(BaseVertex):
    name = thunderdome.String()

class AssignedTo(BaseEdge):
    pass

