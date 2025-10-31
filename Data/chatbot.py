# chatbot.py
# ----------------------------------------
# A simple rule-based chatbot for EV-related interactions
# ----------------------------------------

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! ⚡ I'm your EV assistant. How can I help you today?"
    elif "ev" in user_input or "electric vehicle" in user_input:
        return "Electric Vehicles (EVs) are eco-friendly cars that run on electricity instead of petrol or diesel."
    elif "battery" in user_input:
        return "EV batteries are usually lithium-ion, with capacities measured in kilowatt-hours (kWh)."
    elif "range" in user_input:
        return "The driving range of an EV depends on its battery capacity and efficiency, usually between 250–500 km."
    elif "price" in user_input or "cost" in user_input:
        return "EV prices vary widely — budget models start around $20,000, while luxury models can exceed $70,000."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Keep driving clean and green!"
    else:
        return "I'm not sure about that. Try asking me about EVs, batteries, or prices!"

if __name__ == "__main__":
    print("⚡ Welcome to the EV Chatbot! Type 'exit' to quit.\n")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! 👋 Stay charged!")
            break
        print("Chatbot:", chatbot_response(user_query))
