from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnection:'
            'us-west-2:565393070554:'
            'connection/ee755097-8dd7-46d3-b0eb-2e2c80453299'
        )
