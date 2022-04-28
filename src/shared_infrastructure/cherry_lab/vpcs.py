from aws_cdk import aws_ec2

from constructs import Construct

from typing import Any


class VPCs(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any):
        super().__init__(scope, construct_id, **kwargs)
        self.default_vpc = aws_ec2.Vpc.from_lookup(
            self,
            'VPC',
            vpc_id='vpc-ea3b6581'
        )
