# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage, measureOfTextEquilibrium, possibleString, longueur, blancLigne

#---------------------------------------------------------------------------------
#------------------------------Approche gloutonne---------------------------------
#---------------------------------------------------------------------------------


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
    #print result
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
