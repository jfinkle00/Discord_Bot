import random
from datetime import datetime
import requests


def make_calculation(message:str)->int:
    if message[0] in "0123456789" and message[1] not in "0123456789" and message[-1] in "0123456789" and message[-2] not in "0123456789":
        if message[2] == "+":
            return int(message[0]) + int(message[4])
        elif message[2] == "-":
            return int(message[0]) - int(message[4])
        elif message[2] == "/":
            return int(message[0]) / int(message[4])
        elif message[2] == "*" and message[3] != "*":
            return int(message[0]) * int(message[4])
        elif message[2] == "^":
            return int(message[0]) ** int(message[-1])
        elif message[2] == "%":
            return int(message[0]) % int(message[-1])
    elif message[0] in "0123456789" and message[1] in "0123456789" and message[-1] in "0123456789" and message[-2] in "0123456789":
        if message[3] == "+":
            return int(message[0:2]) + int(message[5:7])
        elif message[3] == "-":
            return int(message[0:2]) - int(message[5:7])
        elif message[3] == "/":
            return int(message[0:2]) / int(message[5:7])
        elif message[3] == "*":
            return int(message[0:2]) * int(message[5:7])
        elif message[3] == "^":
            return int(message[0:2]) ** int(message[5:7])
        elif message[3] == "%":
            return int(message[0:2]) % int(message[5:7])
    elif message[0] in "0123456789" and message[1] in "0123456789" and message[-1] in "0123456789" and message[-2] not in "0123456789":
        if message[3] == "+":
            return int(message[0:2]) + int(message[-1])
        elif message[3] == "-":
            return int(message[0:2]) - int(message[-1])
        elif message[3] == "/":
            return int(message[0:2]) / int(message[-1])
        elif message[3] == "*":
            return int(message[0:2]) * int(message[-1])
        elif message[3] == "^":
            return int(message[0:2]) ** int(message[-1])
        elif message[3] == "%":
            return int(message[0:2]) % int(message[-1])
    elif message[0] in "0123456789" and message[1] not in "0123456789" and message[-1] in "0123456789" and message[-2] in "0123456789":
        if message[2] == "+":
            return int(message[0]) + int(message[-2:])
        elif message[2] == "-":
            return int(message[0]) - int(message[-2:])
        elif message[2] == "/":
            return int(message[0]) / int(message[-2:])
        elif message[2] == "*":
            return int(message[0]) * int(message[-2:])
        elif message[2] == "^":
            return int(message[0]) ** int(message[-2:])
        elif message[2] == "%":
            return int(message[0]) % int(message[-2:])


