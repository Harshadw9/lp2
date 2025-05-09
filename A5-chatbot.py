def chatbot():
    print("ChatBot: Hello! Welcome to our Customer Support. How can I assist you today?")
    print("Type 'help' to see available options or 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "exit":
            print("ChatBot: Thank you for chatting with us! Have a great day!")
            break

        # Help menu
        elif user_input == "help":
            print("ChatBot: Here are the things I can assist you with:")
            print("1. Hours - Get store hours")
            print("2. Location - Find our store location")
            print("3. Services - Learn about our services")
            print("4. Support - Get technica]l support")
            print("Type any of the above keywords to get more information.")

        # Responses to user queries
        elif user_input == "hours" or "Hours":
            print("ChatBot: Our store is open from 9 AM to 9 PM, Monday to Saturday, and 10 AM to 6 PM on Sundays.")

        elif user_input == "location":
            print("ChatBot: We are located at 123 Main Street, Downtown City.")

        elif user_input == "services":
            print("ChatBot: We offer the following services: product consultation, repairs, and home delivery.")

        elif user_input == "support":
            print("ChatBot: For technical support, please email us at support@example.com or call us at +123-456-7890.")

        else:
            print("ChatBot: I'm sorry, I didn't understand that. Type 'help' for assistance.")

# Run the chatbot

chatbot()