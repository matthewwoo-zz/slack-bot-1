import json
from slackclient import SlackClient

token = "xoxb-34239333142-HspVW30XI57E1o6aQqHZpwuX"
sc = SlackClient(token)
message = sc.api_call("channels.history", channel="C103W0BRC", count=1)
raw_message = json.dumps(message)
json_message = json.loads(raw_message)

print json_message

print json_message['messages'][0]['text']

# print sc.api_call("channels.info", channel="C103W0BRC")
# print sc.api_call(
#     "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
#     username='pybot', icon_emoji=':robot_face:'
# )


# import time
# import requests
# from slackclient import SlackClient
# token = "xoxp-34138599623-34132008758-34138148288-4cb67550a9"
# sc = SlackClient(token)
# if sc.rtm_connect():
#     while True:
#         print sc.rtm_read()
#         time.sleep(1)
# else:
#     print "Connection Failed, invalid token?"

