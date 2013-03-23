from flask.ext.classy import FlaskView, route
from flask import request, jsonify
from machete.projects.models import Project

from machete.templating import render
from machete.issues.models import Issue, IssueList

class IssuesView(FlaskView):
    route_base = "/projects/"

    @route("<uuid:project>/issues")
    def index(self, project):

        return render("issues.mako")

    @route("<uuid:project>/issues/create")
    def create(self, project):
        project = Project.get(project)
        return render("issues/create.mako", {"project":project})


    @route("<uuid:project>/issues", methods=["POST"])
    def post(self, project):
        return jsonify({"test":"hi"})
