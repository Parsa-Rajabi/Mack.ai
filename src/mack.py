# This file would be the starting point, what we run to start the bot
# TODO we have to write and include the GUI interface here

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from wit import Wit
import personality as p

print("Starting Mack...")
access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'

client = Wit(access_token=access_token)
print("Mack started.")
looper = True
while looper:
    inputText = input("> ")
    resp = client.message(inputText)
    print("Mack: " + p.tree.navigate_tree(resp, "topic", p.tree.get_root()))
    entities = resp['entities']
    valid = False
    for entity in entities:
        if entity == "intent":
            valid = True
            intent = resp['entities']['intent']
            if intent == "exit":
                looper = False  #Break out of the loop to shut down the chat
print("Mack shut down.")
