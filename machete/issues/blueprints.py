from flask.ext.classy import FlaskView, route
from flask import request, jsonify, session
from machete.base.routes import UUIDConverter
from machete.projects.models import Project

from machete.templating import render
from machete.issues.models import Issue, IssueList, Severity
from machete.base.response import success, error

class IssueConverter(UUIDConverter):
    """Performs URL parameter validation against a UUID.

    Example:

    @app.route('/<projectid:uid>')

    """

    def to_python(self, value):
        return Issue.get(value)

class IssuesView(FlaskView):
    route_base = "/projects/"

    @route("<project:project>/issues")
    def index(self, project):

        return render("issues.mako")

    @route("<project:project>/issues/<issue:issue>")
    def get(self, project, issue):
        return render("issues/get.mako", {"issue": issue})

    @route("<project:project>/issues/create")
    def create(self, project):
        return render("issues/create.mako", {"project":project})


    @route("<project:project>/issues/", methods=["POST"])
    def post(self, project):

        form = request.form
        severity = Severity.get(form['severity'])

        issue = Issue.create(session.user, form['name'], form['description'], project, severity)
        return success(issue)

