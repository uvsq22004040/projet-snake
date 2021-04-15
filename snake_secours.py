##################################
# groupe 3 MIASHS TD2
# Sana MAREF
# Sana MAAREF
# Judith FAUCON
# Jalis LACHEHAB
# Rosary NITHIYANANTHAM 
# Anya BOUBCHIR
# Nolwenn GAUTIER
# https://github.com/uvsq22004040/projet-snake.git
######################################################### 


############################
# IMPORTATION DES LIBRAIRIES

import tkinter as tk
import random as rd

########################
# CONSTANTES

LARGEUR = 600
HAUTEUR = 420
CARRE = LARGEUR // 20
COULEUR_PIERRE1 = "LightGoldenrod3"
COULEUR_PIERRE2 = "LightGoldenrod4"

########################
# FONCTIONS

def mur():
    """Crée un mur autour du canvas"""
    for i in range(CARRE):
        canvas.create_rectangle(i*CARRE,0,(i+1)*CARRE,CARRE,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)
    for i in range(CARRE):
        canvas.create_rectangle(0,i*CARRE,CARRE,(i+1)*CARRE,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)
    for i in range(CARRE):
        canvas.create_rectangle(i*CARRE,HAUTEUR-CARRE,(i+1)*CARRE,HAUTEUR,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)
    for i in range(CARRE):
        canvas.create_rectangle(LARGEUR-CARRE,i*CARRE,LARGEUR,(i+1)*CARRE,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)


def pomme():
    """Place une pomme aléatoirement dans l'herbe"""
    x = rd.randint(CARRE,LARGEUR-CARRE*2)
    y = rd.randint(CARRE,HAUTEUR-CARRE*2)
    canvas.create_oval(x,y,x+CARRE,y+CARRE, fill="red")


########################
# PROGRAMME PRINCIPAL

racine = tk.Tk()
racine.title("Snake")

# création des widgets

canvas = tk.Canvas(racine, bg="chartreuse3", width=LARGEUR, height=HAUTEUR)


# placement des widgets

canvas.grid()

# liaison des événements

mur()
pomme()

# boucle principale

racine.mainloop()