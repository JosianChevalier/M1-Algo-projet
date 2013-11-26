# -*- coding: UTF-8 -*-
import os, subprocess

#teste si int est une chaine de caractère représentant un entier
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def main():

    #---------------Choix de l'algo---------------

    print "Choisissez l'algo a tester : "
    print "[1] : Algorithme de force brute"
    print "[2] : Algorithme glouton"
    print "[3] : Programmation dynamique : matrice bottom-up"
    print "[4] : Programmation dynamique : memoization bottom-up"
    print "[5] : Programmation dynamique : memoization top-down"
    choix=raw_input("Entrez le numéro de l'algo à tester : ")
    while choix not in ["1","2","3","4","5"]: #tant que l'utilisateur n'a pas rentré un nombre correspondantà un algo
        choix=raw_input("Erreur ! Entrez un nombre de  1 à 5 correspondant à l'algo : ") #on l'invite à retenter
    choix=int(choix)


    #---------------Choix de la longueur d'une ligne---------------
    length_line=raw_input("Nombre de caractère par ligne (par défaut 60) : ")
    while not (is_int(length_line) or length_line==""):
        length_line=raw_input("Erreur ! Entrez un entier : ")
    if length_line=="": #si l'utilisateur n'a rien rentré, 60 par défaut
        length_line=60
    else :
        length_line=int(length_line)        
    
    if choix==1:
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test10.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test20.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test30.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test40.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test50.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test60.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test70.txt", "destination.txt"))
        os.system("python algo_force_brute.py --lengthline %i %s %s" % (length_line, "test80.txt", "destination.txt"))
    elif choix==2:
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test10.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test50.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test100.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test200.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test300.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test400.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test500.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test600.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test700.txt", "destination.txt"))
        os.system("python algo_glouton.py --lengthline %i %s %s" % (length_line, "test800.txt", "destination.txt"))
    elif choix==3:
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test10.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test50.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test100.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test200.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test300.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test400.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test500.txt", "destination.txt"))
        os.system("python algo_matrices_bottom-up.py --lengthline %i %s %s" % (length_line, "test600.txt", "destination.txt"))
    elif choix==4:
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test10.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test50.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test100.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test200.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test300.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test400.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test500.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test600.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test700.txt", "destination.txt"))
        os.system("python algo_memoization_bottom-up.py --lengthline %i %s %s" % (length_line, "test800.txt", "destination.txt"))
    elif choix==5:
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test10.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test50.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test100.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test200.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test300.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test400.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test500.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test600.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test700.txt", "destination.txt"))
        os.system("python algo_memoization_top-down.py --lengthline %i %s %s" % (length_line, "test800.txt", "destination.txt"))
       
if __name__ == "__main__":
    main()
