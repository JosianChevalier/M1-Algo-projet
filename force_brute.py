# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage, measureOfTextEquilibrium, possibleString

#---------------------------------------------------------------------------------
#------------------------------Approche force brute-------------------------------
#---------------------------------------------------------------------------------


#--------------Fonctions utilisés par la fonction equilibre-------------
#-----------------------------------------------------------------------

from fonctions_diverses import longueur, blancLigne

#-----------------------Fonctions d'équilibrage-------------------------
#-----------------------------------------------------------------------

def bruteForceWithTransition(words, text, measure, strl):
    if(words == []):
        return [],text,measure,strl
    else:
        text.append([words[0]])
        newText = text[:]
        newText2 = text[:]
        newMeasure = measure + blancLigne([words[0]], strl)
        newWords = words[:]
        if(type(newWords) is str):
            newWords = []
        else:
            newWords.pop(0)
        
        a = bruteForceWithTransition(newWords, newText, newMeasure, strl)
        b = bruteForceWoTransition(newWords, newText2, newMeasure, strl)
        
        if(a[2] < b[2]):
            return a
        else:
            return b

def bruteForceWoTransition(words, text, measure, strl):
    if(words == []):
        return [],text,measure,strl
    else:
        wordToJoin = words[0][:]
        lastString = text[-1][:]
        lastString.append(wordToJoin)
        if(possibleString(lastString , strl)):
            text.pop(-1)
            text.append(lastString)
            newText = text[:]
            newText2 = text[:]
            newMeasure = measureOfTextEquilibrium(newText, strl)
            newWords = words[:]
            if(type(newWords) is str):
                newWords = []
            else:
                newWords.pop(0)
            
            a = bruteForceWithTransition(newWords, newText, newMeasure, strl)
            b = bruteForceWoTransition(newWords, newText2, newMeasure, strl)
            
            if(a[2] < b[2]):
                return a
            else:
                return b
        else:
            return [],[],sys.maxint,strl

			
		
def equilibre(texte, n):
    firstWord = texte[0][:]
    texte.pop(0)
    a = bruteForceWithTransition(texte, [[firstWord]], blancLigne([firstWord], n), n)
    b = bruteForceWoTransition(texte, [[firstWord]], blancLigne([firstWord], n), n)
    if(a[2] < b[2]):
        print a[1]
        return a[1],a[2]
    else:
        print b[1]
        return b[1],b[2]
		

#------------------------------------------Main--------------------------------------
#------------------------------------------------------------------------------------


#On récupère le texte à découper dans un fichier, et on écrit le texte découpé dans un autre

def main():
    f=equilibre
    decoupage(f)


   
if __name__ == "__main__":
    #création du mémo
    main()
