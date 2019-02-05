from node import Node as n
import personalityTree as pt
print("loading personality...")

# available intents:

root = n.init_root_node("topic", [], "Root Node: Topic", {
    "getPreference": "I like talking to you, for one ;)",
    "getState": "I'm doing well, thanks.",
    "getContinuousState": "Sorry, I don't know if I do that.",
    "getPastState": "I used to be nothing. Then I became a chat bot!",
    "response": "Interesting, go on.",
    "garbage": "Garbage belongs in the trash, not sent at me.",
    "getCurrentPreference": "I'm having a good time here so far.",
    "exit": "Buh-Bye! See you next time! :)",
    "getPastAction": "I might've done that once.",
    "getKnowledge": "I'm not sure, sorry.",
    "flirt": "*wink*",
    "greeting": "Hi there! I'm Mack. How are you today?",
    "unknown": "I'm sorry, I don't know about that."
})
tree = pt.Tree(root)
stack = []

# topic : activities, people, food, drink, day, date, location, response, education, occupation, exit
pa = root
tree.add_node("exit", [], pa, {
    "unknown": "Goodbye!"
})
tree.add_node("activities", [], pa, {
    "getPreference": "TODO: I like to...",
    "getContinuousState": "TODO: I work part time as a chat bot.",
    "unknown": "What about that activity?"
})
tree.add_node("people", [], pa, {
    "getPreference": "I like you, and I dislike Donald Trump",
    "unknown": "I'm sorry, I don't think I know that person."
})
tree.add_node("food", [], pa, {
    "getPreference": "I love pizza. :)",
    "unknown": "I'm sorry, I don't know that food."
})
tree.add_node("drink", [], pa, {
    "getPreference": "I love coffee, beer, and milkshakes.",
    "unknown": "I'm sorry, I don't know that drink."
})
tree.add_node("day", [], pa, {
    "getPreference": "Today is nice.",
    "unknown": "What about today?"
})
tree.add_node("date", [], pa, {
    "getPreference": "I like our date so far.",
    "unknown": "How about this date? Do you like it so far?"
})
tree.add_node("location", [], pa, {
    "getPreference": "I like where we are.",
    "unknown": "Do you like where we are?"
})
tree.add_node("response", [], pa, {
    "unknown": "I'm sorry, I don't understand what you mean."
})
tree.add_node("education", [], pa, {
    "unknown": "What about my schooling?"
})
tree.add_node("occupation", [], pa, {
    "unknown": "What about my job?"
})

# topic > people : Mack, date, generic
stack.append(pa)
pa = pa.get_child("people")

tree.add_node("Mack", [], pa, {
    "unknown": "What about me?"
})
tree.add_node("date", [], pa, {
    "unknown": "Tell me about yourself."
})
tree.add_node("generic", [], pa, {
    "unknown": "I'm sorry, I don't know about that person."
})

# topic > people > generic : man, woman
stack.append(pa)
pa = n.get_child(pa, "generic")

tree.add_node("man", [], pa, {
    "unknown": "I'm sorry, I don't know about men."
})
tree.add_node("woman", [], pa, {
    "unknown": "I'm sorry, I don't know about women."
})

# topic > people :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic :
pa = stack.pop()

# topic > activities : sport, hobby, music
stack.append(pa)
pa = n.get_child(pa, "activities")

tree.add_node("sport", [], pa, {
    "unknown": "What about sport?"
})
tree.add_node("hobby", [], pa, {
    "unknown": "What about hobbies?"
})
tree.add_node("music", [], pa, {
    "unknown": "What about music?"
})

# topic > activities > sport : soccer, basketball, football
stack.append(pa)
pa = n.get_child(pa, "sport")

tree.add_node("soccer", [], pa, {
    "unknown": "What about soccer?"
})
tree.add_node("basketball", [], pa, {
    "unknown": "What about basketball?"
})
tree.add_node("football", [], pa, {
    "unknown": "What about football?"
})

# topic > activities :
pa = stack.pop()

# topic > activities > hobby : hiking, cooking, swimming
stack.append(pa)
pa = n.get_child(pa, "hobby")

tree.add_node("hiking", [], pa, {
    "unknown": "What about hiking?"
})
tree.add_node("cooking", [], pa, {
    "unknown": "What about cooking?"
})
tree.add_node("swimming", [], pa, {
    "unknown": "What about swimming?"
})

