from machete import snippets
from machete.issues.models import Issue, Severity, HasSeverity, AssignedTo, Status, Project

import unittest


class CreateTest(unittest.TestCase):
    """Unit-tests around the creation of issues"""

    def setUp(self):
        super(CreateTest, self).setUp()
    
    def test_should_be_able_to_create_new_issue(self):
        """Should be able to create a new issue and get all related objects"""
        user = snippets.create_user()
        project = Project.create(name="test project", user=user)
        severity = Severity.create(name="Low Unbreak Now!")
        status = Status.create(name="Open")

        issue = Issue.create(description="Hey Jon, here's a bug for ya!", project=project,
                             severity=severity, status=status)

        assert issue.severity == severity
        assert issue in severity.issues

        with self.assertRaises(ValueError):
            HasSeverity.create(issue, severity)
