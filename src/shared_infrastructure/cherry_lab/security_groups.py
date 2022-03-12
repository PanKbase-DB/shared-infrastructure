from aws_cdk import aws_ec2

from constructs import Construct


class SecurityGroups(Construct):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.encd_demos = aws_ec2.SecurityGroup.from_security_group_id(
            self,
            'encd_demos',
            'sg-022ea667',
            mutable=False
        )
