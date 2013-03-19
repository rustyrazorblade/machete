import os

from flask import Flask

from machete.issues.blueprints import IssuesView
from machete.questions.blueprints import QuestionsView
from machete.sessions.blueprints import LoginView, LogoutView
from machete.sessions.manager import SessionManager
from machete.projects.blueprints import ProjectsView

from machete.templating.render import render, setup
from machete.wiki.blueprints import WikiView

app = Flask(__name__)
app.debug = True # for a while...

# set session manager
app.session_interface = SessionManager()

#base_dir = os.path.split(os.getcwd())[0]
base_dir = os.getcwd()
setup([base_dir + '/templates'], base_dir + '/static', debug=app.debug)

IssuesView.register(app)
LoginView.register(app)
LogoutView.register(app)
QuestionsView.register(app)
WikiView.register(app)
ProjectsView.register(app)

@app.route("/")
def index():
    return render('index.mako')

if __name__ == "__main__":
    app.run()