def get_response(message:str)->str:
    p_message = message.lower()
    random_number = random.randint(1,8)
    random_number_small = random.randint(1,4)
    
    limit = 1

    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR API KEY HERE'})
    if response.status_code == requests.codes.ok:
        random_fact = response.text
    

    text_profanity = p_message
    api_url_profanity = 'https://api.api-ninjas.com/v1/profanityfilter?text={}'.format(text_profanity)
    response_profanity = requests.get(api_url_profanity, headers={'X-Api-Key': '"YOUR API KEY HERE'})
    if response_profanity.status_code == requests.codes.ok:
        profanity = response_profanity.text
    

    api_url_riddle = 'https://api.api-ninjas.com/v1/riddles'
    response_riddle = requests.get(api_url_riddle, headers={'X-Api-Key': 'YOUR API KEY HERE'})
    if response_riddle.status_code == requests.codes.ok:
        riddle = response_riddle.text


    if p_message[0:7] == "define:":
        word_def = p_message[8:]
        api_url_dic = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word_def)
        response_dic = requests.get(api_url_dic, headers={'X-Api-Key': 'YOUR API KEY HERE'})
        if response_dic.status_code == requests.codes.ok:
            definition = response_dic.text
            if len(definition) > 1965:
                definition = definition[0:1965] + "..."
        return "I believe that word means " + definition
    
    
    if "maple" and "define" in p_message:
        return "If you would like for me to define something for you type this - define: |your_word_here|"
    
    if "true" in profanity and "vibes" not in p_message:
        if random_number_small == 1:
            return "I do not appreaciate foul language in my server. 😡"
        elif random_number_small == 2:
            return "Grrrrr no more cursing please."
        else: 
            return "Growls* 🤬"

    if "maple" and "pet" in p_message:
        if random_number_small == 1:
            return "❤️"
        elif random_number_small == 2:
            return "Much appreciated 🐶"
        else:
            return "Sorry I am on duty right now and do not have time to accept pets :/"
    
    if p_message[0:5] == "food:":
        query = p_message[6:]
        api_url_food = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response_food = requests.get(api_url_food, headers={'X-Api-Key': 'YOUR API KEY HERE'})
        if response_food.status_code == requests.codes.ok:
            food_facts = response_food.text
            return "Here is my expert food analysis " + food_facts
    
    if "maple" and "food" in p_message or "maple" and "calories" in p_message:
        return "If you would like my expert food analysis type |food: your_food_here|"
        


    if p_message[0] in "0123456789" and p_message[-1] in "0123456789":
        return make_calculation(p_message)
    

    if p_message == "hello maple" or p_message == "hey maple" or p_message == "hi maple":
        if random_number == 1:
            return "Hey there! Hope your day is going well! :D"
        elif random_number == 2:
            return "Bark* Bark*"
        elif random_number == 3:
            return "Hi friend!"
        elif random_number == 4:
            return "Oh hey, didn't expect you to be here."
        elif random_number == 5:
            return "How's it going pal?"
        elif random_number == 6:
            return "Roof Roof"
        elif random_number == 7:
            return "😴"
        elif random_number == 8:
            return "👋"
        else:
            return "Hi!"
    



    if "time" in p_message and "maple" in p_message:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return "The current time is " + current_time
        
    if "roll" in p_message and "maple" in p_message:
        return str(random_number) + " is your roll 🎲"
    
    if p_message == "what can you do maple?" or "!commands" in p_message or p_message == "!help":
        return """Here is a list of my commands \n - Command List \n - hello maple \n - roll maple \n - how old are you maple? 
        \n - tell me a joke maple \n - what time is it maple? \n - Math: type |int operator int|
        \n - tell me a fact maple \n - weather: |cityname| \n - pet maple \n - food: |food_name| \n - define: |word| \n - maple tell me a riddle
        \n - vibes: |your message here|"""
    
    if "old" in p_message and "maple" in p_message:
        if random_number_small == 1:
            return "4 years and counting!"
        elif random_number_small == 2:
            return "I hardly think that is any of your business 🙄"
        else:
            return "28 🤭"
    
    if "weather" in p_message and "maple" in p_message:
        return "For a proper weather report type this - weather: city_name"
    if p_message[0:8] == "weather:":
        city = p_message[9:]
        api_url_weather = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
        response_weather = requests.get(api_url_weather, headers={'X-Api-Key': 'YOUR API KEY HERE'})
        if response_weather.status_code == requests.codes.ok:
            weather = response_weather.text 

        return "Here is your weather report! " + weather
    
    if "joke" in p_message and "maple" in p_message:
        if random_number == 1:
            return "A three-legged dog walks into a bar and says, I am looking for the man who shot my paw"
        elif random_number == 2:
            return "Outside of a dog, a book is mans best friend. Inside of the dog, it is too dark to read."
        elif random_number == 3:
            return "What do you get if you cross a Rottweiler and a hyena? I do not know but I recommend you join in if it laughs."
        elif random_number == 4:
            return "Have you heard about the guy who stole the calendar?! Well, he got 12 months!"
        elif random_number == 5:
            return "I stayed up all night and tried to figure out where the sun was. Then it dawned on me."
        elif random_number == 6:
            return "There are 10 kinds of people in the world. Those who understand binary and those who do not."
        elif random_number == 7:
            return "Programming is 10 percent writing code and 90 percent understanding why it is not working"
        elif random_number == 8:
            return "What did the Java Code say to the C code? You have got no class"
        else:
            return "Sorry I am out of jokes right now :/"
        
    if "maple" in p_message and "fact" in p_message:
        if random_number == 1:
            return "Here's a good one. " + random_fact[3:-2]
        elif random_number == 2:
            return "A personal favorite of mine. " + random_fact[3:-2]
        elif random_number == 3:
            return "This one is interesting. " + random_fact[3:-2]
        elif random_number == 4:
            return "Bet ya never heard of this. " + random_fact[3:-2]
        elif random_number == 5:
            return "🧠 " + random_fact[3:-2]
        elif random_number == 6:
            return "Good thing I graduated from petco university to learn this. " + random_fact[3:-2]
        else:
            return "🤯 " + random_fact
        
    if "vibes" in p_message and "maple" in p_message:
        return "To get my expert vibe analysis type |vibes: your_message|"
    
    if p_message[0:6] == "vibes:":
        text = p_message[7:]
        api_url_sentiment = 'https://api.api-ninjas.com/v1/sentiment?text={}'.format(text)
        response_sentiment = requests.get(api_url_sentiment, headers={'X-Api-Key': 'YOUR API KEY HERE'})
        if response_sentiment.status_code == requests.codes.ok:
            sentiment = response_sentiment.text
        return "According to my expert analysis... " + sentiment
    
    if "maple" and "riddle" in p_message:
        return riddle
    
    
    if "walk" in p_message:
        if random_number_small == 1:
            return "DID SOMEONE SAY WALK?!"
        elif random_number_small == 2:
            return "BARK!!!! BARK!!!! BARK!!!! BARK!!!!"
        elif random_number_small == 3:
            return "Tail wags in excitement***"
    
    if "maple" in p_message:
        return "Sorry I heard my name but did not quite understand what you said. Did you need something? Ask |what can you do maple?| or type |!commands| to see how I can be of assistance."
    

