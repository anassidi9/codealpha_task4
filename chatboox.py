def chatbot():
    print("Hello , I am a chatbot ! (type 'bye' to exit)")
    
    while True:
        message = input("You : ").lower()  # .lower() to ignore case
        
        if  "hello" in message:
            print("Bot : hi !")
        elif "bye" in message:
            print("Bot : Goodbye !")
            break  # on sort de la boucle
        elif "how are you" in message:
            print("Bot : I'm doing well, thank you !")
        else:
             print("Bot : Sorry, I didn't understand.")

chatbot()