from flask import redirect, request, session
from flask.ext.classy import FlaskView, route

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