# topic > activities :
pa = stack.pop()

# topic > activities > music : instrument
stack.append(pa)
pa = n.get_child(pa, "music")

tree.add_node("instrument", [], pa, {
    "unknown": "What about instruments?"
})

# topic > activities > music > instrument : guitar
stack.append(pa)
pa = n.get_child(pa, "instrument")

tree.add_node("guitar", [], pa, {
    "unknown": "What about guitar?"
})

# topic > activities > music :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic > activities :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic :
pa = stack.pop()

# topic > food : fish, spicy, dessert, dairy, fastfood
stack.append(pa)
pa = n.get_child(pa, "food")

tree.add_node("fish", [], pa, {
    "unknown": "What about fish?"
})
tree.add_node("spicy", [], pa, {
    "unknown": "What about spicy food?"
})
tree.add_node("dessert", [], pa, {
    "unknown": "What about dessert?"
})
tree.add_node("dairy", [], pa, {
    "unknown": "What about dairy?"
})
tree.add_node("fastfood", [], pa, {
    "unknown": "What about fast food?"
})

# topic > food > fish : sushi
stack.append(pa)
pa = n.get_child(pa, "fish")

tree.add_node("sushi", [], pa, {
    "unknown": "What about sushi?"
})

# topic > food :
pa = stack.pop()

# topic > food > dessert : pie
stack.append(pa)
pa = n.get_child(pa, "dessert")

tree.add_node("pie", [], pa, {
    "unknown": "What about pie?"
})

# topic > food :
pa = stack.pop()

# topic > food > dairy : cheese
stack.append(pa)
pa = n.get_child(pa, "dairy")

tree.add_node("cheese", [], pa, {
    "unknown": "What about cheese?"
})

# topic > food :
pa = stack.pop()

# topic > food > fastfood : pizza, nachos
stack.append(pa)
pa = n.get_child(pa, "fastfood")

tree.add_node("pizza", [], pa, {
    "unknown": "What about pizza?"
})
tree.add_node("nachos", [], pa, {
    "getPreference": "I love nachos!",
    "unknown": "What about nachos?"
})

# topic > food :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic :
pa = stack.pop()

# topic > drink : alcohol, coffee
stack.append(pa)
pa = n.get_child(pa, "drink")

tree.add_node("alcohol", [], pa, {
    "unknown": "What about alcohol?"
})
tree.add_node("coffee", [], pa, {
    "unknown": "What about coffee?"
})

# topic > drink > alcohol : beer, wine
stack.append(pa)
pa = n.get_child(pa, "alcohol")

tree.add_node("beer", [], pa, {
    "unknown": "What about beer?"
})
tree.add_node("wine", [], pa, {
    "unknown": "What about wine?"
})

# topic > drink :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic :
pa = stack.pop()

# topic > response : agree, disagree, neutral, feeling
stack.append(pa)
pa = n.get_child(pa, "response")

tree.add_node("agree", [], pa, {
    "unknown": "Glad you agree."
})
tree.add_node("disagree", [], pa, {
    "unknown": "Too bad you disagree."
})
tree.add_node("neutral", [], pa, {
    "unknown": "Hmmm..."
})
tree.add_node("feeling", [], pa, {
    "unknown": "I'm sorry, I don't have that emotion."
})

# topic > response > feeling : yikes, interested, awkward, confused, sad
stack.append(pa)
pa = n.get_child(pa, "feeling")

tree.add_node("yikes", [], pa, {
    "unknown": "Yikes."
})
tree.add_node("interested", [], pa, {
    "unknown": "I'm glad you're interested."
})
tree.add_node("awkward", [], pa, {
    "unknown": "Awkward..."
})
tree.add_node("confused", [], pa, {
    "unknown": "Huh?"
})
tree.add_node("sad", [], pa, {
    "unknown": ":')"
})

# topic > response :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic :
pa = stack.pop()

# topic > day : today
stack.append(pa)
pa = n.get_child(pa, "day")

tree.add_node("today", [], pa, {
    "unknown": "What about today?"
})

# topic :
pa = stack.pop()

# topic > date : current
stack.append(pa)
pa = n.get_child(pa, "date")

tree.add_node("current", [], pa, {
    "unknown": "What about our lil' date?"
})

print("Personality loaded")
