import json
from slackclient import SlackClient
import src.common.constants as SlackConstants
from src.models.bots.bot import Bot

token = SlackConstants.TOKEN
channel = SlackConstants.CHANNEL
username = SlackConstants.USERNAME

sc = SlackClient(token)
message = sc.api_call("channels.history", channel=channel, count=1)
raw_message = json.dumps(message)
json_message = json.loads(raw_message)
print json_message
print json_message['messages'][0]['text']

# user = json_message['messages'][0]['username']
#
if user == *username*:
#     Bot().post_message()

'''
{u'has_more': True, u'ok': True, u'messages':
    [{u'username': u'instapaper', u'icons': {u'image_64': u'https://slack.global.ssl.fastly.net/d4bf/img/emoji_2015_2/apple/1f916.png', u'emoji': u':robot_face:'}, u'text': u'Hello from Python! :tada:', u'ts': u'1460575537.000009', u'subtype': u'bot_message', u'type': u'message'}]}
Hello from Python! :tada:
'''

# from flask import Flask
#
# app = Flask(__name__)
# app.config.from_object('config')
# app.secret_key = "123"
# app.secret key is used to keep the cookies are servers are using to track users safe


