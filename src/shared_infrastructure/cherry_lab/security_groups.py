import aws_cdk as cdk

from aws_cdk import aws_ec2


class SecurityGroups(cdk.Construct):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.encd_demos = aws_ec2.SecurityGroup.from_security_group_id(
            self,
            'encd_demos',
            'sg-022ea667',
            mutable=False
        )
