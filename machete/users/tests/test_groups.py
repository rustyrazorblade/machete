
from machete.users.models import Group
from machete.snippets import create_user


def test_group_add():
    u1 = create_user()
    u2 = create_user()

    g = Group.create(name="test group")
    assert isinstance(g, Group)

    g.add(u1)
    g.add(u2)

    assert len(g.members) == 2




