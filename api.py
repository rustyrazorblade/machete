import os

from flask import Flask

from machete.issues.blueprints import IssuesView
from machete.questions.blueprints import QuestionsView
from machete.wiki.blueprints import WikiView

from machete.templating.render import render, setup

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
