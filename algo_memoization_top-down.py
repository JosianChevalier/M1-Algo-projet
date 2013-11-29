# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import decoupage

#---------------------------------------------------------------------------------
#---------------------Approche programmation dynamique top-down-------------------
#---------------------------------------------------------------------------------
  

#--------------Fonctions utilisés par la fonction equilibre-------------
#-----------------------------------------------------------------------

from fonctions_diverses import longueur, blancLigne, min, Memo, variance

#-----------------------Fonctions choix-------------------------
#-----------------------------------------------------------------------

#Choisit la fonction à appeler en fonction de la medure d'équilibre


def choix(texte, n, m):

    if m == 'b':
        return equilibre(texte,n)
    elif m == 'e':
        return equilibreEtendue(texte,n)
    elif m == 'v':
        return equilibreVar(texte,n)

#-----------------------Fonctions d'équilibrage-------------------------
#-----------------------------------------------------------------------

#Entrée : texte une liste de strings qui sont les mots du textes à équilibrer
# n le nombre de caractères d'une ligne
# ind l'indice du mot de départ de la portion de texte dans le texte original
#Sortie : un doublet (R1,R2) où :
# - R1 est une liste de listes de strings, chacune représentant les mots d'une ligne
# - R2 est la somme de blancLigne pour chaque ligne

def equilibre_reccur(texte, n, ind):
    res=([],0)
    if longueur(texte)<=n: #si la longueur du texte est inférieur à la longueur de la ligne
        res=([texte],0) #alors pas besoin de le découper, et on ignore le déséquilibre
        MEMO.add(ind,res[0],res[1])
    else :
        curr=0
        s='infini'
        while longueur(texte[0:curr+1])<=n:
            reccur=MEMO.get(ind+curr+1)
            if reccur==-1:
                reccur=equilibre_reccur(texte[curr+1:],n,ind+curr+1)
                MEMO.add(ind+1,reccur[0],reccur[1])
            s1=blancLigne(texte[0:curr+1],n)+reccur[1]
            if min(s1,s)==s1:
                s=s1
                res=([texte[0:curr+1]]+reccur[0],s)
            curr+=1
    return res

def equilibre(texte, n):
    global MEMO
    MEMO=Memo()
    return equilibre_reccur(texte, n, 0)

#-------------------------Déclinaison étendue---------------------------
#-----------------------------------------------------------------------

def equilibre_reccurEtendue(texte, n, ind):
    res=([],0)
    if longueur(texte)<=n: #si la longueur du texte est inférieur à la longueur de la ligne
        res=([texte],0,'infini',0) #alors pas besoin de le découper, et on ignore le déséquilibre
        MEMO.add_etendue(ind,res[0],res[1],res[2],res[3])
    else :
        curr=0
        s='infini'
        longtext=longueur(texte[0:1])
        while longtext<=n:
            reccur=MEMO.get_etendue(ind+curr+1)
            if reccur==-1:
                reccur=equilibre_reccurEtendue(texte[curr+1:],n,ind+curr+1)
                MEMO.add_etendue(ind+1,reccur[0],reccur[1],reccur[2],reccur[3])
            c=reccur[2]
            l=reccur[3]
            if min(longtext,c)==longtext:
                c=longtext
            if min(longtext,l)==l:
                l=longtext                
            s1=l-c
            if min(s1,s)==s1:
                s=s1
                res=([texte[0:curr+1]]+reccur[0],s,c,l)
            curr+=1
            longtext=longueur(texte[0:curr+1])
    return res

def equilibreEtendue(texte, n):
    global MEMO
    MEMO=Memo()
    return equilibre_reccurEtendue(texte, n, 0)


#-------------------------Déclinaison variance---------------------------
#-----------------------------------------------------------------------

def equilibre_reccurVar(texte, n, ind):
    res=([],0)
    if longueur(texte)<=n: #si la longueur du texte est inférieur à la longueur de la ligne
        res=([texte],0) #alors pas besoin de le découper, et on ignore le déséquilibre
        MEMO.add(ind,res[0],res[1])
    else :
        curr=0
        s='infini'
        while longueur(texte[0:curr+1])<=n:
            reccur=MEMO.get(ind+curr+1)
            if reccur==-1:
                reccur=equilibre_reccurVar(texte[curr+1:],n,ind+curr+1)
                MEMO.add(ind+1,reccur[0],reccur[1])
            s1=variance([texte[0:curr+1]]+reccur[0])
            if min(s1,s)==s1:
                s=s1
                res=([texte[0:curr+1]]+reccur[0],s)
            curr+=1
    return res

def equilibreVar(texte, n):
    global MEMO
    MEMO=Memo()
    return equilibre_reccurVar(texte, n, 0)

#------------------------------------------Main--------------------------------------
#------------------------------------------------------------------------------------


#On récupère le texte à découper dans un fichier, et on écrit le texte découpé dans un autre

def main():

    f=choix
    decoupage(f)


   
if __name__ == "__main__":
    #création du mémo
    MEMO=None
    main()
