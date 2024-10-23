from owlready2 import *

onto_path.append("/path/to/your/local/ontology/repository")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()
