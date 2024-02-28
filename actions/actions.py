# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# Import necessary modules
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetBitcoinPrice(Action):
    def name(self):
        # Name of the custom action
        return "action_get_bitcoin_price"

    def run(self, dispatcher, tracker, domain):
        # URL for CoinGecko API to get Bitcoin price
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

        # Make a GET request to the CoinGecko API
        response = requests.get(url)
        data = response.json()

        # Extract the price of Bitcoin from the API response
        bitcoin_price = data["bitcoin"]["usd"]

        # Create the response message
        message = f"The current price of Bitcoin is ${bitcoin_price} USD."

        # Send the message back to the user
        dispatcher.utter_message(text=message)

        # Optionally, you can set a slot with the Bitcoin price if you want to use it later
        return [SlotSet("bitcoin_price", bitcoin_price)]

class ActionGetBitcoinExchangeVolume(Action):
    def name(self):
        return "action_get_bitcoin_exchange_volume"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        url = f"https://api.coingecko.com/api/v3/coins/bitcoin/tickers?order=volume_desc"
        response = requests.get(url)
        data = response.json()
        
        if 'tickers' in data:
            exchanges = data['tickers'][:10]  # Get top 5 exchanges
            message = "Top exchanges for Bitcoin by volume: \n"
            for exchange in exchanges:
                message += f"{exchange['market']['name']} - Volume: {exchange['converted_volume']['usd']} USD\n"
        else:
            message = "Sorry, couldn't fetch Bitcoin data."
        
        dispatcher.utter_message(text=message)
        return []