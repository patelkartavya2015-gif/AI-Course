name = str(input("Hello there, I am AL, Please enter your name here: "))

print(f"Hi! nice to meet you {name}!")

mood = str(input("What's your mood today?").lower())

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad" or mood == "sad":
    print("I hope things get better❤️‍🩹")
else:
    print("Somtimes, it can be difficult to put emotions into words")

print(f"It was nice chatting with you {name}. Goodbye")