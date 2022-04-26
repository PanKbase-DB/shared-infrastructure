from constructs import Construct

from shared_infrastructure.igvf_dev.connection import CodeStarConnection
from shared_infrastructure.igvf_dev.domain import DemoDomain
from shared_infrastructure.igvf_dev.secret import DockerHubCredentials
from shared_infrastructure.igvf_dev.vpc import DemoVpc


class Resources(Construct):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = DemoVpc(
            self,
            'DemoVpc',
        )
        self.domain = DemoDomain
            self,
            'DemoDomain',
        )
        self.docker_hub_credentials = DockerHubCredentials(
            self,
            'DockerHubCredentials',
        )
        self.code_star_connection = CodeStarConnection(
            self,
            'CodeStarConnection',
        )
