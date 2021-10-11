import os

from tkinter import *

from dataObject import joueurs


class GuiChoixJoueurs:

    def __init__(self, caller):
        self.window = Toplevel()
        self.window.title('Choix des joueurs')
        cur_width = 800
        cur_height = 400
        self.window.geometry(str(cur_width) + 'x' + str(cur_height))
        tk_width = cur_width / 10
        tk_height = cur_height / 20
        self.caller = caller

        # TODO: ajouter 2 labels pour les noms des joueurs + ajouter un bouton "reset"
        self.list_joueurs = Listbox(self.window, width=int(tk_width),
                height=int(tk_height * 0.75), font=("Courier", 10, "bold"))
        self.list_joueurs.grid(column=1, row=30, padx=40)
        self.list_joueurs.bind('<<ListboxSelect>>', self.list_click)
        self.caller.joueurs = []
        for joueur in joueurs:
            self.list_joueurs.insert(0, joueur.name)

        self.btn_valider = Button(self.window, text="Valider", command=lambda inst=self: inst.valider())
        self.btn_valider.grid(column=1, row=35, pady=5)


    def list_click(self, event):
        try:
            selected_player = self.list_joueurs.get(event.widget.curselection())
        except:
            # on n'est pas dans la listBox
            return
        instance_joueur = self.get_instance(selected_player)
        self.caller.joueurs.append(instance_joueur)
        print(self.caller.joueurs)
        self.window.update()


    def get_instance(self, w):
        for j in joueurs:
            if j.name == w:
                return j


    def valider(self):
        if len(self.caller.joueurs) > 1:
            self.caller.lbl_nom_joueur1["text"] = self.caller.joueurs[0].name
            self.caller.lbl_nom_joueur2["text"] = self.caller.joueurs[1].name
            self.caller.joueurs[0].health = 0
            self.caller.joueurs[1].health = 0
            self.caller.lbl_score1["text"] = self.caller.joueurs[0].health 
            self.caller.lbl_score2["text"] = self.caller.joueurs[1].health 
            self.caller.lbl_insult1["text"] = ""
            self.caller.lbl_insult2["text"] = ""
            self.caller.insult1 = []
            self.caller.insult2 = [] 
            self.caller.window.update()
            self.window.destroy()
