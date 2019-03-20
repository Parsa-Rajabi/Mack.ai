# This file would be the starting point, what we run to start the bot
# TODO we have to write and include the GUI interface here

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from wit import Wit
import personality as p
import time
from socket import *
s = socket(AF_INET, SOCK_STREAM)


print("Starting Mack...")
access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'

client = Wit(access_token=access_token)
print("Mack started.")
looper = True
sentMsg = '¯\_(ツ)_/¯'
print("Mack: " +sentMsg)
s.connect(('localhost', 6789))
while looper:

    s.send(sentMsg.encode(encoding='UTF-8'))

    inputText = s.recv(1024).decode(encoding='UTF-8')
    resp = client.message(inputText)

    print("Opponant: " + inputText)
    time.sleep(1)
    sentMsg = p.tree.navigate_tree(resp, "topic", p.tree.get_root())
    print("Mack: " + sentMsg)
    time.sleep(1)
    entities = resp['entities']
    valid = False
    for entity in entities:
        if entity == "intent":
            valid = True
            intent = resp['entities']['intent']
            if intent == "exit":
                looper = False  #Break out of the loop to shut down the chat
print("Mack shut down.")
