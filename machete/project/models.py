
import thunderdome
from machete.base import BaseVertex, BaseEdge

class Project(BaseVertex):
    name = thunderdome.String()

class HasProject(BaseEdge):
    pass
