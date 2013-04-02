
import git
import markdown

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

    def create_page(self, name, url, text):
        p = Page.create(name=name, ulr=url, text=text)
        HasPage.create(self, p)
        return p


class Page(BaseVertex):
    text = thunderdome.Text()
    html = thunderdome.Text()
    name = thunderdome.Text()
    url  = thunderdome.Text()

    @property
    def wiki(self):
        self.inV(HasPage)[0]

    def save(self, *args, **kwargs):
        self.html = markdown.markdown(self.text, ['fenced_code', 'codehilite', 'tables', 'toc'])
        return super(Page, self).save(*args, **kwargs)


class HasPage(BaseEdge):
    pass


class HasWiki(BaseEdge):
    pass

class Draft(BaseVertex):
    text = thunderdome.Text()

class HasDraft(BaseVertex):
    pass


