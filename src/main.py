import pandas as pd
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.tree import DecisionTreeClassifier

from Accuracy import accuracy
from Interaction import questions
from Prolog import employment

# Visualizza il database
data = pd.read_csv("Assunzione.csv")

# Mostra le info del DataSet
X = data.drop(['Possibilità_Assunzione'], axis=1)
y = data.Possibilità_Assunzione

X = pd.get_dummies(X, dummy_na = False, columns=['Titolo_di_Studio','Esperienze_Pregresse'])
X.fillna(0, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=12)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

user = questions()
risp = user.getValues()
employment(risp)

for index, row in risp.iterrows():
    if(row[0] == 'Yes'):
        row[0]=1
    else:
        row[0]=0
risp = risp.T

p = model.predict(risp)
if (p[0] == 1):
    print("\nOttimo! Hai alte probabilità di essere richiamato per la candidatura all'interno di un'azienda!")
else:
    print("\nIl sistema ritiene che le conoscenze attuali non sono sufficienti per essere assunto.")
