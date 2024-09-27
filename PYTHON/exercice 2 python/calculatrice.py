def affiche_menu():
    print("1. Faire la somme de deux valeurs")
    print("2. Faire la soustraction de deux valeurs")
    print("3. Faire le produit de deux valeurs")
    print("4. Faire la division de deux valeurs")
    print("5. Quitter")
def demander_valeurs():
    num1 = float(input("Entrer la premiere valeur : "))
    num2 = float(input("Entrer la deuxieme valeur : "))
    return num1, num2
# programme principal
def main():
    while True:
        affiche_menu()
        choix = float(input("Veillez choicir une option"))
        if choix == 1:
            num1, num2 = demander_valeurs()
            resultat = num1 + num2
            print(f"La somme de {num1}, et {num2} est : {resultat}")
            break
        elif choix == 2:
            num1, num2 = demander_valeurs()
            resultat = num1 - num2
            print(f"La soustraction de {num1}, et {num2} est : {resultat}")
            break
        elif choix == 3:
            num1, num2 = demander_valeurs()
            resultat = num1 * num2
            print(f"Le produit de {num1}, et {num2} est : {resultat}")
            break
        elif choix == 4:
            num1, num2 = demander_valeurs()
            if num1 != 0:
                resultat = num1 / num2
                print(f"La division de {num1}, et {num2} est : {resultat}")
            else:
                print("Impossible de faire la devision par zero")
                break
        elif choix == 5:
            print("Quitter")
            break
if __name__ == "__main__":
    main()