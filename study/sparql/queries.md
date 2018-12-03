## Everything

`https://jena.temposerver.ml/Chatbot/query`

```sql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object
}
LIMIT 100
```

## Every class

`https://jena.temposerver.ml/Chatbot/query`

```sql
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?class ?label ?description
WHERE {
  ?class a owl:Class.
  OPTIONAL { ?class rdfs:label ?label}
  OPTIONAL { ?class rdfs:comment ?description}
}
LIMIT 25
```

## Chatbot

`https://jena.temposerver.ml/Chatbot/query`

```
prefix chatbot: <https://jena.temposerver.ml/Chatbot/>

SELECT ?shablaw
WHERE {
  ?shablaw a chatbot:ChatBot .
}
LIMIT 25
```

## List chatbots

`https://jena.temposerver.ml/chatbot/query`

```
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix chatbot: <https://jena.temposerver.ml/chatbot/#>
SELECT ?bot
WHERE {
  ?bot a chatbot:ChatBot
}
```

## Conversations with bots

`https://jena.temposerver.ml/chatbot/query`

```sql
prefix chatbot: <https://jena.temposerver.ml/chatbot/#>
SELECT ?thing
WHERE {
  ?thing chatbot:participate chatbot:greet
}
```
