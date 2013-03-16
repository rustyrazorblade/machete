from datetime import datetime
from thunderdome.connection import setup
import thunderdome

setup(["localhost"], "machete")


class BaseVertex(thunderdome.Vertex):
    created_at = thunderdome.DateTime(default=datetime.now)

    def __repr__(self):
        return "<{}:{}>".format(self.__class__.__name__, self.vid)

class BaseEdge(thunderdome.Edge):
    created_at = thunderdome.DateTime(default=datetime.now)

    def __repr__(self):
        return "<{}:{}>".format(self.__class__.__name__, self.eid)


class CreatedBy(BaseEdge):
    pass


