# Déclaration des listes pour stocker les informations
prenom = []
nom = []
note = []
moyenne = []
classe = []
# Demander à l'utilisateur de saisir la taille du tableau
taille = int(input("Combien de tableau voulez-vous saisir ? "))
for i in range(taille) :
    print(f'\nSaisie la personne {i+1}')
    prenom.append(input('prenom :'))
    nom.append(input('nom :'))
    note.append(float(input('note :')))
    moyenne.append(float(input('moyenne :')))
    classe.append(input('classe :'))
 
for pre, nm, nte, moyen, cls in zip (prenom, nom, note, moyenne, classe) :
    print(f"information de chaque personne: {pre},  {nm}, {nte}, {moyen},{cls}")