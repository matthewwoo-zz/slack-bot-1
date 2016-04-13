# import time
# from slackclient import SlackClient
#
# token = "xoxp-34138599623-34132008758-34138148288-4cb67550a9"
# sc = SlackClient(token)
# print sc.api_call("api.test")
# print sc.api_call("channels.info", channel="1234567890")
# print sc.api_call(
#     "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
#     username='pybot', icon_emoji=':robot_face:'
# )
#

import time
from slackclient import SlackClient

token = "xoxp-34138599623-34132008758-34138148288-4cb67550a9"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"