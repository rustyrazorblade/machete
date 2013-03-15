
from flask import Flask, render_template

from machete.issues.blueprints import IssuesView
from machete.questions.blueprints import QuestionsView
from machete.wiki.blueprints import WikiView

app = Flask(__name__)
app.debug = True # for a while...

IssuesView.register(app)
QuestionsView.register(app)
WikiView.register(app)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
