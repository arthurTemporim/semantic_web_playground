from SPARQLWrapper import SPARQLWrapper, JSON
import simplejson as json

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
        PREFIX dbpedia: <http://dbpedia.org/resource/>
        PREFIX dbpedia-ont: <http://dbpedia.org/ontology/>
        SELECT ?album
        WHERE { ?album dbpedia-ont:artist dbpedia:The_Beatles .}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(json.dumps(results, indent=4, sort_keys=True))
