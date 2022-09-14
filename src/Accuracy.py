from sklearn.model_selection import cross_val_score
from statistics import mean
from sklearn.model_selection._split import LeaveOneOut

def accuracy(model,X, y):
    loo = LeaveOneOut()
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=loo)
    print(model,"L'accuratezza del sistema è: %f" % mean(scores))