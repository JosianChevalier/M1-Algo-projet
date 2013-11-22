import sys

#Entree: words: liste des mots, stringLength: longeur d'une ligne
#Sortie: le nombre des espaces qui restent dans la ligne de longeur "stringLength" apres y avoir mis la sentence a partir des mots de "words"
def spacesLeft(words, stringLength):
        for x in range(0, len(words)):
                stringLength -= len(words[x]);

        stringLength -= len(words)-1;
        return stringLength;

#Entree: words: liste des mots, stringLength: longeur d'une ligne
#Sortie: le nombre des espaces en carre qui restent dans la ligne de longeur "stringLength" apres y avoir mis la sentence a partir des mots de "words"
def spacesLeftSquared(words, stringLength):
        return pow(spacesLeft(words, stringLength), 2)

def measureOfTextEquilibrium(text, stringLength):
		somme = 0;
		for i in range(0, len(text)):
			somme += spacesLeftSquared(text[i], stringLength)
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
				weightMatrix[i][j] = spacesLeftSquared([words[i]], stringLength)
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
					print "First part coord", row, j
					print "First part:", stringMatrix[row][j]
					print "First fusioned:", stringMatrix[row][j][-1]
					print "Second part coord", i, column
					print "Second part:", stringMatrix[i][column]
					print "Second fusioned", stringMatrix[i][column][0]
					fusionedString = stringMatrix[row][j][-1] + stringMatrix[i][column][0]
					print "Concat fusioned",fusionedString
					if(possibleString(fusionedString, stringLength)):
						print "Can put"
						text1 = stringMatrix[row][j][:]
						text2 = stringMatrix[i][column][:]
						if(len(text1)>0):
							text1.pop()
						print "First third ", text1
						if(len(text2)>0):
							text2.pop(0)
						print "Third third", text2
						resultText = text1 + [fusionedString] + text2
						print "Result", resultText
						sp = measureOfTextEquilibrium(resultText, stringLength)
						if(sp < weightMatrix[i][j]):
							print "Put fusioned"
							print "Value", sp
							print "Fusioned text",resultText
							weightMatrix[i][j] = sp
							stringMatrix[i][j] = resultText
							
					column = column + 1
				

			
			print "Placed val",weightMatrix[i][j]
			print "Placed string",stringMatrix[i][j]
			print "##################"
			#print weightMatrix
			#print stringMatrix
		k = k+1;
		m = m-1;
		print "____________________"	
				
	print stringMatrix[wordsCount-1][0]
	print measureOfTextEquilibrium(stringMatrix[wordsCount-1][0], stringLength)


equilibrium(["la", "programmation", "dynamique", "est", "une", "strategie", "algorithmique"], 17)