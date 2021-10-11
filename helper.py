from dataObject import Debut, Fin
from dataObject import joueurs
from dataObject import pointsFaibles

def set_score(j1, ins1, j2, ins2):
    # TODO
    # fonction du nb de mots
    # ajouter des points si une insulte attaque un signe particulier de l'autre joueur
    print(j1.peculiarity + " : point faible du joueur1")
    print(j2.peculiarity + " : point faible du joueur2")
    ins1.append(Fin())
    ins2.append(Fin()) 
    g1 = verif_grammaire(ins1)
    g2 = verif_grammaire(ins2)
    print(f"grammaire joueur 1: {g1}")
    print(f"grammaire joueur 2: {g2}")
    bonus = 15
    if g1:
        j1.health += len(ins1) * 10
        for i in ins1:
            print(i)                #dir(i) renvoit la liste des propriétés de l'objet i
            if "signe_attaque" in dir(i)  and j2.peculiarity == i.signe_attaque:
                j1.health += bonus
    if g2:
        j2.health += len(ins2) * 10
        for i in ins2:
            print(i)
            if "signe_attaque" in dir(i)  and j1.peculiarity == i.signe_attaque:
                j2.health += bonus
    
     

# graphe de la grammaire            dsvclef = debut, sujet, verbe, complement, liaison , expresion final, Fin (les valeur possible phrase non correct)
grammaire = {                       #  la phrase gramaticalement correct si elle suit le chemin.
        'D': ['S'],  # Debut        #sujet
        'S': ['V', 'L'],            #verbe soit Liaison
        'V': ['C'],                 #complement
        'C': ['E', 'L', 'C', 'F'],  #Expression , liaison, complement( ccl ccd)
        'L': ['S'],                 #sujet
        'E': ['F'],  # Fin          # fin vide ou 'F'  #F 
        }
        

#

def verif_grammaire(insults):
    return verif_grammaire2([Debut()] + insults)

def verif_grammaire2(insults):
    if len(insults) < 2:
        return True
    else: 
        mot1 = type_mot(insults[0])
        mot2 = type_mot(insults[1])
    if mot2 in grammaire[mot1]:
        return verif_grammaire2(insults[1:])  # on retourne verif gramaire sur la queue de la liste (liste privée du premier element)
    else:
        return False


def type_mot(mot):
    # type(mot) retourne le nom de la classe
    # __name__ est le nom de la classe sous forme de chaine de caractère (string) ,[0] la première lettre du mot 
    return type(mot).__name__[0]    
