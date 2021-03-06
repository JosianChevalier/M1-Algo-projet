# -*- coding: UTF-8 -*-
import sys
import argparse
import time

#---------------------------------------------------------------------------------
#--------------------Fonctions diverses communes aux algorithmes------------------
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------
#----------------CALCUL DE LA DISPERSION STATISTIQUE------------------
#---------------------------------------------------------------------

#------------------------Fonction variance------------------------
#-----------------------------------------------------------------
#Entree: text: liste de listes des mots;
#Sortie: la valeur de la variance de la longueur effective des lignes du texte
#           (à l'exception de la dernière)        
def variance(text):
    sommeLongueurs = 0.0;
    for i in range(0, len(text)-1):
        sommeLongueurs += longueur(text[i])
    moyen = sommeLongueurs/(len(text)-1)

    sommeEcartesCarres = 0
    for i in range(0, len(text)-1):
        sommeEcartesCarres += (moyen - longueur(text[i]))**2

    return sommeEcartesCarres/(len(text)-1)

#-------------------Fonction etendue--------------------
#-----------------------------------------------------------------
#Entree: text: liste de listes des mots;
#Sortie: la difference entre la ligne la plus longue et la plus courte
def etendue(text):
    plusLongue = 0;
    plusCourte = sys.maxint
    for i in range(0, len(text)):
        lon = longueur(text[i])
        if(lon>plusLongue):
            plusLongue = lon
        if(lon<plusCourte):
            plusCourte = lon

    return plusLongue - plusCourte

def plusLong(text):
    plusLongue = 0;
    for i in range(0, len(text)):
        lon = longueur(text[i])
        if(lon>plusLongue):
            plusLongue = lon
    
    return plusLongue

def plusCourt(text):
    plusCourte = 0;
    for i in range(0, len(text)):
        lon = longueur(text[i])
        if(lon<plusCourte):
            plusCourte = lon
    
    return plusCourte


#---------------------MEMOIZATION-----------------------
#-------------------------------------------------------


#entrée du memo,composée de la portion de texte équilibré et du poid de l'équilibrage, associé dans le
#dictionnaire à l'indice du mot ou commence la portion de texte

class Data_entry:
    def __init__(self,r,s):
        self.result=r
        self.sum=s

#Declinaison pour l'etendue de la Data_entry : ajout de la longueur des lignes plus longues et plus courtes

class Data_entry_etendue:
    def __init__(self,r,e,c,l):
        self.result=r
        self.etend=e    
        self.long=l         
        self.courte=c
        
#mémo où sont stocké les équilibrages déjà calculés

class Memo:
    def __init__(self):
        self.data=dict()

    def add(self,ind,fin_texte,somme):
        d=Data_entry(fin_texte,somme)
        self.data[ind]=d

    def add_etendue(self,ind,fin_texte,etendue,courte,longue):  #version etendue de la fonction add
        d=Data_entry_etendue(fin_texte,etendue,courte,longue)
        self.data[ind]=d

    def get(self,i):
        try:
            res=self.data[i]
        except KeyError:
            return -1
        return res.result, res.sum

    def get_etendue(self,i): #version etendue de la fonction get
        try:
            res=self.data[i]
        except KeyError:
            return -1
        return res.result, res.etend, res.courte, res.long



          
#--------------------Fonction longueur--------------------
#---------------------------------------------------------
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
#-----------------------------------------------------------
#Entrée : une liste de strings t, un entier n, tels que longueur(t)<=n
#Sortie : le cube de n - longueur(t)
#(i.e. le cube du nombre de caractères vides laissés sur une ligne de taille n par les mots de t


def blancLigne(t,n):
    return (n-longueur(t))**3

#----------------------Fonction possibleString--------------------
#-----------------------------------------------------------------
#Entree: words:liste des mots, stringLength:longeur de la ligne
#Sortie: True si on peut mettre les mots de "words" dans une ligne de longueur "stringLength", False sinon
def possibleString(words, stringLength):
    return (stringLength >= longueur(words))


#--------------------Fonction min-------------------------
#---------------------------------------------------------
#Surcharge de la fonction min de python telle que 'infini' est considéré comme un int de valeur infinie

def min(s1,s2):
    if s1=='infini':
        return s2
    elif s2=='infini':
        return s1
    elif s1>s2:
        return s2
    else:
        return s1



#--------------------Fonction args_corrects--------------------
#---------------------------------------------------------------

#vérifie que les arguments entrés sur la ligne de commande sont corrects et renvoie un tuple (a,src,dest,length)
#où a est True si ils sont corrects, False sinon, src est le texte source, dest le fichier de destination,
#et length est la longueur d'une ligne

def args_corrects():

    parser = argparse.ArgumentParser()
    parser.add_argument('source', metavar='source.txt', type=str, nargs='+',help='Source file which contains the text to cut in lines')
    parser.add_argument('destination', metavar='destination.txt', type=str, nargs='+',help='Destination file to write the result')
    parser.add_argument('--lengthline', dest='length_line', action='store', default='60',help='Choose the length of the line (default 60 chars)')
    parser.add_argument('--mesure', dest='mesure', action='store', default='b',help='b to use blanks, e for scope, v for variance')

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
        if args.mesure not in ['v','b','e']:
            print "\nMESURE NON VALIDE."
            print 'Usage : decoupage_top-down.py source-file.txt destination-fil.txt'
            return False,"","",0,""
        return (True,texte_source,args.destination[0],length, args.mesure)
    except (OSError, IOError):
        print "\nFICHIER SOURCE NON VALIDE."
        print 'Usage : decoupage_top-down.py source-file.txt destination-fil.txt'
        return False,"","",0,""
    print "\nErreur inconnue."
    return False,"","",0,""


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
    
    
    correct,texte_source,fichier_dest,ligne,mesure=args_corrects()

    if correct :
        
        texte_formate=formate(texte_source)
        
        start=time.time()
        
        res=fonction(texte_formate,ligne,mesure)

        end=time.time()
       
        texte_final=list_to_text(res[0])
        enregistre(texte_final,fichier_dest)

        print
        print "Le decoupage a pris %f secondes" % (end-start)
        print "Le desequilibre est de ", res[1]

#----------------Fonction measureOfTextEquilibrium----------------
#-----------------------------------------------------------------
#Entree: text: liste de listes des mots; stringLength:longeur d'une ligne
#Sortie: somme des mesures d'inequilibre des lignes de texte
def measureOfTextEquilibrium(text, stringLength):
    somme = 0;
    for i in range(0, len(text)-1):
        somme += blancLigne(text[i], stringLength)
    return somme
