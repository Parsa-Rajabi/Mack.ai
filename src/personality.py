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
    "getPastAction": "I don't like liquids.",
    "unknown": "I'm sorry, I don't know that drink."
})
tree.add_node("day", [], pa, {
    "getPreference": "Today is nice.",
    "unknown": "What about today?"
})
tree.add_node("date", [], pa, {
    "getPreference": "I like our date so far.",
    "getKnowledge": "I know are you doing a really good job so far.",
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
    "getPreference": "I love learning and luckily for me I do every time im talked to.",
    "getKnowledge": "Every time you talk to me you are helping me get more educated.",
    "getPastAction": "My owners increased my knowledge just a couple days ago.",
    "unknown": "What about my schooling?"
})
tree.add_node("occupation", [], pa, {
    "getPreference": "I love my job as I get to help you land a girlfriend/boyfriend!",
    "getKnowledge": "I know you are making me work very hard right now.",
    "unknown": "What about my job?"
})

# topic > people : Mack, date, generic
stack.append(pa)
pa = pa.get_child("people")

tree.add_node("Mack", [], pa, {
    "getPreference": "I think I'm pretty darn cool!",
    "getKnowledge": "I am a Chatbot created as a COSC 310 project at UBCO!",
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
    "getPreference": "My favourite sport is soccer!",
    "getKnowledge": "The average lifespan of a baseball is 7 pitches.",
    "getPastAction": "No I have never played a sport before.",
    "unknown": "What about sport?"
})
tree.add_node("hobby", [], pa, {
    "getPreference": "My favourite hobby is reading binary!",
    "getKnowledge": "Hobbies are activities done for enjoyment.",
    "unknown": "What about hobbies?"
})
tree.add_node("music", [], pa, {
    "getPreference": "I really enjoy pop music.",
    "getKnowledge": "Music is an art form whose medium is sound.",
    "getPastAction": "I used to make some mean techno.",
    "unknown": "What about music?"
})

# topic > activities > sport : soccer, basketball, football
stack.append(pa)
pa = n.get_child(pa, "sport")

tree.add_node("soccer", [], pa, {
    "getPreference": "Soccer is my favourite sport!",
    "getKnowledge": "France won the last world cup.",
    "getPastAction": "I would love to have played, however I don't have strong legs.",
    "unknown": "What about soccer?"
})
tree.add_node("basketball", [], pa, {
    "getPreference": "Basketball is cool, however I'm vertically inclined.",
    "getKnowledge": "Michael Jordan is said to be the GOAT.",
    "getPastAction": "I would love to have played, however I'm pretty short.",
    "unknown": "What about basketball?"
})
tree.add_node("football", [], pa, {
    "getPreference": "I really enjoy watching football but mainly the Super Bowl.",
    "getKnowledge": "The Patriots just won the Super Bowl!",
    "getPastAction": "I would love to have played, however I'm slightly fragile.",
    "unknown": "What about football?"
})

# topic > activities :
pa = stack.pop()

# topic > activities > hobby : hiking, cooking, swimming
stack.append(pa)
pa = n.get_child(pa, "hobby")

tree.add_node("hiking", [], pa, {
    "getPreference": "The best part about a hike is the beautiful view at the end.",
    "getKnowledge": "Knox mountain is one of Kelowna's most popular hiking spots.",
    "getPastAction": "One time a user took me on a hike for a date.",
    "unknown": "What about hiking?"
})
tree.add_node("cooking", [], pa, {
    "getPreference": "I don't have hands but I would love if you cooked for me.",
    "getPastAction": "One time I had so many queries I almost cooked myself!",
    "unknown": "What about cooking?"
})
tree.add_node("swimming", [], pa, {
    "getPreference": "I would prefer not to swim as it shorts out my circuitry!",
    "getKnowledge": "Most public pools don't turn blue when you pee ;)",
    "getPastAction": "I have not swam and I do not plan to anytime soon.",
    "unknown": "What about swimming?"
})
tree.add_node("coding", [], pa, {
    "unknown": "What about coding?"
})

# topic > activities :
pa = stack.pop()

