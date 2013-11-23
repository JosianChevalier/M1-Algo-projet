import sys
from fonctions_diverses import formate, args_corrects, enregistre, list_to_text, decoupage, blancLigne

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
		
def fusionTextes(text1, text2, stringLength):
	fusionedString = text1[-1][:] + text2[0][:]
	if(possibleString(fusionedString, stringLength)):
		t1 = text1[:]
		t2 = text2[:]
		if(len(text1)>0):
			text1.pop()
		if(len(text2)>0):
			text2.pop(0)
		resultText = text1 + [fusionedString] + text2
		
		return True, measureOfTextEquilibrium(resultText, stringLength), resultText
	else:
		return False,0,[]

		
def equilibrium(words, stringLength):
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
	for s in range(0, m):
		for i in range(k, wordsCount):
			j = i-k;
			
			#Remplissage des diagonales
			if(i==j):
				#Remplissage des diagonales principales par mots seuls et poids des lignes avec un seul mot
				weightMatrix[i][j] = blancLigne([words[i]], stringLength)
				stringMatrix[i][j] = [[words[i]]]
			else:
				#Remplissage des autres diagonales
				
				#Essayons de construire une nouvelle partie de texte a partir des construites les plus optimales
				#On peut concatener soustextes ou fusionner la derniere ligne de premier soustexte et premier ligne de deuxieme soustexte
				#en les concatenant si c'est possible
				column = j+1
				for row in range(j, i):
					#Concatenations des soustextes
					s = weightMatrix[row][j] + weightMatrix[i][column]
					if(s < weightMatrix[i][j]):
						weightMatrix[i][j] = s
						stringMatrix[i][j] = stringMatrix[row][j] + stringMatrix[i][column]
						
					#Essai de fusion des soustextes
					fusion = fusionTextes(stringMatrix[row][j][:], stringMatrix[i][column][:], stringLength)
					if(fusion[0] and fusion[1] < weightMatrix[i][j]):
						weightMatrix[i][j] = fusion[1]
						stringMatrix[i][j] = fusion[2]

					column = column + 1
					
		k = k+1;
		m = m-1;
				
	print stringMatrix[wordsCount-1][0]
	print measureOfTextEquilibrium(stringMatrix[wordsCount-1][0], stringLength)
	return stringMatrix[wordsCount-1][0], measureOfTextEquilibrium(stringMatrix[wordsCount-1][0], stringLength)

def main():
	f=equilibrium
	decoupage(f)


if __name__ == "__main__":
	#creation du memo
	main()