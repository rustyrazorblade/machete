from flask.ext.classy import FlaskView

from machete.templating import render

class IssuesView(FlaskView):
    def index(self):
        return render("issues.mako")
