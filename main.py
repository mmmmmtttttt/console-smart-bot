from datetime import datetime

t = datetime.now().time()
d = datetime.now().date()

help = ["hi", "time", "date", "help", "exit", "about"]
say_hello = ["hello", "Hello", "Hi", "hi"]

def small_bot():
    print("Bot: Hello, How to help you")
    while True:
        send = input("User: ").strip()
        if send == "time" or send == "Time":
            print(f"Bot: {t}")
        elif send == "date" or send == "Date":
            print(f"Bot: {d}")
        elif send in say_hello:
            print("Bot: Hello, how are you today?\nHow can I help you?")
        elif send == "help" or send == "Help":
            print(f"""
                        help:
                            {help}
                    """)
        elif send == "about" or send == "About":
            print("I am a small smart assistant. \n I answer some commands. \n If you want to know what those commands are, you can type help.")
        elif send == "exit" or send == "Exit":
            print("Bye, feel free to send if you need anything else.")
            break
        else:
            print("I did not understand the command. Write help to see the available commands.")
            with open("D:/GitHub/console-bot-project/not_recognized.txt", "a", encoding="utf-8") as file:
                file.write(send + "\n")
    

small_bot()