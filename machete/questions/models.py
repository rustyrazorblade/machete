
import thunderdome

from machete.base.models import BaseVertex, BaseEdge


class Question(BaseVertex):
    text = thunderdome.String()



class Answer(BaseVertex):
    text = thunderdome.String()

    @property
    def question(self):
        self.inV()

class HasAnswer(BaseEdge):
    pass






