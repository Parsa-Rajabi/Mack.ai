#merge this and mack once we decide we want to use this or not

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder



print("Starting Mack...")
import personality as p
from wit import Wit
access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'
client = Wit(access_token=access_token)


#set specifics for the stuff in the gui
Builder.load_string('''
<ScrollableLabel>:
    text: app.text
    Label:
        text: root.text
        font_size: 22
        text_size: self.width, None
        color: [1,1,1,1]
        size_hint_y: None
        pos_hint: {"left":1, "top":1}
        height: self.texture_size[1]
        scroll_y: None
<RootWidget>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        ScrollableLabel
        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: .1
            TextInput:
                id: txt_input
                background_color: [1,1,1,1]
                foreground_color: [0,0,0,1]
                cursor_color: [0,0,0,1]
                size_hint_x: .8
            Button:
                id: btn
                text: 'Send'
                size_hint_x: .2
                background_color: [.8, .8, .8, 1]
                color: [1, 1, 1, 1]
                on_press: app.runStuff(txt_input.text)
                on_release: app.read()
''')



print("Mack Started")


class RootWidget(BoxLayout):
    pass


class ScrollableLabel(ScrollView):
    pass


class ChatBot(App):
    text = StringProperty('')

    #initiate the file to write and read from
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('Conversation.txt', 'w') as f:
            f.write('Mack: HI! My name is Mack and I am a chatbot!' + '\n')
            f.close()
        with open('Conversation.txt', 'r') as f:
            contents = f.read()
            self.text = contents

    #handles user input and prints to screen
    def runStuff(self, input):
        try:
                #split sentences up into parts
                userInput = re.split('[\.!?]', input.lower().rstrip('.!?'))
                full_reply = ' '
                for sentence in userInput:
                    #removes white space in front of input
                    sentence=sentence.lstrip()
                    #get response from wit for each sentence
                    resp = client.message(sentence)
                    entities = resp['entities']
                    valid = False
                    for entity in entities:
                        if entity == "intent":
                            valid = True
                            intent = resp['entities']['intent']
                            if intent == "exit":
                                response = "bye"
                                full_reply += response + ' '
                            if intent[0]['value'] in p.intents:
                                response = p.intents[intent[0]['value']]
                                full_reply += response + ' '
                            else:
                                response = "I'm sorry, I don't know about that."
                                full_reply += response + ' '
                    if not valid:
                        response = "I'm sorry, I don't know what you want from me."
                        full_reply += response + ' '
                with open('Conversation.txt', 'a') as f:
                    f.write('User: ' + '  ' + input + '\n')
                    f.write('Mack:' + str(full_reply) + '\n')
                    f.close()

        except:
                pass

    #reads text from Conversation.txt to screen
    def read(self):
        with open('Conversation.txt', 'r') as f:
            contents = f.read()
            self.text = contents

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    app = ChatBot()
    app.run()
