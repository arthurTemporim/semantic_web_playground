# Report

This report its about the creation of an ontology about chatbots.

## Context

Since 2015 with the publish of the [Facebook API](https://developers.facebook.com/docs/messenger-platform/) enabling the usage of chatbots with users through facebook, many developers start to use this technology to many differents contexts.

The objective of this project is to describe the concept of **chatbot** and be able to fit any kind of chatbots using the proposed ontology.

## Objectives

* Describe the concept of **Chatbots** using ontology

* Be able to describe any chatbot using the proposed ontology

* Use the created ontology in a ChatBot

## Ontology

The following image shows the generated ontology diagram using [OWLViz](https://protegewiki.stanford.edu/wiki/OWLViz) that represents the first version of the **chatbot** ontology.

![ontology](images/chatbot.png)

The ontology can be find [here](https://github.com/arthurTemporim/semantic_web_playground/blob/master/project/chatbot.owl)

### Entities

All the entities have comments about the concept inside the **protegé**. Here is a explanation of why using each entity.

* Conversation

The conversation is the "instance" of the comunication between the chatbot and the person. This entity is relevante to contatain all messages that made part of the conversation

* Data

Data is where the message content is sotored, until now i didn't find nothing that is different between data and the concept of message in this ontology because this 2 things only makes sense to store some information.

* SoftwareAplication

It's an high level entity that represents any kind of software application relevant to this ontology.

* Bot

A bot is an automaton that is able to do some action triggered or not by and human action.

* ChatBot

Chatbots are automaton too bot the main objective of this kind of software application is to iteract through conversations with the user to do any kind of actions.

* WebCrawler
    Automaton responsible to get data from websites and format it to the necessary output.

* MessagingApplication

  [Telegram](https://telegram.org/), [Rocket.Chat](https://rocket.chat/) and [Facebook](http://facebook.com/) are examples of messaging applications that are necessary to allow the interation of the chatbots with the user (there are other ways to interact with chatbots too).

  * WebSite
  A collection of related web pages.


## Arquitecture

![semantic_web_bot](images/semantic_web_bot.png)

This is the used Architecture.

## Tools

The main tool to this part of the project was:

* [Protegé](https://protegewiki.stanford.edu/wiki/Main_Page)

* [OWLViz](https://protegewiki.stanford.edu/wiki/OWLViz)

* [Jena](https://jena.apache.org/)

* [RASA core](https://github.com/RasaHQ/rasa_core)

* [RASA nlu](https://rasa.com/docs/nlu/)

* [RASA core-sdk](rasa_core_sdk)

* [virtuoso](http://vos.openlinksw.com/owiki/wiki/VOS/VOSSQLRDF)


## References

* [Protegé Tutorial](https://www.youtube.com/watch?v=R9ERlUgvgwM&list=PLea0WJq13cnAfCC0azrCyquCN_tPelJN1)

* [Bot](https://pt.wikipedia.org/wiki/Bot)

* [Conversation](https://en.wikipedia.org/wiki/Conversation)

* [Message](https://en.wikipedia.org/wiki/Message)

* [Action](https://en.wikipedia.org/wiki/Action_(philosophy))

* [ChatBot](https://en.wikipedia.org/wiki/Chatbot)

* [WebSite](https://en.wikipedia.org/wiki/Website)

* [Data](https://en.wikipedia.org/wiki/Data)

* [Software Application](https://en.wikipedia.org/wiki/Application_software)

* [Message apps](https://en.wikipedia.org/wiki/Messaging_apps)

* [Turing Test](https://en.wikipedia.org/wiki/Turing_test)
