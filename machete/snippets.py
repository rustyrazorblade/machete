
import uuid

from machete.users.models import User


def create_user():
    email = uuid.uuid4().hex + "@example.com"
    name = "test " + uuid.uuid4().hex
    return User.create(email, "test123", name)


def create_group():
    return

def create_wiki():
    return




