
import git

import thunderdome
from machete.base.models import BaseVertex, BaseEdge
from machete.base.config import config

class Wiki(BaseVertex):

    @classmethod
    def create(cls):
        wiki = super(Wiki, cls).create()
        repo = git.Repo.init(wiki.location)
        return wiki

    @property
    def repo(self):
        return git.Repo(self.location)

    @property
    def location(self):
        return "{}/{}".format(config['wiki_dir'], self.id)


class Page(BaseVertex):
    text = thunderdome.Text()
    rendered_text = thunderdome.Text()

    @classmethod
    def create(cls):
        pass

    @property
    def wiki(self):
        self.inV(HasPage)[0]


class HasPage(BaseEdge):
    pass


class HasWiki(BaseEdge):
    pass

class Draft(BaseVertex):
    text = thunderdome.Text()

class HasDraft(BaseVertex):
    pass


