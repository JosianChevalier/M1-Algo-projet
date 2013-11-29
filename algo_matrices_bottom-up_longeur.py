import sys
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage, blancLigne, measureOfTextEquilibrium, possibleString, longueur, longShortDistance

#Entree: text1: liste de listes des mots; text2: liste de listes des mots; stringLength:longeur de la ligne
#Sortie: Si c'est possible de fusionner la derniere proposition de text1 et la premiere proposition de text2,
#on les fusionne et retourne une liste qui contient True, la mesure de texte resultant, le texte resultant
#Sinon on retourne une liste qui contient False, 0 , liste vide
def fusionTextsMinMax(text1, text2, stringLength):
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
        #print "minmax for fusioned text:", longShortDistance(resultText)


        return True, longShortDistance(resultText), resultText
    else:
        #print "Fusion impossible"
        return False,[0,0],[]



def equilibrium(words, stringLength): #O(n^4)
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
                    fusion = fusionTextsMinMax(stringMatrix[row][j][:], stringMatrix[i][column][:], stringLength)
                    if(fusion[0] and fusion[1][0] - fusion[1][1] < maxMatrix[i][j] - minMatrix[i][j]):
                        maxMatrix[i][j] = fusion[1][0]
                        minMatrix[i][j] = fusion[1][1]
                        stringMatrix[i][j] = fusion[2]
                    #print "Placed string", fusion[2]

                    column = column + 1

        k = k+1;
        m = m-1;

    #print "Result string:", stringMatrix[wordsCount-1][0]
    #print "Result dif:", maxMatrix[wordsCount-1][0] - minMatrix[wordsCount-1][0]
    return stringMatrix[wordsCount-1][0], maxMatrix[wordsCount-1][0] - minMatrix[wordsCount-1][0]

def main():
	f=equilibrium
	decoupage(f)


if __name__ == "__main__":
	#creation du memo
	main()
