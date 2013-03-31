from datetime import datetime
from thunderdome.connection import setup
import thunderdome
from machete.base.config import config

host = config["rexster_host"]

setup([host], "machete", index_all_fields=False)


class BaseVertex(thunderdome.Vertex):
    created_at = thunderdome.DateTime(default=datetime.now)

    def __repr__(self):
        return "<{}:{}>".format(self.__class__.__name__, self.vid)

    @property
    def id(self):
        return self.vid

    @id.setter
    def id(self, id):
        self.vid = id

    @property
    def json(self):
        result = {}
        for name, col in self._columns.items():
            result[col.db_field or name] = col.to_python(getattr(self, name, None))

        # api is nicer with id instead of vid
        if 'vid' in result:
            result['id'] = result.pop('vid')
        return result


class BaseEdge(thunderdome.Edge):
    created_at = thunderdome.DateTime(default=datetime.now)

    def __repr__(self):
        return "<{}:{}>".format(self.__class__.__name__, self.eid)


class CreatedBy(BaseEdge):
    pass


