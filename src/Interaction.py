from Ontology import Ontology
from User import User

def questions():
    ont = Ontology()
    ont.get_language_descriptions()
    language, keys_language = ont.print_language()

    print("\nBenvenuto nel sistema in grado di predire la probabilità di assunzione durante i colloqui con le Aziende.\n\
Di seguito verranno fatte domande inerenti alle abilità informatiche di cui si è in possesso.\n")
    print("Le risposte devono essere date nei possibili seguenti modi:\n Per il titolo di studio inserire: \n\
    -> 0 (NON DIPLOMATO)\n\
    -> 1 (DIPLOMATO)\n\
    -> 2 (LAUREATO)\
     \n Per i linguaggi informatici conosciuti utilizzare\n\
    -> si,s\n\
    -> no,n\n\
    -> info (per comprendere i requisiti del linguaggio richiesti)\
    \n Per indicare l'esperienza lavorativa, indicare il numero di anni di lavoro nell'ambito informatico\n")
    utente = User()

    while (True):
        print('Di che titolo di studio sei in possesso?')
        utente.setTitolo_di_Studio_0(input(''))
        if utente.Titolo_di_Studio_0.__eq__('0'):
            utente.setTitolo_di_Studio_0('Yes')
            break
        elif utente.Titolo_di_Studio_0.__eq__('1'):
            utente.setTitolo_di_Studio_1('Yes')
            utente.setTitolo_di_Studio_0('No')
            break
        elif utente.Titolo_di_Studio_0.__eq__('2'):
            utente.setTitolo_di_Studio_2('Yes')
            utente.setTitolo_di_Studio_0('No')
            break

    while (True):
        print("Conosci il linguaggio Java?")
        utente.setJava(input(''))
        if utente.Java.__eq__('si') or utente.Java.__eq__('s'):
            utente.setJava('Yes')
            break
        elif utente.Java.__eq__('no') or utente.Java.__eq__('n'):
            utente.setJava('No')
            break
        elif utente.Java.__eq__('info'):
            print("Linguaggio: %s, descrizione: %s" % (keys_language[2], " ".join(language[2])))

    while (True):
        print("Conosci il linguaggio MySql?")
        utente.setMySql(input(''))
        if utente.MySql.__eq__('si') or utente.MySql.__eq__('s'):
            utente.setMySql('Yes')
            break
        elif utente.MySql.__eq__('no') or utente.MySql.__eq__('n'):
            utente.setMySql('No')
            break
        elif utente.MySql.__eq__('info'):
            print("Linguaggio: %s, descrizione: %s" % (keys_language[3], " ".join(language[3])))

    while (True):
        print("Conosci il linguaggio Python?")
        utente.setPython(input(''))
        if utente.Python.__eq__('si') or utente.Python.__eq__('s'):
            utente.setPython('Yes')
            break
        elif utente.Python.__eq__('no') or utente.Python.__eq__('n'):
            utente.setPython('No')
            break
        elif utente.Python.__eq__('info'):
            print("Linguaggio: %s, descrizione: %s" % (keys_language[4], " ".join(language[4])))

    while (True):
        print("Conosci la lingua Inglese?")
        utente.setInglese(input(''))
        if utente.Inglese.__eq__('si') or utente.Inglese.__eq__('s'):
            utente.setInglese('Yes')
            break
        elif utente.Inglese.__eq__('no') or utente.Inglese.__eq__('n'):
            utente.setInglese('No')
            break
        elif utente.Inglese.__eq__('info'):
            print("Linguaggio: %s, descrizione: %s" % (keys_language[1], " ".join(language[1])))

    while (True):
        print("Quanti anni hai di esperienza lavorativa?")
        utente.setEsperienze_Pregresse_0_2(input(''))
        if (utente.Esperienze_Pregresse_0_2.__eq__('0') or utente.Esperienze_Pregresse_0_2.__eq__(
                '1') or utente.Esperienze_Pregresse_0_2.__eq__(
                '2')):
            utente.setEsperienze_Pregresse_0_2('Yes')
            break
        elif (utente.Esperienze_Pregresse_0_2.__eq__('3') or utente.Esperienze_Pregresse_0_2.__eq__(
                '4') or utente.Esperienze_Pregresse_0_2.__eq__('5')
              or utente.Esperienze_Pregresse_0_2.__eq__('6')):
            utente.setEsperienze_Pregresse_3_6('Yes')
            utente.setEsperienze_Pregresse_0_2('No')
            break
        elif (utente.Esperienze_Pregresse_0_2.isnumeric()):
            if (int(utente.Esperienze_Pregresse_0_2) >= 7):
                utente.setEsperienze_Pregresse_7_('Yes')
                utente.setEsperienze_Pregresse_0_2('No')
                break

    return utente
