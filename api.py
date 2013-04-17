import os

from flask import Flask, session, redirect
from machete.base.routes import UUIDConverter

from machete.issues.blueprints import IssuesView, IssueConverter
from machete.questions.blueprints import QuestionsView
from machete.sessions.blueprints import LoginView, LogoutView
from machete.sessions.manager import SessionManager
from machete.projects.blueprints import ProjectsView, ProjectMemberView, ProjectConverter

from machete.templating.render import render, setup
from machete.wiki.blueprints import WikiView

app = Flask(__name__)
app.debug = True # for a while...

# set session manager
app.session_interface = SessionManager()

#base_dir = os.path.split(os.getcwd())[0]
base_dir = os.getcwd()
setup([base_dir + '/templates'], base_dir + '/static', debug=app.debug)

app.url_map.converters['uuid'] = UUIDConverter
app.url_map.converters['project'] = ProjectConverter
app.url_map.converters['issue'] = IssueConverter

IssuesView.register(app)
LoginView.register(app)
LogoutView.register(app)
QuestionsView.register(app)
WikiView.register(app)
ProjectsView.register(app)
ProjectMemberView.register(app)

# set up search indexes

@app.route("/")
def index():
    tvars = {}

    if not session.user:
        return redirect("/login/")


    return render('index.mako', tvars)

if __name__ == "__main__":
    app.run()
