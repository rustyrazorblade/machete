
import git

import thunderdome
from machete.base.models import BaseVertex, BaseEdge
from machete.base.config import config

class Wiki(BaseVertex):
    location = thunderdome.Text()

    @classmethod
    def create(cls):
        repo = git.Repo.init("/tmp/test_repo.git", bare=True)

    @property
    def repo(self):
        return git.Repo()

    @property
    def abs_location(self):
        return ""

class Page(BaseVertex):
    text = thunderdome.Text()
    rendered_text = thunderdome.Text()

    @property
    def wiki(self):
        self.inV(HasPage)[0]

    def save(self):
        # commit change to git repo
        # if successful, go ahead and save the changes

        index.add(['my_new_file'])      # add a new file to the index
        index.remove(['dir/existing_file'])
        new_commit = index.commit("my commit message")

        tmp = super(Page, self).save()
        return tmp

class HasPage(BaseEdge):
    pass


class HasWiki(BaseEdge):
    pass

class Draft(BaseVertex):
    text = thunderdome.Text()

class HasDraft(BaseVertex):
    pass


