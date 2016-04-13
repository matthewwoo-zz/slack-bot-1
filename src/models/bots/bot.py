from slackclient import SlackClient
import src.models.bots.constants as BotConstants

class Bot(object):
    def __init__(self, token=None, username=None):
        self.token = BotConstants.TOKEN if token is None else None
        self.username = BotConstants.USERNAME if username is None else None

    def __repr__(self):
        print "{}, {}".format(self.token, self.username)

    def post_message(self):
        sc = SlackClient(self.token)
        print sc.api_call("api.test")
        sc.api_call(
            "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
            username=self.username, as_user="false", icon_emoji=':robot_face:'
        )
