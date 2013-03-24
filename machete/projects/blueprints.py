from flask import redirect, request, session
from flask.ext.classy import FlaskView, route
from machete.base.response import success

from machete.templating import render

from machete.projects.models import Project

class ProjectsView(FlaskView):
    def index(self):
        projects = session.user.projects
        return render('projects.mako')

    def get(self, id):
        project = Project.get(id)
        issues = []

        return render('projects/get.mako', {"project":project,
                                            "issues": issues})


class ProjectMemberView(FlaskView):
    route_base = "/projects/"

    @route("<uuid:project>/members/")
    def index(self, project):
        return render("projects/members/index.mako")

    @route("<uuid:project>/members/")
    def post(self, project):
        import ipdb; ipdb.set_trace()
        project = Project.get(project)
        return success({})

    def delete(self):
        return success({})
