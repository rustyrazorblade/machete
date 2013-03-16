
"""
Tests creating a user, and logging in
"""

from machete.users.models import User
import unittest
import uuid


def test_create_and_login():
    email = uuid.uuid4().hex + "@test.com"
    password = "test123"

    user = User.create(email, password, "myname")
    assert isinstance(user, User)
    assert user.password != password

    user = User.get_by_email(email)
    assert isinstance(user, User)

    assert user.authenticate(password)
    assert not user.authenticate("nobacon")




