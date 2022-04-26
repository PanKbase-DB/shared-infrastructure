from constructs import Construct

from aws_cdk.aws_secretsmanager import Secret


class DockerHubCredentials(Construct):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'DockerSecret',
            'arn:aws:secretsmanager:us-west-2:109189702753:secret:docker-hub-credentials-EStRH5',
        )
