
from thunderdome.connection import setup
import thunderdome

setup(["localhost"], "machete")


class BaseVertex(thunderdome.Vertex):
    created_at = thunderdome.DateTime()
    updated_at = thunderdome.DateTime()



class BaseEdge(thunderdome.Edge):
    pass


