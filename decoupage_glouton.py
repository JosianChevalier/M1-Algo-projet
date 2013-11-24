# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage

#---------------------------------------------------------------------------------
#------------------------------Approche gloutonne---------------------------------
#---------------------------------------------------------------------------------


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

def measureOfTextEquilibrium(text, stringLength):
		somme = 0;
		for i in range(0, len(text)-1):
			somme += blancLigne(text[i], stringLength)
		return somme

#Entree: words:liste des mots, stringLength:longeur d'une ligne
#Sortie: est-ce que c'est possible de mettre la sentence a partir des mots dans "words" en ligne de longeur "stringLength" 
def possibleString(words, stringLength):
		for x in range(0, len(words)):
			if stringLength >= len(words[x]):
				stringLength -= len(words[x])+1
			else: 
				return False
				
		return True



def equilibreGlouton(words, textEquilibre, n):
    if(words == []):
        return textEquilibre
    else:
        if(textEquilibre == []):
            textEquilibre = [[words[0][:]]]
            words.pop(0)
            
            return equilibreGlouton(words, textEquilibre, n)
        
        if(possibleString(textEquilibre[-1] + [words[0]], n)):
            lastString = textEquilibre[-1][:] + [words[0][:]]
            textEquilibre.pop(-1)
            textEquilibre.append(lastString)
            words.pop(0)
            
            return equilibreGlouton(words, textEquilibre, n)
        else:
            lastString = [words[0][:]]
            words.pop(0)
            textEquilibre = textEquilibre[:]
            textEquilibre.append(lastString)
            
            return equilibreGlouton(words, textEquilibre, n)
        

def equilibre(texte, n):
    textEq = [[texte[0][:]]]
    texte.pop(0)
    result = equilibreGlouton(texte, textEq, n)
    print result
    return result, measureOfTextEquilibrium(result, n)




#------------------------------------------Main--------------------------------------
#------------------------------------------------------------------------------------


#On récupère le texte à découper dans un fichier, et on écrit le texte découpé dans un autre

def main():
    f=equilibre
    decoupage(f)


   
if __name__ == "__main__":
    #création du mémo
    main()
