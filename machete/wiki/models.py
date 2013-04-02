
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
        wiki.create_page("Wiki", "", "Welcome to the wiki.")
        return wiki

    @property
    def repo(self):
        return git.Repo(self.location)

    @property
    def location(self):
        return "{}/{}".format(config['wiki_dir'], self.id)

    def create_page(self, name, url, text):
        p = Page.create(wiki=self, name=name, url=url, text=text)
        return p

    def find_page(self, url):
        return None


class Page(BaseVertex):
    text = thunderdome.Text()
    html = thunderdome.Text()
    name = thunderdome.Text()

    # fragment.  can be whatever the user wants that's allowed in a pagename
    # shooting for pretty urls
    # example: project/id/wiki/GettingStarted
    url  = thunderdome.Text()
    wiki_id = thunderdome.Text()
    lookup_url = thunderdome.Text()

    @property
    def wiki(self):
        Wiki.get(self.wiki_id)

    @classmethod
    def create(cls, wiki, name, url, text):
        page = super(Page, cls).create(wiki_id=wiki.id,
                                       name=name,
                                       url=url,
                                       text=text)
        HasPage.create(wiki, page)
        return page

    def save(self, *args, **kwargs):
        self.html = markdown.markdown(self.text, ['fenced_code', 'codehilite', 'tables', 'toc'])
        self.lookup_url = "{}:{}".format(self.wiki_id, self.url)

        return super(Page, self).save(*args, **kwargs)


class HasPage(BaseEdge):
    pass


class HasWiki(BaseEdge):
    pass

class Draft(BaseVertex):
    text = thunderdome.Text()

class HasDraft(BaseVertex):
    pass


