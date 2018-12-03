from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3
from rdflib import Graph 
import simplejson as json

sparql = SPARQLWrapper("https://jena.temposerver.ml/chatbot/query")
baseQuery = """
  prefix chatbot: <https://jena.temposerver.ml/chatbot/#>
  SELECT ?thing
  WHERE {{
    ?thing {}
  }}
"""

def print_json(result):
    print(json.dumps(result, indent=4, sort_keys=True))

def get_data(data):
    sparql.setQuery(baseQuery.format(data))
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

def format_result(result):
    data = ''
    content = result['results']['bindings']
    for i in range(len(content)):
        data += content[i]['thing']['value'].split('#')[1].capitalize()
        if i+1 < len(content):
            data +=', '
    return data

# List bots
#print_json(get_data('a chatbot:ChatBot'))
# List Conversations
#print_json(get_data('a chatbot:Conversation'))
# List bots able to talk about something
#print_json(get_data('chatbot:participate chatbot:greet'))
#print_json(get_data('chatbot:participate chatbot:knowUnbRuMenu'))
