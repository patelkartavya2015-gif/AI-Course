import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}🐍 Welcome to Sentimant spy! 🐍{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please Enter Your username: {Style.RESET_ALL}")

if not user_name:
    user_name = "Mystery Agent"
conversation_history = []

print(f"\n {Fore.CYAN}Hello Agent {user_name}")
print(f"Type a scentence")
print(f"Type {Fore.YELLOW}reset to reset your history, history to show your history, exit to quit.")

while True:
    user_input = input(f"{Fore.RED}Enter here!")

    if not user_input:
        print(f"{Fore.RED}Please enter Valid details")

    elif user_input.lower() == "exit":
        print(f"Exiting Sentimant Spy, farewell agent {Fore.CYAN} Agent {user_name}")
        break
    elif user_input == "reset":
        print(f"{Fore.BLUE} Deleting your history...")
        conversation_history.clear()
        print(f"{Fore.GREEN}Data Reset!")
    elif user_input == "history":
        if not conversation_history:
            print("No data?")
        for idx, (text, polaratity, sentiment_type) in enumerate(conversation_history, start=-1):
            if sentiment_type == "Positive":
                color = Fore.GREEN
                emoji = "😃"
            elif sentiment_type == "Negative":
                color = Fore.RED
                emoji = "😢"
            else:
                color = Fore.GREEN
                emoji = "😑"

            print(f"{idx}. {color}{emoji} {text}"
                  f"Polarity: {polaratity:.2f}, {sentiment_type}{Style.RESET_ALL}")

            continue

    polaratity = TextBlob(user_input).sentiment.polarity
    if polaratity > 0.25:
            sentiment_type = "Positive"
            color = Fore.GREEN
            emoji = "😃"
    elif polaratity < -0.25:
            sentiment_type = "Negative"
            color = Fore.RED
            emoji = "😢"
    else:
            sentiment_type = "Nuteral"
            color = Fore.GREEN
            emoji = "😑"

    conversation_history.append((user_input, polaratity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type}, semtiment! Polarity: {polaratity:.2f}")

