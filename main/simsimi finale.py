def reset():
    exit=open("texte","w")
    exit.write("1ere ligne")
    exit.write("\n")
    exit.close

def texte ():
    question=0
    reponse=("posez moi une question")
    while question!=("stop"):
        fiche=open("texte","r")
        data=fiche.read()
        fiche.close()
        data=data.splitlines()
        print(data)
        question=input(reponse)
        for i,ligne in enumerate(data):
                if question in ligne:
                    print("ok")
                    reponse=(data[i+1])
                    break
        if question not in data:
                    ecriture=open("texte","a")
                    ecriture.write(question)
                    ecriture.write("\n")
                    ecriture.write(input("je ne connais pas cette reponse, que dois-je repondre?"))
                    ecriture.write("\n")
                    ecriture.close()
                    reponse=("repose moi une autre question")