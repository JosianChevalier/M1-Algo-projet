# -*- coding: UTF-8 -*-
import sys
import argparse
import time

#---------------------------------------------------------------------------------
#--------------------Fonctions diverses communes aux algorithmes------------------
#---------------------------------------------------------------------------------


#--------------------Fonction longueur--------------------
#Entrée : une liste de strings t
#Sortie : (La somme de la longueur de chaque string de t) + (le nombre de string dans t)-1
#        (i.e. la longueur du texte formé par la succession de ces strings)


def longueur(t):
    if (t==[]):
        res=0
    else:
        res = len(t[0])
        for i in range (1,len(t)):
            res+=len(t[i])+1
    return res


#--------------------Fonction blancLigne--------------------
#Entrée : une liste de strings t, un entier n, tels que longueur(t)<=n
#Sortie : le cube de n - longueur(t)
#(i.e. le cube du nombre de caractères vides laissés sur une ligne de taille n par les mots de t


def blancLigne(t,n):
    return (n-longueur(t))**3

#--------------------Fonction largs_corrects--------------------
#---------------------------------------------------------------

#vérifie que les arguments entrés sur la ligne de commande sont corrects et renvoie un tuple (a,src,dest,length)
#où a est True si ils sont corrects, False sinon, src est le texte source, dest le fichier de destination,
#et length est la longueur d'une ligne

def args_corrects():

    parser = argparse.ArgumentParser()
    parser.add_argument('source', metavar='source.txt', type=str, nargs='+',help='Source file which contains the text to cut in lines')
    parser.add_argument('destination', metavar='destination.txt', type=str, nargs='+',help='Destination file to write the result')
    parser.add_argument('--lengthline', dest='length_line', action='store', default='60',help='Choose the length of the line (default 60 chars)')

    args = parser.parse_args()

    #Les fichiers sourceet destination doivent être indiqués comme arguments
    #on lit le texte du fichier source et on l'enregistre dans un string
    try:
        source=open(args.source[0],'r')
        try :
             texte_source=source.readline()
        finally :
            source.close()
        length=int(args.length_line)
        return (True,texte_source,args.destination[0],length)
    except (OSError, IOError):        
        print "\nFICHIER SOURCE NON VALIDE."
        print 'Usage : decoupage_top-down.py source-file.txt destination-fil.txt'
        return False,"","",0
    print "\nErreur inconnue."
    return False,"","",0


#-----------------------Fonction enregistre---------------------
#---------------------------------------------------------------

#Enregistre le texte entré en paramètre dans le fichier "destination" nomme en 2nd argument

def enregistre(texte_final, file_dest):
    try:
            dest=open(file_dest,'w+')
            dest.write(texte_final)
    finally:
        dest.close()
                
#-----------------------Fonction formate------------------------
#---------------------------------------------------------------

#Transforme un texte en liste de mots pour etre utilisé par les algorithmes de découpage

def formate(texte):
    texte_formate=texte.split(" ")
    return texte_formate


#--------------------Fonction list_to_text----------------------
#---------------------------------------------------------------


#transforme une liste de liste de mots en texte où chaque sous-liste est une ligne
def list_to_text(a):
    texte_final=""
    for e in a:
        texte_final+=e[0]
        for i in e[1:]:
            texte_final+=' '+i
        texte_final+='\n'
    return texte_final


#-------------------------Fonction decoupage----------------------
#-----------------------------------------------------------------

#Fonction principale : prend en paramètre la fonction que l'on souhaite utiliser et
#effectue les appels requis pour vérifier les arguments, effectuer les affichages d'erreur,
#de temps, et enregistre le résultat dans un fichier

def decoupage(fonction):
    
    
    correct,texte_source,fichier_dest,ligne=args_corrects()

    if correct :
        
        texte_formate=formate(texte_source)
        
        start=time.time()
        
        res=fonction(texte_formate,ligne)

        end=time.time()
        
        print "Le decoupage a prit %f secondes" % (end-start)
	print "Le déséquilibre est de ", res[1]
        
        texte_final=list_to_text(res[0])
        enregistre(texte_final,fichier_dest)
