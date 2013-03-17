import sys
sys.path.append("")

from machete.users.models import User
from shovel import task


@task
def create(email, password, name=None):
    """
    Creates a user, name should be one word

    :param email:
    :param password:
    :param name:
    :return:
    """
    user = User.create(email, password, name)
