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
classQuery = """
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix chatbot: <https://jena.temposerver.ml/chatbot/#>

SELECT DISTINCT ?class ?description
WHERE {
  ?class a owl:Class.
  OPTIONAL { ?class rdfs:comment ?description}
}
"""

def print_json(result):
    print(json.dumps(result, indent=4, sort_keys=True))

def get_data(data='', query=baseQuery):
    try:
        if data != '':
            sparql.setQuery(query.format(data))
        else:
            sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
    except ValueError:
        print(ValueError)
    return sparql.query().convert()

def format_result(result=None, queryType='base', className=None):
    data = ''
    try:
        content = result['results']['bindings']
    except ValueError:
        print(ValueError)
    if queryType == 'base':
        for i in range(len(content)):
            data += content[i]['thing']['value'].split('#')[1].capitalize()
            if len(content) == 2:
                data +=' and '
            elif i+1 < len(content):
                data +=', '
    elif queryType == 'class':
        for i in range(len(content)):
            if content[i]['class']['value'].split('#')[1].lower() == className:
                data += content[i]['description']['value'].strip('\"\\\"')
    return data

# List bots
#print_json(get_data('a chatbot:ChatBot'))
# List Conversations
#print_json(get_data('a chatbot:Conversation'))
# List bots able to talk about something
#print_json(get_data('chatbot:participate chatbot:greet'))
#print_json(get_data('chatbot:participate chatbot:knowUnbRuMenu'))
#print_json(format_result(get_data(query=classQuery), 'class', 'ChatBot'))
