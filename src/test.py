from owlready2 import *


def main():
    onto_path.append("data/")
    bon = get_ontology("bacteria.owl").load()

    onto = get_ontology("http://test.org/onto.owl#")
    set_log_level(9)

    with onto:

        class Bacterium(Thing):
            pass

        class Shape(Thing):
            pass

        class Grouping(Thing):
            pass

        class Rod(Shape):
            pass

        class MyBacterium(bon.Bacterium):
            pass

    print(onto.Bacterium)
    print(Bacterium.iri)
    print(bon.Bacterium)


if __name__ == "__main__":
    main()
