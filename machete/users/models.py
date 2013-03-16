
import passlib
from passlib.hash import sha256_crypt
import thunderdome
from machete.base import BaseVertex, BaseEdge


class User(BaseVertex):
    name = thunderdome.String()
    email = thunderdome.String()
    password = thunderdome.String()

    @classmethod
    def hash(password):
        """
        >>> # import the hash algorithm
        >>> from passlib.hash import sha256_crypt

        >>> # generate new salt, and hash a password
        >>> hash = sha256_crypt.encrypt("toomanysecrets")
        >>> hash
        '$5$rounds=80000$zvpXD3gCkrt7tw.1$QqeTSolNHEfgryc5oMgiq1o8qCEAcmye3FoMSuvgToC'

        >>> # verifying the password
        >>> sha256_crypt.verify("toomanysecrets", hash)
        True
        >>> sha256_crypt.verify("joshua", hash)
        False
        """
        sha256_crypt.encrypt

        return password

    @classmethod
    def create(cls, email, password, name):
        password = sha256_crypt.encrypt(password)
        return super(User, cls).create(email=email, password=password, name=name)

    @classmethod
    def authenticate(cls, email, password):
        sha256_crypt.verify(password)
        return False
    @classmethod
    def get_by_email(cls, email):
        return


class Group(BaseVertex):
    name = thunderdome.String()

    def add(self, user):
        MemberOf.create(Group, User)

class MemberOf(BaseEdge):
    pass


