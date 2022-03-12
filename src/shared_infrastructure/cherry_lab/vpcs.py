import aws_cdk as cdk

from aws_cdk import aws_ec2


class VPCs(cdk.Construct):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.default_vpc = aws_ec2.Vpc.from_lookup(
            self,
            'VPC',
            vpc_id='vpc-ea3b6581'
        )
