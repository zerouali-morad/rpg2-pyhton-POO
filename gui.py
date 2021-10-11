import os
from random import shuffle

from tkinter import *
from tkinter import messagebox

from gui_choix_joueurs import GuiChoixJoueurs
from dataObject import get_text, joueurs
from helper import set_score, verif_grammaire


class gui:

    def __init__(self):
        self.window = Tk()
        self.window.title('Python project, Amine Amira Leila Morad group , battle of insults  " french version of : oh sir the insult simulator"')
        cur_width = 1000
        cur_height = 600
        self.window.geometry(str(cur_width) + 'x' + str(cur_height))
        tk_width = cur_width / 10
        tk_height = cur_height / 20

        self.btn_cdj = Button(self.window, text="Choisir les joueurs", command=lambda inst=self: inst.choix_des_joueurs())
        self.btn_cdj.grid(column=1, row=5, pady=5)
        self.btn_start = Button(self.window, text="Nouvelle partie", command=lambda inst=self: inst.nouveau_jeu())
        self.btn_start.grid(column=1, row=10, pady=5)
        self.btn_fin = Button(self.window, text="J'arrête !", command=lambda inst=self: inst.fin_de_jeu())
        self.btn_fin.grid(column=1, row=15, pady=5)

        self.lbl_nom_joueur1 = Label(self.window)
        self.lbl_nom_joueur1.config(bg="blue", fg="yellow")
        self.lbl_nom_joueur1.grid(column=1, row=20)
        self.lbl_nom_joueur2 = Label(self.window)
        self.lbl_nom_joueur2.grid(column=1, row=30)
        self.lbl_insult1 = Label(self.window)
        self.lbl_insult1.grid(column=1, row=25)
        self.lbl_insult2 = Label(self.window)
        self.lbl_insult2.grid(column=1, row=35)
        self.lbl_resultat = Label(self.window)
        self.lbl_resultat.grid(column=1, row=45, pady=4)
        self.list_mots = Listbox(self.window, width=int(tk_width),
                height=int(tk_height * 0.75), font=("Courier", 10, "bold"))
        self.list_mots.grid(column=1, row=40, padx=40)
        self.lbl_score1 = Label(self.window)
        self.lbl_score1.grid(column=2, row=20, padx=40)
        self.lbl_score2 = Label(self.window)
        self.lbl_score2.grid(column=2, row=30, padx=40)
        # a passer au verif_grammaire()
        self.list_mots.bind('<<ListboxSelect>>', self.list_click)
        self.current_player = 1
        self.insult1 = []
        self.insult2 = []
        self.joueurs = []
        self.btn_cdj.focus()
        self.window.update()
 

    def list_click(self, event):
        print(self.joueurs)
        try:
            selected_word = self.list_mots.get(event.widget.curselection())
        except:
            # on n'est pas dans la listBox
            return
        # TODO: eviter la redondance de code (utiliser une liste d' "insults")
        if self.current_player == 1:
            instance_mot = self.get_instance(selected_word)
            self.insult1.append(instance_mot) 
            res = verif_grammaire(self.insult1)
            if not res:
                print(f"{self.joueurs[0].name} : révise ta grammaire!")
            strinsult1 = []
            for instance in self.insult1:
                texte = instance.valeur
                strinsult1.append(texte)            
            self.lbl_insult1['text'] = " ".join(strinsult1)   
            self.current_player = 2
        else:
            instance_mot = self.get_instance(selected_word)
            self.insult2.append(instance_mot) 
            res = verif_grammaire(self.insult2)
            if not res:
                print(f"{self.joueurs[1].name} : révise ta grammaire!")
            strinsult2 = []
            for instance in self.insult2:
                texte = instance.valeur
                strinsult2.append(texte)            
            self.lbl_insult2['text'] = " ".join(strinsult2)   
            self.current_player = 1

        for i in range(self.list_mots.size()):
            if self.list_mots.get(i) == selected_word:
                self.list_mots.delete(i)
                break
        self.window.update()


    def get_instance(self, w):
        for element in self.internal_mots:
            if element.valeur == w:
                return element
        

    def nouveau_jeu(self):   
        if len(self.joueurs) == 2 :
            self.insult1 = []
            self.insult2 = []
            self.lbl_insult1['text'] = ""
            self.lbl_insult2['text'] = ""
            self.internal_mots = get_text()
            for text in self.internal_mots:
                self.list_mots.insert(0, text.valeur)
        else:  
           messagebox.showinfo(title="Joueurs manquant", message="il faut impérativement choisir deux joueurs")

    def choix_des_joueurs(self):
        cdj = GuiChoixJoueurs(self)
        self.window.update()
        

    def fin_de_jeu(self):
        # TODO: afficher le resultat dans la GUI, plutot que par print()
        resultatDuCombat = ""
        set_score(self.joueurs[0], self.insult1, self.joueurs[1], self.insult2)
        
        if self.joueurs[0].health > self.joueurs[1].health :
            resultatDuCombat = f"{self.joueurs[0].name}" + " a gagné" #f"{self.joueurs[0].name} a gagné!")
        elif self.joueurs[0].health < self.joueurs[1].health:
             resultatDuCombat= f"{self.joueurs[1].name}" + " a gagné"    #f"{self.joueurs[1].name} a gagné!")
        else:
            resultatDuCombat = "Egalité!" 
        
        self.lbl_resultat['text'] = resultatDuCombat
        self.lbl_score1['text'] = self.joueurs[0].health
        self.lbl_score2['text'] = self.joueurs[1].health

    def mainloop(self):
        self.window.mainloop()
