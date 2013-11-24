# -*- coding: UTF-8 -*-
from fonctions_diverses import decoupage, Memo

#---------------------------------------------------------------------------------
#---------------------Approche programmation dynamique top-down-------------------
#---------------------------------------------------------------------------------
  

#--------------Fonctions utilisés par la fonction equilibre-------------
#-----------------------------------------------------------------------

from fonctions_diverses import longueur, blancLigne, min

#-----------------------Fonctions d'équilibrage-------------------------
#-----------------------------------------------------------------------

#Entrée : texte une liste de strings qui sont les mots du textes à équilibrer
#         n le nombre de caractères d'une ligne
#Sortie : un doublet (R1,R2) où :
#           - R1 est une liste de listes de strings, chacune représentant les mots d'une ligne
#           - R2 est la somme de blancLigne pour chaque ligne

def equilibre(texte,n):
    for i in range (len(texte)-1,-1,-1):    #Pour i allant de l'indice du dernier mot au premier
        if longueur(texte[i:])<n:
            res=([texte[i:]],0)        
        else:
            curr=0
            deseq='infini'
            while longueur(texte[i:i+curr+1])<n:
                suite=MEMO.get(i+curr+1)
                deseq_bis=blancLigne(texte[i:i+curr+1],n)+suite[1]
                if min(deseq,deseq_bis)==deseq_bis:
                    deseq=deseq_bis
                    res=([texte[i:i+curr+1]]+suite[0],deseq)
                curr+=1
        MEMO.add(i,res[0],res[1])
    return res


#------------------------------------------Main--------------------------------------
#------------------------------------------------------------------------------------


#On récupère le texte à découper dans un fichier, et on écrit le texte découpé dans un autre

def main():

    global MEMO
    MEMO=Memo()
    f=equilibre
    decoupage(f)


   
if __name__ == "__main__":
    #création du mémo
    MEMO=None
    main()
