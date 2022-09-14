import pandas as pd

class User(object):

    def __init__(self):
        self.Java = 'No'
        self.Python = 'No'
        self.MySql = 'No'
        self.Inglese = 'No'
        self.Titolo_di_Studio_0 = 'No'
        self.Titolo_di_Studio_1 = 'No'
        self.Titolo_di_Studio_2 = 'No'
        self.Esperienze_Pregresse_0_2 = 'No'
        self.Esperienze_Pregresse_3_6 = 'No'
        self.Esperienze_Pregresse_7_ = 'No'

    def getValues(self):
        df = pd.DataFrame.from_dict(vars(self), orient='index', dtype='string')
        return df

    def setTitolo_di_Studio_0(self, val):
        self.Titolo_di_Studio_0 = val

    def setTitolo_di_Studio_1(self, val):
        self.Titolo_di_Studio_1 = val

    def setTitolo_di_Studio_2(self, val):
        self.Titolo_di_Studio_2 = val

    def setJava(self, val):
        self.Java = val

    def setPython(self, val):
        self.Python = val

    def setMySql(self, val):
        self.MySql = val

    def setInglese(self, val):
        self.Inglese = val

    def setEsperienze_Pregresse_0_2(self, val):
        self.Esperienze_Pregresse_0_2 = val

    def setEsperienze_Pregresse_3_6(self, val):
        self.Esperienze_Pregresse_3_6 = val

    def setEsperienze_Pregresse_7_(self, val):
        self.Esperienze_Pregresse_7_ = val
