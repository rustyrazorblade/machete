import sys
sys.path.append("")
from shovel import task

from machete.users.models import User, Group
from machete.projects.models import Project


@task
def create(name, email):
    user = User.get_by_email(email)
    project = Project.create_with_defaults(name, user)
    print "Created project {}".format(name)
