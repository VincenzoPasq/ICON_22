from owlready2 import *

class Ontology:

    def __init__(self):
        self.ontology = get_ontology(os.path.basename("ontologia.owl")).load()
        self.dict_language = {}

    def get_language_descriptions(self):
        dict_language_onto = {}

        for i in self.ontology.individuals():
            dict_language_onto[str(i)] = i.Descrizione_linguaggio

        for k in dict_language_onto.keys():

            k1 = k
            k1 = k1.replace("ontologia.istanza_","")
            self.dict_language[k1] = dict_language_onto[k]


    def print_language(self):
        i = 1
        dict_nums_language = {}
        dict_nums_keys = {}

        for k in self.dict_language.keys():

            dict_nums_language[i] = self.dict_language[k]
            dict_nums_keys[i] = k
            i = i + 1

        return dict_nums_language, dict_nums_keys