from flask.ext.classy import FlaskView

from machete.templating import render


class WikiView(FlaskView):
    def index(self):
        return render("wiki.mako")
