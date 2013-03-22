
# comments are on their own module because they can appear on anything

import thunderdome
from machete.base.models import BaseEdge, BaseVertex

class Comment(BaseVertex):
    text = thunderdome.String()

