from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnection:'
            'us-west-2:565393070554:'
            'connection/c3f2e400-46e5-4af6-8397-d3815e49113e'
        )
