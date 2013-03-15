

from flask import render_template
from flask.ext.classy import FlaskView


class QuestionsView(FlaskView):
    def index(self):
        return render_template("questions.html")

