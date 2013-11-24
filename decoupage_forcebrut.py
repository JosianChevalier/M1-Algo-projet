# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage

#---------------------------------------------------------------------------------
#------------------------------Approche force brut--------------------------------
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
		for i in range(0, len(text)):
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

def bruteForceWithTransition(words, text, measure, strl):
    print "-----------------------------------"
    print "With transition"
    print "Words: ", words
    print "Text: ", text
    print "Measure: ",measure
    
    if(words == []):
        return [],text,measure,strl
    else:
        print "Added new string to the text ", text
        text.append([words[0]])
        newText = text[:]
        newText2 = text[:]
        print "So, now it's", newText
        newMeasure = measure + blancLigne([words[0]], strl)
        print "New measure: ",newMeasure
        newWords = words[:]
        if(type(newWords) is str):
            newWords = []
        else:
            newWords.pop(0)
        print "Words rest: ",newWords
        
        a = bruteForceWithTransition(newWords, newText, newMeasure, strl)
        b = bruteForceWoTransition(newWords, newText2, newMeasure, strl)
        
        if(a[2] < b[2]):
            return a
        else:
            return b

def bruteForceWoTransition(words, text, measure, strl):
    print "-----------------------------------"
    print "Without transition"
    print "Words: ", words
    print "Text: ", text
    print "Measure: ",measure
    
    if(words == []):
        return [],text,measure,strl
    else:
        wordToJoin = words[0][:]
        lastString = text[-1][:]
        print "Trying to add to string", lastString
        print "word ", wordToJoin
        lastString.append(wordToJoin)
        if(possibleString(lastString , strl)):
            print "It's possible, so last string is: ", lastString
            text.pop(-1)
            text.append(lastString)
            newText = text[:]
            newText2 = text[:]
            print "Text result: ", newText
            newMeasure = measureOfTextEquilibrium(newText, strl)
            print "Measure of this text ", newMeasure
            print "Words were:", words
            newWords = words[:]
            if(type(newWords) is str):
                newWords = []
            else:
                newWords.pop(0)
            
            print "Words rest:", newWords
            
            a = bruteForceWithTransition(newWords, newText, newMeasure, strl)
            b = bruteForceWoTransition(newWords, newText2, newMeasure, strl)
            
            if(a[2] < b[2]):
                return a
            else:
                return b
        else:
            print "But it's impossible"
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
