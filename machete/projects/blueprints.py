from flask import redirect, request, session
from flask.ext.classy import FlaskView, route

from machete.templating import render

from machete.projects.models import Project

class ProjectsView(FlaskView):
    def index(self):
        return render('projects.mako')

