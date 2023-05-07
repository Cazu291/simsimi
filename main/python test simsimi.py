def test ():
    fichier=open("simsimi","a")
    fichier.write("ce test est reussi\n")
    fichier.close
    fichier=open("simsimi","r")
    for ligne in fichier:
       print (ligne)
    fichier.close

def exit ():
    exit=open("texte","w")
    exit.write("1ere ligne")

def texte ():
    question=input("entrez une question")
    while question!=("stop"):
        question=input("entrez une question")
        try:
            fiche=open("texte","r")
            for ligne in fiche:
                if ligne==question:
                    print(ligne+1)
            fiche.close
        except:
            ecriture=open("texte","a")
            ecriture.write(question)
            ecriture.write("\n")
            ecriture.write(input("entrer la reponse"))
            ecriture.close