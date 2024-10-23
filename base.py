from owlready2 import *

# Load the BFO ontology from an online OWL file (or you can use a local file path)
bfo = get_ontology("http://purl.obolibrary.org/obo/bfo.owl").load()
cco = get_ontology("CommonCoreOntologiesMerged.rdf").load()

# Verify that the ontology loaded successfully
print(cco)

# List classes to explore the ontology structure
for cls in cco.classes():
    print(cls)

# Verify the ontology loaded
