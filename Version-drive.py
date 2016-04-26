# Charley GUITTON
# Tristan Legacque
# Paul Ferrand 
# Galérie d'Art

from tkinter import *

win = Tk("Polygones")
win.title('Polygones')

#Fonctions : 

#Initialisations des variables
W = 2 
sommet = []

#liste de couleurs pour les diagonales
color = ['GREEN', 'BLUE', 'RED', 'PURPLE', 'PINK', 'YELLOW', 'BROWN', 'MAGENTA']
nb_clik=0



def triangularisation(points):              #dessine des diagonales
    global sens
    n = len(points)
    determination_du_sens()
    for k in range(n):                          #a et c sont les points voisins, b est le point du centre
        a = points[(k-1)%n]
        b = points[(k)%n]
        c = points[(k+1)%n]

        if (sens=='trigo'):
            if(det(a,b,c) < 0):                     #Verifie si c'est une oreille ou non
                print("Le point "+str(k)+" "+str(b)+" est une oreille !")
                cnv.create_line(a,c, fill=color[k%len(color)], width=W)
                
        if sens=='horaire':
            if(det(a,b,c) > 0):
                print("Le point "+str(k)+" "+str(b)+" est une oreille !")
                cnv.create_line(a,c, fill=color[k%len(color)], width=W)

    print (sommet)
    
def vect(a,b):                                  #Crée deux vecteurs à partir de 3 points
    return (b[0]-a[0], b[1]-a[1])
        
def det(a,b,c):                                 #Calcul le determinant 
    ab = vect(a,b)
    ac = vect(a,c)
    return(ab[0]*ac[1]-ab[1]*ac[0])



def select (event):                             #Creer une liste avec les coordonnées de points 
     global coordx,coordy, nb_clik
     
     coordx,coordy = event.x, event.y
     cnv.create_rectangle(coordx-1,coordy-1,coordx+1,coordy+1,fill='black')
     sommet.append([coordx,coordy])

     if len(sommet)>1 :
          
          cnv.create_line(sommet[-2][0],sommet[-2][1],sommet[-1][0],sommet[-1][1], width=W)
     nb_clik=nb_clik+1
     print (coordx,coordy)
     print (sommet)
     print (nb_clik)

def fermer ():                                  #Bouton fermer
    cnv.create_line(sommet[0][0],sommet[0][1],sommet[-1][0],sommet[-1][1], width=W)
    cnv.unbind('<ButtonPress>')

def setDEFAULT():
    global sommet
    sommet = [[69, 157], [30, 75], [83, 100], [142, 50], [211, 106], [151, 113], [193, 175], [125, 225], [123, 160], [43, 210]]
    cnv.delete(ALL)
    n = len(sommet)
    for k in range(n):
        cnv.create_line(sommet[k%n], sommet[(k+1)%n])

def determination_du_sens():
    global sens , sommet
    if sommet[1][0]>sommet[0][0]:
        sens='horaire'
    else :
        sens='trigo'
    print(sens)
    
    
#Création d'une fenêtre gauche :
cnv = Canvas(win, width=300, height=300,bg='white')
cnv.pack(side = 'left', expand=True)

#Création d'une fenêtre droite (pour le menu) :
frm = Frame(win, width=50, height=300, bg = 'light blue', padx=10, pady=15)
frm.pack(side = 'right')

#Bouton "Quitter" :
espace1 = Label(frm, bg = 'light blue').pack(side = 'bottom')
Quitter = Button(frm, text = "Quitter", command=win.destroy)
Quitter.pack(side = 'bottom')
espace2 = Label(frm, bg = 'light blue').pack(side = 'bottom')

#Bouton "Fermer polygone": 
Fermer = Button(frm, text = "Fermer\n Polygone", command=fermer)
Fermer.pack(side = 'bottom')
espace3 = Label(frm, bg = 'light blue').pack(side = 'bottom')

#Bouton "Oreille" :
Oreille = Button(frm, text = "Oreille", command=lambda:triangularisation(sommet))
Oreille.pack(side = 'bottom')
espace4 = Label(frm, bg = 'light blue').pack(side = 'bottom')

cnv.bind('<ButtonPress>',select)
#setDEFAULT()

win.mainloop()

