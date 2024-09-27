# Fonction pour afficher le menu principal
def afficher_menu():
    print("1. Solde de mon compte")
    print("2. Transfert d’argent")
    print("3. Paiement de facture")
    print("4. Achats de crédit")
    print("5. Quitter")

# Fonction pour afficher le solde
def afficher_solde(compte):
    print("Le solde de votre compte est de :", compte, "FCFA")

# Fonction pour le transfert d'argent
def transfert_argent(compte):
    print("1. Saisir le montant du transfert")
    print("2. Quitter")
    sous_choix = int(input("Veuillez saisir une option : "))
    
    if sous_choix == 1:
        montant = float(input("Veuillez saisir le montant du transfert : "))
        if montant > compte:
            print("Votre solde est insuffisant pour effectuer ce transfert.")
            afficher_solde(compte)
        else:
            compte -= montant
            print("Transfert réussi !")
            afficher_solde(compte)
    exit() 

def paiement_facture(compte):
    print("1. Payer par liquide")
    print("2. Payer par chèque")
    print("3. Quitter")
    choix_paiement = int(input("Veuillez choisir une méthode de paiement : "))

    if choix_paiement == 1:
        montant = float(input("Veuillez saisir le montant à payer : "))
        if montant > compte:
            print("Votre solde est insuffisant pour effectuer ce paiement.")
        else:
            compte -= montant
            print("Paiement par liquide réussi !")
        afficher_solde(compte)
    elif choix_paiement == 2:
        montant = float(input("Veuillez saisir le montant du chèque : "))
        if montant > compte:
            print("Votre solde est insuffisant pour effectuer ce paiement.")
        else:
            compte -= montant
            print("Paiement par chèque réussi !")
        afficher_solde(compte)

    exit() 

# Fonction pour l'achat de crédit
def achat_credit(compte):
    numero_telephone = input("Veuillez entrer le numéro de téléphone : ")
    montant_credit = float(input("Veuillez entrer le montant du crédit : "))
    if montant_credit > compte:
        print("Votre solde est insuffisant pour acheter ce crédit.")
    else:
        compte -= montant_credit
        print(f"Achat de {montant_credit} FCFA de crédit réussi pour le numéro {numero_telephone}.")
        afficher_solde(compte)

    exit() 

# Programme principal
def main():
    compte = 200000
    x = input("Veuillez saisir le code (#144#) : ")

    if x != "#144#":
        print("Veuillez saisir le code valide : #144#")
    else:
        afficher_menu()
        choix = int(input("Veuillez choisir une option : "))
        
        if choix == 1:
            # Option 1 : Solde de mon compte
            afficher_solde(compte)
        
            exit()  # Terminer après l'affichage du solde
        
        elif choix == 2:
            # Option 2 : Transfert d'argent
            compte = transfert_argent(compte)
        
        elif choix == 3:
            # Option 3 : Paiement de facture
            compte = paiement_facture(compte)
        
        elif choix == 4:
            # Option 4 : Achats de crédit
            compte = achat_credit(compte)
        
        elif choix == 5:
            # Option 5 : Quitter
            print("Merci d'avoir utilisé Orange Money. À bientôt !")
            exit()  # Terminer le programme
        
        else:
            print("Option invalide. Le programme va se terminer.")
            exit()  # Terminer si une option invalide est choisie

# Lancement du programme principal
if __name__ == "__main__":
    main()
