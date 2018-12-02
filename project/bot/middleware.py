from SPARQLWrapper import SPARQLWrapper, JSON
import simplejson as json

sparql = SPARQLWrapper("https://jena.temposerver.ml/chatbot/query")
baseQuery = """
  prefix owl: <http://www.w3.org/2002/07/owl#>
  prefix chatbot: <https://jena.temposerver.ml/chatbot/#>
  SELECT ?conversation
  WHERE {
    ?conversation a chatbot:Conversation
  }
"""

def print_json(result):
    print(json.dumps(result, indent=4, sort_keys=True))

def get_data(data):
    sparql.setQuery(baseQuery)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

print_json(get_data('ChatBot'))
