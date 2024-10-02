from constructs import Construct

from aws_cdk.aws_secretsmanager import Secret

from typing import Any


class DockerHubCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'DockerSecret',
            'arn:aws:secretsmanager:us-west-2:495599754696:secret:docker-pankbase-db-Rla2zW',
        )


class PortalCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.indexing_service_key = Secret.from_secret_complete_arn(
            self,
            'IndexingServiceKey',
            'arn:aws:secretsmanager:us-west-2:495599754696:secret:indexing-service-portal-gewpZr',
        )


class UploadFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:495599754696:secret:upload-pankbase-files-user-access-key-secret-nwxf78',
        )


class UploadRestrictedFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:495599754696:secret:upload-pankbase-restricted-files-user-access-key-secret-FSgROD',
        )
