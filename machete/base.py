
from thunderdome.connection import setup
import thunderdome

setup(["localhost"], "machete")


class BaseVertex(thunderdome.Vertex):
    pass

class BaseEdge(thunderdome.Edge):
    pass


