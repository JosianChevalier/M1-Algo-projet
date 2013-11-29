import sys
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage, blancLigne, measureOfTextEquilibrium, possibleString, longueur, etendue, plusLong, plusCourt

def choix(texte, n, m):

    if m == 'b':
        return equilibre(texte,n)
    elif m == 'e':
        return equilibreEtendue(texte,n)

#---------------------------------------------------------------------------------
#--------------Approche programmation dynamique bidimensionel---------------------
#---------------------------------------------------------------------------------

###########################################################################################################
############################### Algo avec blancLigne comme parametre ######################################
###########################################################################################################


#Entree: text1: liste de listes des mots; text2: liste de listes des mots; stringLength:longeur de la ligne
#Sortie: Si c'est possible de fusionner la derniere proposition de text1 et la premiere proposition de text2,
#on les fusionne et retourne une liste qui contient True, la mesure de texte resultant, le texte resultant
#Sinon on retourne une liste qui contient False, 0 , liste vide

def fusionTextes(text1, text2, textm1, textm2, stringLength): #O(1)
    fusionedString = text1[-1][:] + text2[0][:] #O(1)
    if(possibleString(fusionedString, stringLength)):
        t1 = text1[:] #O(1)
        t2 = text2[:] #O(1)
        fm = blancLigne(fusionedString ,stringLength)
        m1 = blancLigne(text1[-1], stringLength)
        m2 = blancLigne(text2[0], stringLength)
        newM = (textm1 - m1) + (textm2 - m2) + fm
        
        if(len(text1)>0):
            text1.pop() #O(1)
        if(len(text2)>0):
            text2.pop(0) #O(1)
        resultText = text1 + [fusionedString] + text2 #O(1)

        return True, newM, resultText #O(1)
    else:
        return False,0,[]

		
def equilibre(words, stringLength): #O(n^3)
    wordsCount = len(words)
    #La matrice qui contient tous les poids des configurations de texte differentes.
    #Initialise par maxInt
    weightMatrix = [[sys.maxint for _ in xrange(wordsCount)] for _ in xrange(wordsCount)]

    #La matrice qui contient les souslignes de textes pour chaque pas de programmation dynamique
    #Initialisee par listes vides
    stringMatrix = [[[] for _ in xrange(wordsCount)] for _ in xrange(wordsCount)]

    #Le parcours des diagonales commenceant d'element [0][0]
    k = 0;
    m = wordsCount;
    for s in range(0, m): #O(n^2/2)
        for i in range(k, wordsCount):
            j = i-k
            #print "###########################"
            #print "## Working with case",i,j,"##"
            #print "###########################"

            #Remplissage des diagonales
            if(i==j):
            #Remplissage des diagonales principales par mots seuls et poids des lignes avec un seul mot
                #print "Filling main diagonal case"
                weightMatrix[i][j] = blancLigne([words[i]], stringLength) #O(1)
                stringMatrix[i][j] = [[words[i]]] #O(1)
                #print "Weight of case", weightMatrix[i][j]
                #print "String in case", stringMatrix[i][j]
            else:
                #Remplissage des autres diagonales

                #Essayons de construire une nouvelle partie de texte a partir des construites les plus optimales
                #On peut concatener soustextes ou fusionner la derniere ligne de premier soustexte et premier ligne de deuxieme soustexte
                #en les concatenant si c'est possible
                column = j+1
                for row in range(j, i): #O(n)
                    #print "-----------------------------------------------------------------"
                    #Concatenations des soustextes
                    #print "Working with case ", row,j, " with text", stringMatrix[row][j]
                    #print "and case", i, column," with text", stringMatrix[i][column]
                    s = weightMatrix[row][j] + weightMatrix[i][column] #O(1)
                    
                    #print "*****************************************************************"
                    #print "Concatenation of these texts weights ", s
                    if(s < weightMatrix[i][j]):
                        #print "which is less than current value of case",weightMatrix[i][j]
                        weightMatrix[i][j] = s #O(1)
                        stringMatrix[i][j] = stringMatrix[row][j] + stringMatrix[i][column] #O(1)
                        #print "So, new text is", stringMatrix[i][j]
                    #else:
                        #print "But it's greater than the value already in case"
                    
                    #print "*****************************************************************"
                    #Essai de fusion des soustextes
                    fusion = fusionTextes(stringMatrix[row][j][:], stringMatrix[i][column][:], weightMatrix[row][j], weightMatrix[i][column], stringLength) #O(1)
                    #print "Now, I'm trying to make a fusion of textes in this cases: "
                    if(fusion[0] and fusion[1] < weightMatrix[i][j]):
                        #print "It's possible and the weight of this fusion is ", fusion[1]
                        #print "The text in the case is", fusion[2]
                        weightMatrix[i][j] = fusion[1] #O(1)
                        stringMatrix[i][j] = fusion[2] #O(1)
                    #else:
                        #print "But it's impossible or the weight of new text:",fusion[1]
                        #print "is greater than current: ",weightMatrix[i][j]
                    column = column + 1

        k = k+1;
        m = m-1;

    #print stringMatrix[wordsCount-1][0]
    #print weightMatrix[wordsCount-1][0]
    return stringMatrix[wordsCount-1][0], weightMatrix[wordsCount-1][0]

