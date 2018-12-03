from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from middleware import get_data, print_json, format_result, classQuery

API_CONNECTION_ERROR = 'I had a problem while trying to get the data =/'

class ActionGetChatbots(Action):
   def name(self):
      return "action_get_chatbots"

   def run(self, dispatcher, tracker, domain):
      message = 'I know '

      try:
         result  = get_data('a chatbot:ChatBot')
         message += format_result(result)
      except ValueError:
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
      except ValueError:
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
      except ValueError:
         message = API_CONNECTION_ERROR

      dispatcher.utter_message(message)

class ActionWhatIs(Action):
   def name(self):
      return "action_what_is"

   def run(self, dispatcher, tracker, domain):
      tslot = tracker.get_slot('class').lower()
      if tslot not in domain['slots']['class']['values']:
         dispatcher.utter_message("Sorry, i don't know this concept yet =/")
      elif tslot != None:
         try:
            dispatcher.utter_message("You are asking about: ")
            dispatcher.utter_message(tslot)
            dispatcher.utter_message(format_result(get_data(query=classQuery), 'class', tslot))
         except ValueError:
            dispatcher.utter_message(API_CONNECTION_ERROR)
      else:
         dispatcher.utter_message("You need to tell what you want to know ;)")
