import pytholog as pl

def employment(ris):
    kb = pl.KnowledgeBase('Assunzione')

    kb([f"lang0(Java,{ris[0][0].lower()})",
        f"lang1(Python,{ris[0][1].lower()})",
        f"lang2(MySql,{ris[0][2].lower()})",
        f"lang3(Inglese,{ris[0][3].lower()})",

        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, X), lang2(MySql, X), lang3(Inglese,X), V is '100%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, Y), lang2(MySql, Y), lang3(Inglese,Y), V is '22%'",
        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, X), lang2(MySql, X), lang3(Inglese,Y), V is '88%' ",
        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, X), lang2(MySql, Y), lang3(Inglese,X), V is '77%'",
        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, Y), lang2(MySql, X), lang3(Inglese,X), V is '77%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, X), lang2(MySql, X), lang3(Inglese,X), V is '77%'",

        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, X), lang2(MySql, Y), lang3(Inglese,Y), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, Y), lang2(MySql, X), lang3(Inglese,Y), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, Y), lang2(MySql, Y), lang3(Inglese,X), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, X), lang2(MySql, X), lang3(Inglese,Y), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, Y), lang2(MySql, X), lang3(Inglese,X), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, X), lang2(MySql,Y), lang3(Inglese,X), V is '66%'",

        "prob(X,Y,V) :- lang0(Java, X), lang1(Python, Y), lang2(MySql, Y), lang3(Inglese,Y), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, X), lang2(MySql, Y), lang3(Inglese,Y), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, Y), lang2(MySql, X), lang3(Inglese,Y), V is '66%'",
        "prob(X,Y,V) :- lang0(Java, Y), lang1(Python, Y), lang2(MySql, Y), lang3(Inglese,X), V is '22%'",
        ])

    print(kb.query(pl.Expr("prob(yes,no,Probabilità_Assunzione)")))
