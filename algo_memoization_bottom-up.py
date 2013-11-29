# -*- coding: UTF-8 -*-
from fonctions_diverses import decoupage, Memo

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
#         n le nombre de caractères d'une ligne
#Sortie : un doublet (R1,R2) où :
#           - R1 est une liste de listes de strings, chacune représentant les mots d'une ligne
#           - R2 est la somme de blancLigne pour chaque ligne

def equilibre(texte,n):
    global MEMO
    MEMO=Memo()
    for i in range (len(texte)-1,-1,-1):    #Pour i allant de l'indice du dernier mot au premier
        if longueur(texte[i:])<=n:
            res=([texte[i:]],0)        
        else:
            curr=0
            deseq='infini'
            while longueur(texte[i:i+curr+1])<=n:
                suite=MEMO.get(i+curr+1)
                deseq_bis=blancLigne(texte[i:i+curr+1],n)+suite[1]
                if min(deseq,deseq_bis)==deseq_bis: #on notera que la fonction min a été surchargée pour
                                                    #considérer 'infini' comme l'infini
                    deseq=deseq_bis
                    res=([texte[i:i+curr+1]]+suite[0],deseq)
                curr+=1
        MEMO.add(i,res[0],res[1])
    return res

#-------------------------Déclinaison étendue---------------------------
#-----------------------------------------------------------------------


def equilibreEtendue(texte, n):  
    global MEMO
    MEMO=Memo()
    for i in range (len(texte)-1,-1,-1):    #Pour i allant de l'indice du dernier mot au premier
        if longueur(texte[i:])<=n:
            res=([texte[i:]],0,'infini',0)
        else:
            curr=0
            deseq='infini'
            longtext=longueur(texte[i:i+1])
            while longtext<=n:
                suite=MEMO.get_etendue(i+curr+1)
                c=suite[2]
                l=suite[3]
                if min(longtext,c)==longtext:
                    c=longtext
                if min(longtext,l)==l:
                    l=longtext                
                deseq_bis=l-c
                if min(deseq,deseq_bis)==deseq_bis: #on notera que la fonction min a été surchargée pour
                                                    #considérer 'infini' comme l'infini
                    deseq=deseq_bis
                    res=([texte[i:i+curr+1]]+suite[0],deseq,c,l)
                curr+=1
                longtext=longueur(texte[i:i+curr+1])
        MEMO.add_etendue(i,res[0],res[1],res[2],res[3])
    return res


#-------------------------Déclinaison variance---------------------------
#-----------------------------------------------------------------------
#Pour la variance on remplace simplement l'entrée 

def equilibreVar(texte, n):
    global MEMO
    MEMO=Memo()
    for i in range (len(texte)-1,-1,-1):    #Pour i allant de l'indice du dernier mot au premier
        if longueur(texte[i:])<=n:
            res=([texte[i:]],0)        
        else:
            curr=0
            deseq='infini'
            while longueur(texte[i:i+curr+1])<=n:
                suite=MEMO.get(i+curr+1)
                deseq_bis=variance([texte[i:i+curr+1]]+suite[0])
                if min(deseq,deseq_bis)==deseq_bis: #on notera que la fonction min a été surchargée pour
                                                    #considérer 'infini' comme l'infini
                    deseq=deseq_bis
                    res=([texte[i:i+curr+1]]+suite[0],deseq)
                curr+=1
        MEMO.add(i,res[0],res[1])
    return res

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
