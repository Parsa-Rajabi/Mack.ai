#merge this and mack once we decide we want to use this or not

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import datetime

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window


print("Starting Mack...")
import personality as p
from wit import Wit
access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'
client = Wit(access_token=access_token)

def time_now():
    return "[" + datetime.datetime.now().strftime("%H:%M:%S") + "]"

#set specifics for the stuff in the gui
root_widget = Builder.load_string('''
<ScrollableLabel>:
    #Specifics of Scrollable Label
    text: app.text
    Label:
        text: root.text
        font_size: 14
        text_size: self.width, None
        color: [0,0,0,1]
        markup: True
        size_hint_y: None
        pos_hint: {"left":1, "top":1}
        height: self.texture_size[1] 
        valign: 'top'
        halign: 'left'
        scroll_y: None
        padding_x: 7
        padding_y: 7
<BoxLayout>
<RootWidget>:
    #Background Set
    BoxLayout:
        size: root.size
        pos: 0,0
        canvas.before:
            Rectangle: 
                pos: self.pos
                size: self.size
                source: '../mackenzie.jpg'
        
        #Conversation Box
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 10
            BoxLayout:
                size_hint: None, None
                size: root.width * 0.35, root.height - 100
                canvas.before:
                    Color:
                        rgba: 0,0,0,.75
                    BorderImage:
                        source: 'zelda.png'
                        pos: self.x - 1, self.y - 1
                        size: (root.width * 0.35)+2, root.height - 98
                    Color:
                        rgba: .95,.95,.95,.9
                    Rectangle: 
                        pos: self.pos
                        size: root.width * 0.35,root.height - 100
                ScrollableLabel:
                    id: Mack_output
                    markup: True
            
            #Bottom Bar
            BoxLayout:
                orientation: 'horizontal'
                spacing: 10
                size_hint_y: .1
                TextInput:
                    id: txt_input
                    background_color: [1,1,1,.95]
                    foreground_color: [0,0,0,1]
                    cursor_color: [0,0,0,1]
                    size_hint_x: .8
                    #multiline: False
                    write_tab: False
                    hint_text: "Insert Text Here"
                Button:
                    id: btn
                    text: 'Send'
                    font_size: 20
                    bold: True
                    size_hint_x: .2
                    background_color: [.8, .8, .8, 1]
                    color: [1, 1, 1, 1]
                    on_press: app.runStuff(txt_input.text)
                    on_release: app.read()
                    on_release: txt_input.text=""
''')


print("Mack Started")


class RootWidget(BoxLayout):
    pass


class ScrollableLabel(ScrollView):
    pass


class Mackenzie(App):
    text = StringProperty('')

    #Initiate the file to write and read from / Start conversation
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        Window.bind(on_key_up=self._on_keyboard_up)
        with open('Conversation.txt', 'w') as f:
            f.write('[b]' + time_now() + ' Mack:[/b] HI! My name is Mack and I am a chatbot!' + '\n')
            f.close()
        with open('Conversation.txt', 'r') as f:
            contents = f.read()
            self.text = contents

    #Make it so on keyboard enter it runs and clears text of text box
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:  # enter
            app.runStuff(self.root.ids.txt_input.text)
    def _on_keyboard_up(self,instance, keyboard, keycode):
        if keycode == 40:  # enter
            app.read()
            self.root.ids.txt_input.text=""

    #Handles user input and prints to screen
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
                    #makes call to tree to get response
                    response = p.tree.navigate_tree(resp, "topic", p.tree.get_root())
                    full_reply += response + ' '
                    #checks to make sure the user isnt exiting, if so closes window intent == exit
                    entities = resp['entities']
                    for entity in entities:
                        if entity == "intent":
                            intent = resp['entities']['intent']
                            if intent[0]['value'] == "exit":
                                app.get_running_app().stop()
                with open('Conversation.txt', 'a') as f:
                    f.write('[b]' + time_now() + ' User:[/b] ' + input + '\n')
                    f.write('[b]' + time_now() + ' Mack:[/b]' + str(full_reply) + '\n')
                    f.close()
        except:
                pass

    #Reads text from Conversation.txt to screen
    def read(self):
        with open('Conversation.txt', 'r') as f:
            contents = f.read()
            self.text = contents

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    app = Mackenzie()
    app.run()
