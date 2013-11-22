# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage

#---------------------------------------------------------------------------------
#---------------------Approche programmation dynamique top-down-------------------
#---------------------------------------------------------------------------------


#-------------------------------Memoization----------------------------
#----------------------------------------------------------------------

#entrée du memo,composée de la portion de texte équilibré et du poid de l'équilibrage, associé dans le
#dictionnaire à l'indice du mot ou commence la portion de texte

class Data_entry:
    def __init__(self,r,s):
        self.result=r
        self.sum=s

#mémo où sont stocké les équilibrages déjà calculés

class Memo:
    def __init__(self):
        self.data=dict()

    def add(self,ind,fin_texte,somme):
        d=Data_entry(fin_texte,somme)
        self.data[ind]=d

    def get(self,i):
        try:
            res=self.data[i]
        except KeyError:
            return -1
        return res.result, res.sum
          
    


#--------------Fonctions utilisés par la fonction equilibre-------------
#-----------------------------------------------------------------------

from fonctions_diverses import longueur, blancLigne

#--------------------Fonction min--------------------
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


#-----------------------Fonctions d'équilibrage-------------------------
#-----------------------------------------------------------------------

#Entrée : texte une liste de strings qui sont les mots du textes à équilibrer
#         n le nombre de caractères d'une ligne
#         ind l'indice du mot de départ de la portion de texte dans le texte original
#Sortie : un doublet (R1,R2) où :
#           - R1 est une liste de listes de strings, chacune représentant les mots d'une ligne
#           - R2 est la somme de blancLigne pour chaque ligne

def equilibre_reccur(texte, n, ind):
    res=([],0)
    if longueur(texte)<=n: #si la longueur du texte est inférieur à la longueur de la ligne
        res=([texte],0)    #alors pas besoin de le découper, et on ignore le déséquilibre
        MEMO.add(ind,res[0],res[1])
    else :
        curr=0
        s='infini'
        while longueur(texte[0:curr+1])<=n:
            reccur=MEMO.get(ind+curr+1)
            if reccur==-1:
                reccur=equilibre(texte[curr+1:],n,ind+curr+1)            
                MEMO.add(ind,reccur[0],reccur[1])
            s1=blancLigne(texte[0:curr+1],n)+reccur[1]
            if min(s1,s)==s1:
                s=s1
                res=([texte[0:curr+1]]+reccur[0],s)
            curr+=1
    return res

def equilibre(texte, n):
    return equilibre_reccur(texte, n, 0)

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