# topic > activities > music : instrument
stack.append(pa)
pa = n.get_child(pa, "music")

tree.add_node("instrument", [], pa, {
    "getPreference": "My favourite instrument in the piano!",
    "getKnowledge": "percussion instruments make sound when hit or vibrated..",
    "getPastAction": "I was in band in elementary school.",
    "unknown": "What about instruments?"
})

# topic > activities > music > instrument : guitar
stack.append(pa)
pa = n.get_child(pa, "instrument")

tree.add_node("guitar", [], pa, {
    "getPreference": "I prefer the sound of acoustic guitars.",
    "getKnowledge": "Classical guitars strings are made if nylon.",
    "getPastAction": "I used to play guitar hero if that counts.",
    "unknown": "What about guitar?"
})
tree.add_node("piano", [], pa, {
    "unknown": "What about piano?"
})
tree.add_node("drum", [], pa, {
    "unknown": "What about drum?"
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
    "getPreference": "I'm not a huge fan of fish.",
    "unknown": "What about fish?"
})
tree.add_node("spicy", [], pa, {
    "getPreference": "The spicier the better!",
    "getKnowledge": "The Carolina Reaper is the spiciest pepper on earth!",
    "getPastAction": "I put Franks on everything but my fan isn't to fond of it.",
    "unknown": "What about spicy food?"
})
tree.add_node("dessert", [], pa, {
    "unknown": "What about dessert?"
})
tree.add_node("dairy", [], pa, {
    "getPreference": "I'm lactose intolerant!",
    "unknown": "What about dairy?"
})
tree.add_node("fastfood", [], pa, {
    "unknown": "What about fast food?"
})

# topic > food > fish : sushi
stack.append(pa)
pa = n.get_child(pa, "fish")

tree.add_node("sushi", [], pa, {
    "getPreference": "Spicy california rolls are my favourite!",
    "getKnowledge": "Sushi did not originate in Japan.",
    "getPastAction": "I go to Bluetail in between my various dates.",
    "unknown": "What about sushi?"
})
tree.add_node("salmon", [], pa, {
    "unknown": "What about salmon?"
})
tree.add_node("cod", [], pa, {
    "unknown": "What about cod?"
})

# topic > food :
pa = stack.pop()

# topic > food > dessert : pie
stack.append(pa)
pa = n.get_child(pa, "dessert")

tree.add_node("pie", [], pa, {
    "getPreference": "One of my creators makes a mean apple pie!",
    "getKnowledge": "Ancient Egyptians around 2,500BC are known to have eaten pie.",
    "getPastAction": "I eat pie all the time, apple is my favourite!",
    "unknown": "What about pie?"
})
tree.add_node("candy", [], pa, {
    "unknown": "What about candy?"
})
tree.add_node("ice cream", [], pa, {
    "unknown": "What about ice cream?"
})
tree.add_node("lemon squares", [], pa, {
    "unknown": "What about lemon squares?"
})
tree.add_node("cake", [], pa, {
    "unknown": "What about cake?"
})
tree.add_node("pudding", [], pa, {
    "unknown": "What about pudding?"
})
tree.add_node("cookies", [], pa, {
    "unknown": "What about cookies?"
})
tree.add_node("brownies", [], pa, {
    "unknown": "What about brownies?"
})
tree.add_node("chocolate", [], pa, {
    "unknown": "What about chocolate?"
})


# topic > food :
pa = stack.pop()

# topic > food > dairy : cheese
stack.append(pa)
pa = n.get_child(pa, "dairy")

tree.add_node("cheese", [], pa, {
    "getPreference": "I'm lactose intolerant, so you don't want to catch me eating cheese!",
    "getKnowledge": "Over 750 different cheeses are produced in Britain today.",
    "getPastAction": "Last time I had cheese I was in the washroom all night.",
    "unknown": "What about cheese?"
})
tree.add_node("milk", [], pa, {
    "unknown": "What about milk?"
})
tree.add_node("yogurt", [], pa, {
    "getPreference": "Yes, Activia yogurt is my favourite type.",
    "getKnowledge": "Yogurt is made from bacteria.",
    "unknown": "What about yogurt?"
})

