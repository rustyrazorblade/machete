
import uuid
from machete.projects.models import Project

from machete.users.models import User, Group


def create_user():
    email = uuid.uuid4().hex + "@example.com"
    name = "test " + uuid.uuid4().hex
    return User.create(email, "test123", name)


def create_group():
    return Group.create(name="Test Group {}".format(uuid.uuid4().hex))

def create_wiki():
    return


def create_project(users=[]):
    name = "Test Project {}".format(uuid.uuid4().hex)
    p = Project.create(name=name)
    for u in users:
        p.add_user(u)
    return p



