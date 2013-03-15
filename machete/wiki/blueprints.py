from flask import render_template
from flask.ext.classy import FlaskView


class WikiView(FlaskView):
    def index(self):
        return render_template("wiki.html")
