import thunderdome
from machete.base import BaseVertex, BaseEdge


class Issue(BaseVertex):
    """Represents an issue in machete and associated information."""
    description = thunderdome.String()

    @property
    def severity(self):
        """
        Returns the severity associated with this issue

        :rtype: machete.issues.models.Severity
        
        """
        result = self.outV(Caliber)
        # Ensure this invariant holds as each issue should have one severity
        assert len(result) <= 1
        return result[0]

        
class Severity(BaseVertex):
    """Indicates the severity of an issue"""
    name = thunderdome.String()

    @property
    def issues(self):
        """
        Return a list of issues associated with this severity.

        :rtype: list
        
        """
        return self.inV(Caliber)

        
class Caliber(BaseEdge):
    """Edge connecting an issue to its severity"""

    @property
    def issue(self):
        """
        Return the issue associated with this caliber.

        :rtype: machete.issues.models.Issue
                
        """
        return self.outV()

    @property
    def severity(self):
        """
        Return the severity associated with this caliber.

        :rtype: machete.issues.models.Severity
        
        """
        return self.inV()
        

class AssignedTo(BaseEdge):
    """Edge associating an issue with a particular user or users"""
    pass
