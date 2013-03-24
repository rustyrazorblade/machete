from flask import redirect, request, session
from flask.ext.classy import FlaskView, route
from machete.base.response import success

from machete.templating import render

from machete.projects.models import Project
from machete.users.models import User


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

    @route("<uuid:project>/members/", methods=["POST"])
    def post(self, project):
        project = Project.get(project)
        user = User.get(request.form['user'])
        project.add_user(user)
        return success({})

    def delete(self):
        return success({})
