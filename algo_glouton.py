# -*- coding: UTF-8 -*-
import sys
sys.setrecursionlimit(50000) #Augmentation du nb max de mots à traiter
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage, measureOfTextEquilibrium, possibleString, longueur, blancLigne

def choix(texte, n, m):
    
    if m == 'b':
        return equilibreBl(texte,n)
    elif m == 'e':
        return equilibreEtendue(texte,n)

#---------------------------------------------------------------------------------
#------------------------------Approche gloutonne---------------------------------
#---------------------------------------------------------------------------------

###########################################################################################################
############################### Algo avec blancLigne comme parametre ######################################
###########################################################################################################




def equilibreGloutonBl(words, textEquilibre, n):
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
        

def equilibreBl(texte, n):
    textEq = [[texte[0][:]]]
    texte.pop(0)
    result = equilibreGloutonBl(texte, textEq, n)
    #print result
    return result, measureOfTextEquilibrium(result, n)

###########################################################################################################
############################### Algo avec etendu comme parametre ##########################################
###########################################################################################################

def equilibreGloutonEtendu(words, textEquilibre, n):
    if(words == []):
        return textEquilibre
    else:
        if(textEquilibre == []):
            textEquilibre = [[words[0][:]]]
            words.pop(0)
            return equilibreGlouton(words, textEquilibre, n)
        
        textWithTransfer = textEquilibre[:]
        textWithTransfer.append([words[0][:]])
        print "WT", textWithTransfer
        
        if(possibleString(textEquilibre[-1] + [words[0]], n)):
            lastString = textEquilibre[-1][:] + [words[0][:]]
            textWoTransfer = textEquilibre[:]
            textWoTransfer.pop(-1)
            textWoTransfer.append(lastString)
            words.pop(0)
            print "WoT", textWoTransfer
            
            maxMinWoT = longShortDistance(textWoTransfer)
            distanceWoT = maxMinWoT[0]-maxMinWoT[1]
            maxMinWT = longShortDistance(textWithTransfer)
            distanceWT = maxMinWT[0]-maxMinWT[1]
            if(distanceWoT < distanceWT):
                return equilibreGlouton(words, textWoTransfer, n)
            else:
                return equilibreGlouton(words, textWithTransfer, n)
        else:
            words.pop(0)
            return equilibreGlouton(words, textWithTransfer, n)

def equilibreEtendu(texte, n):
    textEq = [[texte[0][:]]]
    texte.pop(0)
    result = equilibreGloutonEtendu(texte, textEq, n)
    #print result
    return result, measureOfTextEquilibrium(result, n)


#------------------------------------------Main--------------------------------------
#------------------------------------------------------------------------------------


#On récupère le texte à découper dans un fichier, et on écrit le texte découpé dans un autre

def main():
    f=choix
    decoupage(f)


   
if __name__ == "__main__":
    #création du mémo
    main()
