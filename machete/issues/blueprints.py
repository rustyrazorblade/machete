from flask.ext.classy import FlaskView, route

from machete.templating import render
from machete.issues.models import Issue, IssueList

class IssuesView(FlaskView):
    route_base = "/projects/"

    @route("<uuid:project>/issues/")
    def index(self, project):

        return render("issues.mako")

    def create(self):
        return render("issues/create.mako")


