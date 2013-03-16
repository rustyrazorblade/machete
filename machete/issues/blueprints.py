from flask import render_template, jsonify
from flask.ext.classy import FlaskView


class IssuesView(FlaskView):
    def index(self):
        return render_template("issues.html")
