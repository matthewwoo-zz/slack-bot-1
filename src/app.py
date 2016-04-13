# import json
# from slackclient import SlackClient
#
# token = "xoxb-34239333142-HspVW30XI57E1o6aQqHZpwuX"
# sc = SlackClient(token)
# message = sc.api_call("channels.history", channel="C103W0BRC", count=1)
# raw_message = json.dumps(message)
# print json_message
#
# print json_message['messages'][0]['text']
# json_message = json.loads(raw_message)



#
# import time, json, yaml, re, os
# from slackclient import SlackClient
# token = "xoxb-34239333142-HspVW30XI57E1o6aQqHZpwuX"
# sc = SlackClient(token)
#
# while True:
#   new_evts = sc.rtm_read()
#   for evt in new_evts:
#       print(evt)
#       if "type" in evt:
#         if evt["type"] == "message" and "text" in evt:
#           message=evt["text"]
#       time.sleep(3)

# print sc.api_call("channels.info", channel="C103W0BRC")
# print sc.api_call(
#     "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
#     username='pybot', icon_emoji=':robot_face:'
# )


import time
import requests
from slackclient import SlackClient
token = "xoxp-34138599623-34132008758-34138148288-4cb67550a9"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        if sc.rtm_read():
            time.sleep(3)
else:
    print "Connection Failed, invalid token?"

