from flask.ext.classy import FlaskView

from machete.templating import render
from machete.issues.models import Issue, IssueList

class IssuesView(FlaskView):
    def index(self):
        return render("issues.mako")
