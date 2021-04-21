##################################
# groupe 3 MIASHS TD2
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

L = 600
H = 420
CARRE = L // 20
LARGEUR = L-CARRE
HAUTEUR = H-CARRE
COULEUR_PIERRE1 = "LightGoldenrod3"
COULEUR_PIERRE2 = "LightGoldenrod4"
x = L // 2
y = H // 2
dx, dy = 10, 10
flag = 0
direction = 'haut'
pX = rd.randint(CARRE, LARGEUR)
pY = rd.randint(CARRE, HAUTEUR)
SERPENT = [[x,y],[x,y],[x,y],[x,y]]
 
########################
# FONCTIONS

def ajout_pomme():
    """Ajoute une pomme au hasard sur le terrain à chaque fois qu'elle est mangée et agrandit le serpent"""
    global pomme
    global x,y,pX,pY
    global SERPENT
    if SERPENT[1][0]>pX-40 and  SERPENT[1][0]<pX:        
        if SERPENT[1][1]>pY-40 and SERPENT[1][1]<pY:
            #On remet une pomme au hasard
            pX = rd.randint(CARRE, LARGEUR-20)
            pY = rd.randint(CARRE, HAUTEUR-20)
            #On ajoute un nouveau point au serpent
            SERPENT.append([0,0])
    
 

def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    deplacement_serpent()
    
 
def left(event):
    """Le serpent se dirige vers la gauche"""
    global direction
    direction = "gauche"
 
def right(event):
    """Le serpent se dirige vers la droite"""
    global direction
    direction = "droite"
 
def up(event):
    """Le serpent se dirige vers le haut"""
    global direction
    direction = "haut"
 
def down(event):
    """Le serpent se dirige vers le bas"""
    global direction
    direction = "bas"

def deplacement_serpent():
    """Fixe le décors et permet de faire bouger le serpent"""
    global x,y,pX,pY
    global SERPENT
    canvas.delete("all")
    i=len(SERPENT)-1
    j=0
    while i > 0:
        SERPENT[i][0]=SERPENT[i-1][0]
        SERPENT[i][1]=SERPENT[i-1][1]
        corps_serpent = canvas.create_oval(SERPENT[i][0], SERPENT[i][1], SERPENT[i][0]+15, SERPENT[i][1]+15,outline='black', fill='blue')
        i=i-1
    tete_serpent = canvas.create_oval(SERPENT[0][0], SERPENT[0][1], SERPENT[0][0]+15, SERPENT[0][1]+15,outline="black", fill="blue")
    pomme = canvas.create_oval(pX-20, pY-20, pX, pY, outline='black', fill='red')
    
    for i in range(CARRE):
        canvas.create_rectangle(i*CARRE,0,(i+1)*CARRE,CARRE,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)
    for i in range(CARRE):
        canvas.create_rectangle(0,i*CARRE,CARRE,(i+1)*CARRE,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)
    for i in range(CARRE):
        canvas.create_rectangle(i*CARRE,H-CARRE,(i+1)*CARRE,H,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)
    for i in range(CARRE):
        canvas.create_rectangle(L-CARRE,i*CARRE,L,(i+1)*CARRE,
         fill=COULEUR_PIERRE1, outline=COULEUR_PIERRE2, width=2)

    if direction  == "gauche":
        SERPENT[0][0]  = SERPENT[0][0] - dx
        if SERPENT[0][0] < CARRE:
            racine.destroy()
    elif direction  == "droite":
        SERPENT[0][0]  = SERPENT[0][0] + dx
        if SERPENT[0][0] > LARGEUR:
            racine.destroy()
    elif direction  == "haut":
        SERPENT[0][1]  = SERPENT[0][1] - dy
        if SERPENT[0][1] < CARRE:
            racine.destroy()
    elif direction  == "bas":
        SERPENT[0][1]  = SERPENT[0][1] + dy
        if SERPENT[0][1] > HAUTEUR:
            racine.destroy()
    
    ajout_pomme()
    
    if flag != 0:
        racine.after(90, deplacement_serpent)


 
########################
# PROGRAMME PRINCIPAL
 
racine = tk.Tk()
racine.title("Snake")
 
# création des widgets
 
canvas = tk.Canvas(racine, bg="chartreuse3", width=L, height=H)

serpent_avant_lancement = canvas.create_oval(SERPENT[0][0], SERPENT[0][1], SERPENT[0][0]+15, SERPENT[0][1]+15, outline="black", fill="blue")
pomme = canvas.create_oval(pX, pY, pX+20, pY+20, fill="red")

b1 = tk.Button(racine, text='Nouvelle Partie', command=newGame, bg="white" , fg="black")
b2 = tk.Button(racine, text="Quitter", command=racine.destroy, bg="white" , fg="black")


# placement des widgets
 
canvas.grid(column=0)
b1.grid(column=0,row=1)
b2.grid(column=0,row=2)

 
# liaison des événements

racine.bind('<KeyPress-Right>', right)
racine.bind('<KeyPress-Left>', left)
racine.bind('<KeyPress-Up>' , up)
racine.bind('<KeyPress-Down>', down)


# boucle principale
 
racine.mainloop()
