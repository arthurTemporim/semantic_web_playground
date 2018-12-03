from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from middleware import get_data, print_json, format_result

class ActionCheckRestaurants(Action):
   def name(self):
      return "action_get_chatbots"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      #chatbots= tracker.get_slot('chatbots')
      #return [SlotSet("matches", result if result is not None else [])]

      message = 'Eu conheço '

      result  = get_data('a chatbot:ChatBot')
      message += format_result(result)

      dispatcher.utter_message(message)
