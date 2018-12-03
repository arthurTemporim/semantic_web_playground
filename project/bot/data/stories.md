## path 1
* greet
  - utter_greet
* goodbye
  -utter_goodbye

## path 2
* greet
  - utter_greet
* get_chatbots
  - action_get_chatbots

## path 3
* get_chatbots
  - action_get_chatbots
* goodbye
  -utter_goodbye

## path 4
* greet
  - utter_greet
* get_conversations
  - action_get_conversations

## path 5
* get_conversations
  - action_get_conversations
* goodbye
  -utter_goodbye

## path 6
* greet
  - utter_greet
* knows_knowunbrumenu
  - action_knows_knowunbrumenu

## path 7
* knows_knowunbrumenu
  - action_knows_knowunbrumenu
* goodbye
  -utter_goodbye

## path 8
* what_is{"class": "ChatBot"}
  - slot{"class": "ChatBot"}
  - action_what_is

## path 9
* what_is{"class": "Data"}
  - slot{"class": "Data"}
  - action_what_is
