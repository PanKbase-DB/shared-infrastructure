from constructs import Construct


class CodeStarConnection:

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codestar-connections:'
            'us-west-2:109189702753:'
            'connection/d65802e7-37d9-4be6-bc86-f94b2104b5ff'
        )
