from flask import render_template
from flask.ext.classy import FlaskView

from machete.templating import render

class QuestionsView(FlaskView):
    def index(self):
        return render("questions.mako")

