from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from middleware import get_data, print_json, format_result

API_CONNECTION_ERROR = 'I had a problem while trying to get the data =/'

class ActionGetChatbots(Action):
   def name(self):
      return "action_get_chatbots"

   def run(self, dispatcher, tracker, domain):
      message = 'I know '

      try:
         result  = get_data('a chatbot:ChatBot')
         message += format_result(result)
      except e:
         message = API_CONNECTION_ERROR

      dispatcher.utter_message(message)

class ActionGetConversations(Action):
   def name(self):
      return "action_get_conversations"

   def run(self, dispatcher, tracker, domain):
      message = 'All ChatBots that i know can talk about '

      try:
          result  = get_data('a chatbot:Conversation')
          message += format_result(result)
      except e:
          message = API_CONNECTION_ERROR

      dispatcher.utter_message(message)

class ActionKnowsKnowUnbRuMenu(Action):
   def name(self):
      return "action_knows_knowunbrumenu"

   def run(self, dispatcher, tracker, domain):
      message = 'Who knows talk about it is '
      try:
         result  = get_data('chatbot:participate chatbot:knowUnbRuMenu')
         result = format_result(result)
         message += result
      except e:
         message = API_CONNECTION_ERROR

      dispatcher.utter_message(message)
