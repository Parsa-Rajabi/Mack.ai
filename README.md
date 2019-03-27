# COSC 310 Project
The goal of this project is to create an interactive, text-based chatbot which is capable of completing 30 turns of conversation in a realistic manner. This must be accomplished using proper communication, structure and planning in order to accurately represent the industry standards. 

# Scenario
Our project is simulating a blind first date scenario with the mysterious ‘Mackenzie’. It will cover topics such as hobbies, interests and goals. The scenario has multiple endings, both positive and negative, based on user responses. The majority of the responses will contain humour as the primary personality trait.

# Implementation
The project is being implemented using python and the library wit.ai which was chosen because it handles all of the natural language processing for us which turns the text into intents. Python was chosen due to it working well with wit.ai and we were all familiar with it. 

# How to compile and run Mack.py 
This was created and test on python3.7
## Windows Instructions: 

*If python doesn’t work replace it with py*

1. Install Pycharm or any alternative python compiler 
2. Open command prompt and ensure you have the latest pip and wheel:
  - Check if you have wheel installed
	` python -m pip help wheel `
  - If you don’t have wheel installed run this command: 
   `python -m pip install wheel --user  `
  - If you do have wheel installed run this command:
   `python -m pip install --upgrade pip wheel setuptools`
3. Install the dependencies
`python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer`
4. Install kivy and Wit.ai:    
`python -m pip install kivy
python -m pip install wit`
5. Run MackGui.py on python compiler
`	python MackGui.py`

## Mac OSX Instructions:
1. Install Pycharm or any alternative python compiler 
2. Open terminal and ensure you have the latest pip and wheel:
  - Check if you have wheel installed
	` python3 -m pip help wheel`
  - If you don’t have wheel installed run this command:
  ` python3 -m pip install wheel --user  `
  - If you do have wheel installed run this command:
  ` python3 -m pip install --upgrade pip wheel setuptools `
3. Install the dependencies
`python3 -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python3 -m pip install kivy.deps.gstreamer`
4. Install kivy and Wit.ai:    
`python3 -m pip install kivy
python3 -m pip install wit`
5. Run MackGui.py on python compiler
`	python3 MackGui.py`

# Class Structure
All classes are camelCase, contain only lowercase letters with capital letters signifying the start of a new word. Our classes are organized using the following folder structure. *note gui will be included in Mack*

  + Source
    + Data structure
    + Wit
    + Mack
    + Personality  
  + Docs
    + Gantt Chart
    + WBS
    + Project Proposal
    + Project Report
    + Toggl Summary
 
# Assignment 3 Details:

Additions: 
  + Added 6 new topics (1 per team member)
    + Colour Yellow
    + Gin
    + Rum
    + Amaretto
    + Tequila
    + Jager
   
  + Added 5 Different Off Topic Responses 
    + I'm sorry I don't understand.
    + Wanna talk about sports?
    + I do not understand you at all ;)
    + I am very confused right now.
    + Could we talk about something else?
   
  + Mack can now communicate with itself through our socket feature
  
Unchanged Features from A2: 
  + GUI was already implemented during A2
  + wit.ai was used to create Mack.ai which is a language toolkit 
  + wit.ai handles spelling mistakes 
    

# Project Plan Submission Deadline
January 31st, 2019 11:59 PM 

# A2 deadline
February 15th, 2019 11:59 PM 

# A3 deadline
April 5th, 2019
