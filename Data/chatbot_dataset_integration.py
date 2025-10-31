# chatbot_dataset_integration.py
# ----------------------------------------
# Chatbot integrated with EV dataset (cars_data_RAW_cleaned.csv)
# ----------------------------------------

import pandas as pd

# Load dataset
try:
    df = pd.read_csv("../data/cars_data_RAW_cleaned.csv")
except FileNotFoundError:
    print("⚠️ Dataset not found! Make sure the file exists in '../data/' folder.")
    exit()

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello there! ⚡ I'm your EV Data Assistant. How can I help you today?"

    # List available EVs
    elif "list" in user_input or "models" in user_input:
        models = ", ".join(df["Car_Name"].tolist())
        return f"Here are some EV models I know: {models}"

    # Find EV price
    elif "price" in user_input or "cost" in user_input:
        for car in df["Car_Name"]:
            if car.lower() in user_input:
                price = df.loc[df["Car_Name"] == car, "Price(USD)"].values[0]
                return f"The price of {car} is approximately ${price}."
        return "Please specify the car name (e.g., Tesla Model 3, TATA Nexon EV)."

    # Find EV range
    elif "range" in user_input:
        for car in df["Car_Name"]:
            if car.lower() in user_input:
                rng = df.loc[df["Car_Name"] == car, "Range(km)"].values[0]
                return f"The {car} offers a range of about {rng} km per charge."
        return "Could you tell me which car's range you'd like to know?"

    # Find EV charging time
    elif "charge" in user_input or "charging" in user_input:
        for car in df["Car_Name"]:
            if car.lower() in user_input:
                charge = df.loc[df["Car_Name"] == car, "Charging_Time(hr)"].values[0]
                return f"The {car} takes approximately {charge} hours to fully charge."
        return "Please mention the EV name for charging info."

    # Exit
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Keep exploring EV technology."

    else:
        return "I can tell you about EV prices, range, or charging times — just ask!"

if __name__ == "__main__":
    print("🚗 Welcome to the EV Dataset Chatbot! Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! 👋 Stay electric!")
            break
        print("Chatbot:", chatbot_response(query))
