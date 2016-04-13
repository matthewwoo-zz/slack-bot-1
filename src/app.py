import json

import re

import time
from slackclient import SlackClient
import src.common.constants as SlackConstants
from src.models.bots.bot import Bot

token = SlackConstants.TOKEN
channel = SlackConstants.CHANNEL
username = SlackConstants.USERNAME

sc = SlackClient(token)


if sc.rtm_connect():
    while True:
        new_evts = sc.rtm_read()
        for evt in new_evts:
            raw_message = json.dumps(evt)
            json_message = json.loads(raw_message)
            try:
                text = json_message['messages'][0]['text']
                print text
            try:
                pattern = re.compile(".{}.".format(username))
                match = pattern.search(text)
                user = match.group()
                if user == SlackConstants.USERNAME2:
                    Bot().post_message()
            except:
                pass
        time.sleep(1)
else:
    print "Connection failed"

    # for evt in new_evts:
    #     print(evt)
    #     if "type" in evt:
    #         if evt["type"] == "message" and "text" in evt:
    #             message = evt["text"]
    #     time.sleep(3)

'''
# raw_message = json.dumps(message)
# json_message = json.loads(raw_message)
# text = json_message['messages'][0]['text']
# pattern = re.compile(".{}.".format(username))
#
# match = pattern.search(text)
# user = match.group()

if user == SlackConstants.USERNAME2:
    Bot().post_message()


# '''
# {u'has_more': True, u'ok': True, u'messages':
#     [{u'username': u'instapaper', u'icons': {u'image_64': u'https://slack.global.ssl.fastly.net/d4bf/img/emoji_2015_2/apple/1f916.png', u'emoji': u':robot_face:'}, u'text': u'Hello from Python! :tada:', u'ts': u'1460575537.000009', u'subtype': u'bot_message', u'type': u'message'}]}
# Hello from Python! :tada:
# '''
#
#
