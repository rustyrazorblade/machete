from flask.ext.classy import FlaskView

from machete.templating import render
from machete.issues.models import Issue, IssueList

class IssuesView(FlaskView):
    route_base = "/projects/<uuid:id>/issues/"

    def index(self):
        return render("issues.mako")

    def create(self):
        return render("issues/create.mako")


