def get_response(user_input):
    user_input = user_input.lower()
    
    #Defining Rules and Responses
    if user_input in ['hi', 'hello']:
        return "Hello there!"
    elif user_input == 'how are you?':
        return "I'm just a chatbot, but I'm here to help you!"
    elif user_input == "what is your name?":
        return " I'm a Chatbot"
    elif user_input == "how old are you?":
        return "I don't have an age like a human"
    elif user_input == "how do you work?":
        return "My responses are generated based on patterns in the data I've been trained on."
    elif user_input == "what is your favorite food?":
        return "I don't eat, so I don't have personal preferences."
    elif user_input == "what are some tips for improving productivity?":
        return "Set clear goals and priorities.Break tasks into smaller, manageable steps."
    elif user_input == "bye":
        return "Goodbye!Thanks for reaching out. Have a great day."
    else:
        return "I'm sorry, I don't understand that."

def main():
    print("ChatBot: Hi! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        # Checking for exit condition
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day.")
            break
        
        # Getting the chatbot response
        reply = get_response(user_input)
        print("ChatBot:", reply)

if __name__ == "__main__":
    main()
