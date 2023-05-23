from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests


# Create a new chat bot
chatbot = ChatBot('WeatherBot')

# Create a new trainer for the chat bot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chat bot with the ChatterBot corpus data
trainer.train('chatterbot.corpus.english')


def get_weather(location):
    api_key = 'ad02582bb4752dab19650341186f730c'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant weather information from the response
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        return f"The weather in {location} is {description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information."

def get_bot_response(user_input):
    # Check if the user input contains a weather-related query
    if 'weather' in user_input:
        location = 'London'  # Extract the location from the user input, or set a default location
        return get_weather(location)
    else:
        # Generate a response using ChatterBot
        return str(chatbot.get_response(user_input))

# Example usage
user_input = input("User: ")
bot_response = get_bot_response(user_input)
print("Bot: " + bot_response)
