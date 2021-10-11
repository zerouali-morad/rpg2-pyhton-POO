from random import shuffle


# les personnages
class Joueur(object):
    def __init__(self, name, peculiarity): 
        self.name = name
        self.peculiarity = peculiarity  
        self.health = 0

# variables point faible players
vieux = "vieux"
obese = "obese"
blonde = "blonde"
lunettes = "lunettes"  # eventuellement utiliser la classe enum
chauve = "chauve"


pointsFaibles = [vieux, obese, blonde, lunettes, chauve]


Robert = Joueur("Robert", obese)
Charles = Joueur("Charles", lunettes)
Denise = Joueur("Denise", blonde)
Ernest = Joueur("Ernest", vieux)

joueurs = [Robert, Charles, Denise, Ernest]

class Debut(object):
    pass

class Fin(object):
    pass

# les sujets
class Sujet(object):
    def __init__(self, valeur, signe_attaque=""):
        self.valeur = valeur
        self.signe_attaque = signe_attaque


papa = Sujet("ton père")
maman = Sujet("ta mère")
figure = Sujet("ta tête")  
coupe = Sujet("ta coiffure", chauve)
quartier = Sujet("ton quartier")
gros = Sujet("ton ventre", obese)
pays = Sujet("ton pays")
tonton = Sujet("ton oncle")
tata = Sujet("ta tante")
nez = Sujet("ton nez") 


sujets = [papa, maman, quartier, figure, coupe, gros, pays, tonton, tata, nez]

# les verbes
class Verbe(object):
    def __init__(self, valeur, signe_attaque=""):
        self.valeur = valeur
        self.signe_attaque = signe_attaque       

moche = Verbe('est/sont moche(s)' )
gros = Verbe('est/sont gros(e)', obese)
blondinette = Verbe('est/sont bête(s)', blonde)
ancien = Verbe('est/sont vieux', vieux)
agir = Verbe('agit/ssent' )
miraud = Verbe('est/sont miraud(s)', lunettes)
danser = Verbe('danse/ent')
similaire = Verbe('ressemble/ent ')
rigoler = Verbe('rigole/ent' )

verbes = [moche, gros, blondinette, ancien, agir, miraud, danser, similaire, rigoler]

# les liaisons
class Liaison(object):
    def __init__(self, valeur):
        self.valeur = valeur

et = Liaison('et')
donc = Liaison('donc')
mais  = Liaison('mais')
ou_alors = Liaison('ou alors')

liaisons = [et, donc, mais, ou_alors]


# les complements
class Complement(object):
    def __init__(self, valeur, signe_attaque=""): 
        self.valeur = valeur
        self.signe_attaque = signe_attaque

mariage = Complement('au mariage de')
lit = Complement('dans son lit')
superU = Complement('à superU')
journee = Complement('toute la journee')
nuit = Complement('toute la nuit')
pied = Complement('comme tes pieds')
clio2 = Complement('comme un embrayage de clio2')
theon = Complement('comme theon dans game of thrones')
ane = Complement('comme un ane', blonde)
elephant = Complement('comme un éléphant', obese)
choux_fleur = Complement('comme un choux-fleur')
la = Complement('à los Angeles')
reine = Complement('comme la reine d\'angleterre', vieux)
jallet = Complement('comme christophe jallet', chauve)
taupe = Complement('comme une taupe', lunettes)

complements = [mariage, lit, superU, journee, nuit, pied, elephant,choux_fleur, clio2, theon, reine, ane]


class Expression_finale(object):
    def __init__(self, valeur):
        self.valeur = valeur
pourToi = Expression_finale('voila pour toi!')
na = Expression_finale('na!')
dans_ta_face = Expression_finale('dans ta face!')
voila = Expression_finale('et voila!')
pub = Expression_finale('et n\'a pas encore fini sa puberté !')
got = Expression_finale('et n\'a toujours pas vu game of thrones')
hetic = Expression_finale('et en plus de cela tu n\'es meme pas inscrit à l\'ecole hetic')

expressions_finales = [pourToi, na, dans_ta_face, voila, got, hetic]


def get_text():

    nb_sujets = 6
    nb_verbes = 5
    nb_liaisons = 3
    nb_complements = 5
    nb_ef = 2
    shuffle(sujets)
    shuffle(verbes)
    shuffle(liaisons)
    shuffle(complements)
    shuffle(expressions_finales)
    res = sujets[:nb_sujets] + verbes[:nb_verbes] + liaisons[:nb_liaisons] + complements[:nb_complements] + expressions_finales[:nb_ef]
    shuffle(res)
    return res
# on ne prend pas toutes les expressions , on les melanges et on prend le nombre que l'on a indiqué.
## retourne moi les indices de la liste sujets a nombres nb sujets