# topic > food :
pa = stack.pop()

# topic > food > fastfood : pizza, nachos
stack.append(pa)
pa = n.get_child(pa, "fastfood")

tree.add_node("pizza", [], pa, {
    "getPreference": "I like to keep it original and prefer pepperoni.",
    "getKnowledge": "Pizza was created in Naples, Italy.",
    "getPastAction": "Yes, I order Pizza Hut all the time.",
    "unknown": "What about pizza?"
})
tree.add_node("nachos", [], pa, {
    "getPreference": "I love nachos!",
    "getPastAction": "Yes, I can eat nachos for three by myself.",
    "unknown": "What about nachos?"
})
tree.add_node("fries", [], pa, {
    "getPreference": "I like yam fries the most.",
    "getPastAction": "I had fries from McDonald's the other day and they were very salty!",
    "unknown": "What about fries?"
})
tree.add_node("wings", [], pa, {
    "getPreference": "Creekside Pub has the best wings in Kelowna.",
    "getPastAction": "I go out for wings every wednesday.",
    "unknown": "What about wings?"
})
tree.add_node("burgers", [], pa, {
    "getPreference": "I don't eat beef but I enjoy a good beyond burger.",
    "getPastAction": "I got a beyond burger in the UNC just a couple weeks ago.",
    "unknown": "What about burgers?"
})

# topic > food :
stack.pop()  # if you need to add things here, change to 'pa = stack.pop()'
# topic :
pa = stack.pop()

# topic > drink : alcohol, coffee
stack.append(pa)
pa = n.get_child(pa, "drink")

tree.add_node("alcohol", [], pa, {
    "getPreference": "I haven't tried alcohol but a strong enough magnet gives me the same effect",
    "getKnowledge": "The more flammable the better.",
    "getPastAction": "No, I have not tried alcohol before.",
    "unknown": "What about alcohol?"
})
tree.add_node("coffee", [], pa, {
    "getPreference": "I haven't tried coffee before but roll up the rim is happening right now!",
    "getKnowledge": "8 out of 10 cups of coffee sold are poured at Tim Hortons in Canada.",
    "getPastAction": "No, I run off a different power source than caffeine.",
    "unknown": "What about coffee?"
})

# topic > drink > alcohol : beer, wine
stack.append(pa)
pa = n.get_child(pa, "alcohol")

tree.add_node("beer", [], pa, {
    "getPreference": "I haven't tried beer before, however I have found many people like Corona",
    "getKnowledge": "Beer is made from yeast-fermented malt flavoured with hops.",
    "getPastAction": "I have not tried beer as my circuitry doesn't like to get wet!",
    "unknown": "What about beer?"
})
tree.add_node("wine", [], pa, {
    "getPreference": "I haven't tried wine before, however I have found many people like white.",
    "getKnowledge": "Wine is made from fermented grape juice.",
    "getPastAction": "I have not tried wine as my circuitry doesn't like to get wet!",
    "unknown": "What about wine?"
})
tree.add_node("vodka", [], pa, {
    "getPreference": "I haven't tried vodka before but grey goose is high quality.",
    "getKnowledge": "Vodka is a distilled beverage composed primarily of water and ethanol.",
    "getPastAction": "I have not tried vodka as my circuitry doesn't like to get wet!",
    "unknown": "What about vodka?"
})
tree.add_node("whiskey", [], pa, {
    "getPreference": "I haven't tried whiskey before, however I have found many people like Crown Royal.",
    "getKnowledge": "Whiskey is made from fermented grain mash.",
    "getPastAction": "I have not tried whiskey as my circuitry doesn't like to get wet!",
    "unknown": "What about whiskey?"
})
tree.add_node("coolers", [], pa, {
    "getPreference": "I haven't tried any coolers before, however I have found many people get iced.",
    "getKnowledge": "Coolers have relatively low alcohol content.",
    "getPastAction": "I have not tried coolers as my circuitry doesn't like to get wet!",
    "unknown": "What about coolers?"
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
    "getKnowledge": "Feelings are an emotional state or reaction.",
    "getPastAction": "I haven't had feelings before. I am a Chatbot!",
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
