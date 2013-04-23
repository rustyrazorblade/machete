from flask.ext.classy import FlaskView, route
from flask import request, session
from machete.base.routes import UUIDConverter
from machete.projects.models import Project

from machete.templating import render
from machete.issues.models import Issue
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

    def create(self):
        return render("issues/create.mako", {"project":project})

    def post(self):
        form = request.form
        project = Project.get(form['project'])

        issue = Issue.create(session.user,
                             form['name'],
                             form['description'],
                             project)

        return success(issue)

    @route("/search")
    def search(self):
        # we might want to have /issues/search just return all issues
        # that are open in all projects a user is a part of

        pids = request.args.get('projects').split(",")
        assert pids
        projects = Project.all(pids)

        issues = Issue.search(projects)

        return success(issues)