###########################################################################################################
############################### Algo avec etendu comme parametre ##########################################
###########################################################################################################

#Entree: text1: liste de listes des mots; text2: liste de listes des mots; stringLength:longeur de la ligne
#Sortie: Si c'est possible de fusionner la derniere proposition de text1 et la premiere proposition de text2,
#on les fusionne et retourne une liste qui contient True, la mesure de texte resultant, le texte resultant
#Sinon on retourne une liste qui contient False, 0 , liste vide
def fusionTextesEtendue(text1, text2, stringLength):
    #print "Try to fusion"
    fusionedString = text1[-1][:] + text2[0][:]
    if(possibleString(fusionedString, stringLength)):
        #print "Fusioned string: ", fusionedString
        #print "is possible"
        fusionedLength = longueur(fusionedString)
        #print "with length", fusionedLength
        if(len(text1)>0):
            text1.pop()
        if(len(text2)>0):
            text2.pop(0)
        
        resultText = text1 + [fusionedString] + text2
        #print "minmax for fusioned text:", etendue(resultText)
        
        
        return True, etendue(resultText), resultText
    else:
        #print "Fusion impossible"
        return False,[0,0],[]

def equilibreEtendue(words, stringLength): #O(n^4)
    wordsCount = len(words)
    #Initialise par maxInt
    
    #Les matrices qui contiennent la longueur de ligne de taille maximale/minimale dans le texte
    maxMatrix = [[sys.maxint for _ in xrange(wordsCount)] for _ in xrange(wordsCount)]
    minMatrix = [[0 for _ in xrange(wordsCount)] for _ in xrange(wordsCount)]
    
    #La matrice qui contient les sous-textes pour chaque pas de programmation dynamique
    #Initialisee par listes vides
    stringMatrix = [[[] for _ in xrange(wordsCount)] for _ in xrange(wordsCount)]
    
    #Le parcours des diagonales commenceant d'element [0][0]
    k = 0;
    m = wordsCount;
    for s in range(0, m): #O(n^2/2)
        for i in range(k, wordsCount):
            j = i-k
            #print "###########################"
            #print "## Working with case",i,j,"##"
            #print "###########################"
            
            #Remplissage des diagonales
            if(i==j):
                #Remplissage des diagonales principales par mots seuls et poids des lignes avec un seul mot
                #    print "Filling main diagonal case"
                
                minMatrix[i][j] = longueur([words[i]])
                maxMatrix[i][j] = longueur([words[i]])
                
                stringMatrix[i][j] = [[words[i]]]
            
            #   print "String in case", stringMatrix[i][j]
            #   print "Min value", minMatrix[i][j]
            #print "Max value", maxMatrix[i][j]
            else:
                #Remplissage des autres diagonales
                
                #Essayons de construire une nouvelle partie de texte a partir des construites les plus optimales
                #On peut concatener soustextes ou fusionner la derniere ligne de premier soustexte et premier ligne de deuxieme soustexte
                #en les concatenant si c'est possible
                column = j+1
                for row in range(j, i):
                    #Concatenations des soustextes
                    #print "Working with case ", row,j, "with text", stringMatrix[row][j], "difValue:", maxMatrix[row][j]-minMatrix[row][j]
                    #print "and case", i, column," with text", stringMatrix[i][column], "difValue:", maxMatrix[row][j]-minMatrix[row][j]
                    d = max([maxMatrix[row][j], maxMatrix[i][column]]) - min([minMatrix[row][j], minMatrix[i][column]])
                    #print "Max-Min for concatenation", d
                    #print "Current value", maxMatrix[i][j]-minMatrix[i][j]
                    
                    if(d < maxMatrix[i][j] - minMatrix[i][j]):
                        #print "Now Min = ", minMatrix[i][j]
                        maxMatrix[i][j] = max([maxMatrix[row][j], maxMatrix[i][column]])
                        #print "Max = ", maxMatrix[i][j]
                        stringMatrix[i][j] = stringMatrix[row][j] + stringMatrix[i][column]
                    #print "New string = ", stringMatrix[i][j]
                    
                    #Essai de fusion des soustextes
                    fusion = fusionTextesEtendue(stringMatrix[row][j][:], stringMatrix[i][column][:], stringLength)
                    if(fusion[0] and fusion[1] < maxMatrix[i][j] - minMatrix[i][j]):
                        maxMatrix[i][j] = plusLong(fusion[2])
                        minMatrix[i][j] = plusCourt(fusion[2])
                        stringMatrix[i][j] = fusion[2]
                    #print "Placed string", fusion[2]
                    
                    column = column + 1
        
        k = k+1;
        m = m-1;
    
    #print "Result string:", stringMatrix[wordsCount-1][0]
    #print "Result dif:", maxMatrix[wordsCount-1][0] - minMatrix[wordsCount-1][0]
    return stringMatrix[wordsCount-1][0], maxMatrix[wordsCount-1][0] - minMatrix[wordsCount-1][0]

def main():
	f=choix
	decoupage(f)


if __name__ == "__main__":
	#creation du memo
	main()
