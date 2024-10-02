from constructs import Construct

from aws_cdk.aws_secretsmanager import Secret

from typing import Any


class DockerHubCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'DockerSecret',
            'arn:aws:secretsmanager:us-west-2:565393070554:secret:docker-pankbase-db-joCYc5',
        )


class PortalCredentials(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.indexing_service_key = Secret.from_secret_complete_arn(
            self,
            'IndexingServiceKey',
            'arn:aws:secretsmanager:us-west-2:565393070554:secret:indexing-service-portal-pQ7RjP',
        )


class UploadFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:565393070554:secret:upload-pankbase-files-user-access-key-secret-SRRgkH',
        )


class UploadRestrictedFilesUserAccessKeys(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.secret = Secret.from_secret_complete_arn(
            self,
            'AccessKeyAndSecretAccessKey',
            'arn:aws:secretsmanager:us-west-2:565393070554:secret:upload-pankbase-restricted-files-user-access-key-secret-DWPFVb',
        )
