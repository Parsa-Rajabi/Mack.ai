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
  + + Data structure
  + + Wit
  + + Mack
  + + Personality  
  + Docs
  

# Project Plan Submission Deadline
January 31st, 2019 11:59 PM 

# Final deadline
February 15th, 2019 11:59 PM 


# Specific evaluation criteria are:

+ 5 points: Creation of individual GitHub accounts and having a team repository there.
+ 4 points: Brief description of project being done. Description and rationale for the chosen SDLC. List of limitations of the program submitted.
+ 6 points: Listing of phases, tasks, subtasks. Breadth of coverage. Meaningful breakdown.
+ 10 points: WBS including all task assignments, hour estimations, actual hours. Distribution of workload should be fair.
+ 5 points: Gantt chart with start/end dates and dependencies.
+ 10 points: Software's ability to undergo 30 turns of a dialogue. Quality of dialogue: is the conversation "smooth" and realistic? Coverage of test output provided.
+ 10 points: Software design (at the class level) and understandability of code documentation.
+ 5 points: Presentation: does the demo work? Were branches used per feature implemented? Did everyone contribute to the project in some way?
+ 5 points each round: Four rounds of peer evaluations for each of your team member. At each round, 4 points are allocated towards your ability to critique and 1 point based on your peer reports on you.
