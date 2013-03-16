import os

from flask import Flask

from issues.blueprints import IssuesView
from questions.blueprints import QuestionsView
from wiki.blueprints import WikiView

from templating.render import render, setup

app = Flask(__name__)
app.debug = True # for a while...

#base_dir = os.path.split(os.getcwd())[0]
base_dir = os.getcwd()
setup([base_dir + '/templates'], base_dir + '/static', debug=app.debug)

IssuesView.register(app)
QuestionsView.register(app)
WikiView.register(app)

@app.route("/")
def index():
    return render('index.mako')

if __name__ == "__main__":
    app.run()
