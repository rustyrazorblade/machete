from flask.ext.classy import FlaskView, route
from flask import request, session
from machete.base.routes import UUIDConverter

from machete.templating import render
from machete.issues.models import Issue, Severity
from machete.base.response import success

class IssueConverter(UUIDConverter):
    """Performs URL parameter validation against a UUID.

    Example:

    @app.route('/<projectid:uid>')

    """

    def to_python(self, value):
        return Issue.get(value)

class IssuesView(FlaskView):

    def index(self):
        return render("issues.mako")

    def get(self, issue):
        return render("issues/get.mako", {"issue": issue})

    def create(self, project):
        return render("issues/create.mako", {"project":project})

    def post(self, project):

        form = request.form
        severity = Severity.get(form['severity'])

        issue = Issue.create(session.user, form['name'], form['description'], project, severity)
        return success(issue)

