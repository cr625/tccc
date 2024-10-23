from owlready2 import *


def main():
    onto_path.append("data/")

    onto = get_ontology("data/bacteria.owl").load()
    cco = get_ontology("data/MergedAllCoreOntology.rdf").load()
    bfo = get_ontology("data/bfo-core").load()
    cco.base_iri = "http://www.ontologyrepository.com/CommonCoreOntologies/"
    obo = get_namespace("http://purl.obolibrary.org/obo/")

    # for c in cco.classes():
    #    print(c)
    # print(cco["Agent"])

    agent = cco.Agent
    print(agent.iri)
    print(agent.is_a)

    agent_parent = cco.search_one(is_a=obo.BFO_0000040)
    print(agent_parent)
    print(obo.BFO_0000040.label)
    print(agent_parent.label)


if __name__ == "__main__":
    main()
