from flask import redirect, request, session
from flask.ext.classy import FlaskView, route
from machete.base.response import success
from machete.base.routes import UUIDConverter

from machete.templating import render

from machete.projects.models import Project
from machete.users.models import User

class ProjectConverter(UUIDConverter):
    """Performs URL parameter validation against a UUID.

    Example:

    @app.route('/<projectid:uid>')

    """

    def to_python(self, value):
        return Project.get(value)


class ProjectsView(FlaskView):
    def index(self):
        projects = session.user.projects
        return render('projects.mako')

    def get(self, id):
        issues = []

        return render('projects/get.mako', {"project":project,
                                            "issues": issues})


class ProjectMemberView(FlaskView):
    route_base = "/projects/"

    @route("<project:project>/members/")
    def index(self, project):
        return render("projects/members/index.mako")

    @route("<project:project>/members/", methods=["POST"])
    def post(self, project):
        user = User.get(request.form['user'])
        project.add_user(user)
        return success({})

    @route("<project:project>/members/<uuid:user>", methods=["DELETE"])
    def delete(self, project, user):
        user = User.get(user)
        return success({})
