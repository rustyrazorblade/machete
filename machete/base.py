from datetime import datetime
from thunderdome.connection import setup
import thunderdome

setup(["localhost"], "machete")


class BaseVertex(thunderdome.Vertex):
    created_at = thunderdome.DateTime(default=datetime.now)

class BaseEdge(thunderdome.Edge):
    created_at = thunderdome.DateTime(default=datetime.now)


class CreatedBy(BaseEdge):
    pass


