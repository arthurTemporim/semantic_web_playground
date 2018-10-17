# SPARQL

## RDF

RDF is a directed, labeled graph data format for representing information in the Web. RDF is often used to represent, among other things, personal information, social networks, metadata about digital artifacts, as well as to provide a means of integration over disparate sources of information. This specification defines the syntax and semantics of the SPARQL query language for RDF.

## SPARQL

The SPARQL query language for RDF is designed to meet the use cases and requirements identified by the RDF Data Access Working Group in RDF Data Access Use Cases and Requirements [UCNR]. 

## Methods

The code in `queries` directory about the methods bellow its from SPARQLWrapper documentation.

* [SELECT query](https://www.w3.org/TR/rdf-sparql-query/#select)

    The SELECT form of results returns variables and their bindings directly. The syntax SELECT * is an abbreviation that selects all of the variables in a query.

* [ASK query](https://www.w3.org/TR/rdf-sparql-query/#ask)

    Applications can use the ASK form to test whether or not a query pattern has a solution. No information is returned about the possible query solutions, just whether or not a solution exists.

* [CONSTRUCT query](https://www.w3.org/TR/rdf-sparql-query/#construct)

    The CONSTRUCT query form returns a single RDF graph specified by a graph template. The result is an RDF graph formed by taking each query solution in the solution sequence, substituting for the variables in the graph template, and combining the triples into a single RDF graph by set union.

* [DESCRIBE query](https://www.w3.org/TR/rdf-sparql-query/#describe)

The DESCRIBE form returns a single result RDF graph containing RDF data about resources. This data is not prescribed by a SPARQL query, where the query client would need to know the structure of the RDF in the data source, but, instead, is determined by the SPARQL query processor. The query pattern is used to create a result set. The DESCRIBE form takes each of the resources identified in a solution, together with any resources directly named by IRI, and assembles a single RDF graph by taking a "description" which can come from any information available including the target RDF Dataset. The description is determined by the query service. The syntax DESCRIBE * is an abbreviation that describes all of the variables in a query.

## References

* [RDF sparql query](https://www.w3.org/TR/rdf-sparql-query/)
* [sparqlwrapper package](https://pypi.org/project/SPARQLWrapper/)
* [sparqlwrapper documentation](https://rdflib.github.io/sparqlwrapper/)
* [Ontobee](http://www.ontobee.org/tutorial/sparql/)
* [RDF example](https://jena.apache.org/tutorials/sparql_data_pt.html)
