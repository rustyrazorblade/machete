from machete.issues.models import Issue, Severity, Caliber, AssignedTo

import unittest


class CreateTest(unittest.TestCase):
    """Unit-tests around the creation of issues"""

    def setUp(self):
        super(CreateTest, self).setUp()
    
    def test_should_be_able_to_create_new_issue(self):
        """Should be able to create a new issue and get all related objects"""
        issue = Issue.create(description="Hey Jon, here's a bug for ya!")
        severity = Severity.create(name="Low Unbreak Now!")
        caliber = Caliber.create(issue, severity)

        assert issue.severity == severity
        assert issue in severity.issues
        assert caliber.issue == issue
        assert caliber.severity == severity

        with self.assertRaises(ValueError):
            Caliber.create(issue, severity)
