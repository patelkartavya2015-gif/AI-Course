import re, colorama, random

from colorama import Fore, init



init(autoreset = True)



destinations = {
    "beaches" : ["Bali", "Maldives", "Hawaii", "Phuket", "Bahamas"],
    "mountains" : ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Dolomites"],
    "cities" : ["New York", "Paris", "Tokyo", "London", "Sydney"],
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the bicycle fall over? Because it was two-tired!",
]



def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.strip().lower())


def recommend():
    print(Fore.CYAN + "Travel bot : Beaches, Mountains, Cities?")
    preference = input(Fore.GREEN + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.CYAN + f"Travel bot : I recommend visiting {suggestion}!")
        print(Fore.CYAN + "Travel bot : Do you want to go there? (yes/no)")
        answer = input(Fore.GREEN + "You: ").lower()

        if answer == "yes":
            print(Fore.CYAN + "Travel bot : Great! Have a wonderful trip!")
        elif answer == "no":
            print(Fore.CYAN + "Travel bot : Lets try again!")
            recommend()
        else:
            print(Fore.CYAN + "Travel bot : I didn't understand that. Let's try again!")
    else:
        print(Fore.RED + "Travel bot : Sorry, I don't have recommendations for that. Please choose from Beaches, Mountains, or Cities.")

def packing():
    print(Fore.CYAN + "Travel bot : What type of trip are you going on? (beach/mountain/city)")
    trip_type = input(Fore.GREEN + "You: ")
    trip_type = normalize_input(trip_type)

    print(Fore.CYAN + "Travel bot : How many days?")
    days = input(Fore.GREEN + "You: ")

    print(Fore.GREEN + f"Travel bot : For a {days}-day {trip_type} trip, you should pack:")
    print(Fore.GREEN + "Versatile clothes")
    print(Fore.GREEN + "adapter")
    print(Fore.GREEN + "check forcast of weather")

def tell_joke():
    print(Fore.CYAN + "Travel bot : Here's a joke for you:", Fore.YELLOW + random.choice(jokes))


def help():
    print(Fore.MAGENTA + "\n I can:")
    print(Fore.CYAN + "1. Recommend a travel destination(reccomend is command)")
    print(Fore.CYAN + "2. Help with packing(help is command)")
    print(Fore.CYAN + "3. Tell a joke(joke is command)")
    print(Fore.CYAN + "4. Exit(exit is command)")


def chat():
    print(Fore.CYAN + "Travel bot : Hello! I'm your travel assistant. How can I help you today?")
    name = input(Fore.GREEN + "You: ")
    print(Fore.CYAN + f"Travel bot : Nice to meet you, {name}!")


    while True:
        help()
        userinput = input(Fore.GREEN + "You: ")
        userinput = normalize_input(userinput)

        if userinput.lower() == "recommend":
            recommend()
        elif userinput.lower() == "help":
            packing()
        elif userinput.lower() == "joke":
            tell_joke()
        elif userinput.lower() == "exit":
            print(Fore.CYAN + "Travel bot : Goodbye! Have a great trip!")
            break
        else:
            print(Fore.RED + "Travel bot : Sorry, I didn't understand that. Please type 'recommend', 'help', 'joke', or 'exit'.")


if __name__ == "__main__":
    chat()