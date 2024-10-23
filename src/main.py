from owlready2 import *


def main():
    # Load the ontology from RDF/XML
    onto = get_ontology("data/CommonCoreOntologiesMerged.rdf").load()

    # Print the classes in the ontology
    print("Classes in the ontology:")
    for cls in onto.classes():
        print(cls)

    # Access the class by IRI or search for it
    education_artifact_function_class = onto.search_one(
        iri="http://www.ontologyrepository.com/CommonCoreOntologies/EducationArtifactFunction"
    )

    if education_artifact_function_class:
        print(f"Class found: {education_artifact_function_class}")
    else:
        print("Class not found.")

    class EducationArtifactFunction(onto.EducationArtifactFunction):
        equivalent_to = [onto.EducationArtifact]


if __name__ == "__main__":
    main()
