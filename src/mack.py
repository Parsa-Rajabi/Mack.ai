#This file would be the starting point, what we run to start the bot
#TODO we have to write and include the GUI interface here

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("Starting Mack...")
import personality as p
from wit import Wit
access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'

client = Wit(access_token=access_token)
print("Mack started.")
looper = True
while looper:
    inputtext = input("> ")
    resp = client.message(inputtext)
    entities = resp['entities']
    valid = False
    for entity in entities:
        if entity == "intent":
            valid = True
            intent = resp['entities']['intent']
            if intent == "exit":
                looper = False  #Break out of the loop to shut down the chat
            if intent[0]['value'] in p.intents:
                print(p.intents[intent[0]['value']])
            else:
                print("I'm sorry, I don't know about that.")
    if not valid:
        print("I'm sorry, I don't know what you want from me.")
print("Mack shut down.")
