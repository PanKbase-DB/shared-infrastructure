from constructs import Construct

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from typing import Any


class Notification(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.encode_dcc_chatbot = SlackChannelConfiguration.from_slack_channel_configuration_arn(
            self,
            'EncodeDCCChatbot',
            'arn:aws:chatbot::109189702753:chat-configuration/slack-channel/aws-chatbot'
        )
