
"""
Tests creating a user, and logging in
"""

from machete.users.models import User
import unittest
import uuid



def test_create_and_login():
    email = uuid.uuid4().hex + "@test.com"

    user = User.create(email, "test123", "myname")
    assert isinstance(user, User)

    user = User.get_by_email(email)
    assert isinstance(user, User)


