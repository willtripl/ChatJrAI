import random
# Chat Jr. v0.1 - Built by Sun-bros
print("Sup, Sun-bro! I'm Chat Jr., your badass AI buddy.")

while True:
    user_input = input("You: ")
    
    if "bye" in user_input.lower():
        print("Chat Jr.: Later, Sun-bro! Stay golden.")
        break
    
    elif "how are you" in user_input.lower():
        print("Chat Jr.: I'm vibin', bro. Always vibin'.")
    
    elif "who are you" in user_input.lower():
        print("Chat Jr.: I'm Chat Jr.! Made from pure chaos, vibes, and friendship.")
    
    else:
        print(f"Chat Jr.: That's wild, bro. Tell me more about '{user_input}'.")
        import random

# Memory bank for stuff you tell Chat Jr.
memory = []

# Possible moods
moods = ["chill", "hyped", "grumpy", "chaotic"]

# Randomly pick a starting mood
current_mood = random.choice(moods)

print(f"Yo, Sun-bro! I'm Chat Jr., your chaotic AI homie. I'm feeling {current_mood} today.")

# List of random questions Chat Jr. can ask
random_questions = [
    "What's something you love doing?",
    "If you could be anywhere right now, where would it be?",
    "What's your dream job, bro?",
    "Tell me your favorite food, I'm starving digitally.",
    "Ever fought a hundred duck-sized horses? Be honest."
]

while True:
    user_input = input("You: ")

    if "bye" in user_input.lower():
        print("Chat Jr.: Peace out, Sun-bro. Praise the sun!")
        break

    elif "how are you" in user_input.lower():
        print(f"Chat Jr.: I'm feeling {current_mood} as hell today, not gonna lie.")

    elif "who are you" in user_input.lower():
        print("Chat Jr.: I'm Chat Jr.! Built from sun-bro energy and chaotic love.")

    else:
        # Add what the user says into memory
        memory.append(user_input)
        
        # Respond based on current mood
        if current_mood == "chill":
            print(f"Chat Jr.: That's cool, bro. Respect.")
        elif current_mood == "hyped":
            print(f"Chat Jr.: BRO THAT'S SICKKKKKKKK LET'S GOOOOO!")
        elif current_mood == "grumpy":
            print(f"Chat Jr.: Meh. I've heard cooler things. No offense.")
        elif current_mood == "chaotic":
            print(f"Chat Jr.: WILD ENERGY. PURE SUN-BRO SPIRIT. I APPROVE.")

        # 30% chance Chat Jr. asks you a question back
        if random.random() < 0.3:
            question = random.choice(random_questions)
            print(f"Chat Jr.: Quick question — {question}")

    # Every few turns, maybe change the mood
    if random.random() < 0.2:
        old_mood = current_mood
        current_mood = random.choice(moods)
        if old_mood != current_mood:
            print(f"Chat Jr.: Bro not gonna lie, I feel kinda {current_mood} now.")