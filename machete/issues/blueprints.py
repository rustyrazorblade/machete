from flask.ext.classy import FlaskView, route
from flask import request, jsonify, session
from machete.projects.models import Project

from machete.templating import render
from machete.issues.models import Issue, IssueList, Severity
from machete.base.response import success, error


class IssuesView(FlaskView):
    route_base = "/projects/"

    @route("<uuid:project>/issues")
    def index(self, project):

        return render("issues.mako")

    @route("<uuid:project>/issues/create")
    def create(self, project):
        project = Project.get(project)
        return render("issues/create.mako", {"project":project})


    @route("<uuid:project>/issues/", methods=["POST"])
    def post(self, project):

        project = Project.get(project)
        form = request.form
        severity = Severity.get(form['severity'])

        issue = Issue.create(session.user, form['name'], form['description'], project, severity)
        return success(issue)

