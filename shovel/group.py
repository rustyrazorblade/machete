import sys
sys.path.append("")
from shovel import task

from machete.users.models import User, Group

@task
def create(name):
    group = Group.create(name=name)
    print "Group {} created".format(name)


