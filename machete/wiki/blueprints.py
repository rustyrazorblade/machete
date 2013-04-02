
from flask import request, session
from flask.ext.classy import FlaskView, route

from machete.templating import render
from machete.base.response import success


class WikiView(FlaskView):
    route_base = "/projects/"

    @route("<project:project>/wiki/", methods=["GET"])
    def index(self, project):
        return render("wiki.mako")

    @route("<project:project>/wiki/<string:page>", methods=["GET"])
    def get(self, project, page):
        return render("wiki.mako")

    @route("<project:project>/wiki/", methods=["POST"])
    def post(self, project):
        x = request.form
        page = project.wiki.create_page(x['name'], x['url'], x['text'])
        return success(page)

    @route("<project:project>/wiki/<string:page>", methods=["PUT"])
    def put(self, project, name):
        page = project.wiki.find_page(name)
        return success(page)
