from owlready2 import get_ontology


def load_ontology(file_path="data/MergedAllCoreOntology.rdf"):
    """
    Load ontology from the given RDF/XML file path.
    :param file_path: Path to the RDF/XML file
    :return: Loaded ontology
    """
    try:
        # Load the ontology from the given RDF/XML file path
        ontology = get_ontology(f"file://{file_path}").load()
        print(f"Ontology loaded successfully from {file_path}")
        return ontology
    except Exception as e:
        print(f"Error loading ontology from {file_path}: {e}")
        return None
