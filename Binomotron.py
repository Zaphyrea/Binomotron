
import random # importe module random (génère nombres aléatoires)
import mysql.connector # importe module mysql (permet connexion et interaction avec la bdd de MySQL)

connexion = mydb = mysql.connector.connect(  #fonction établit connexion avec bdd MySQL avec paramètres ci-dessous
                                                # la connexion est assignée aux variables 'connexion' et 'mydb'
  host="localhost",
  port="3307",
  user="root",
  password="example",
  database="Binomotron"  
)  

mycursor=mydb.cursor() # créé objet curseur à partir de bdd. L'objet sera utilisé pour 
                        # exécuter des requêtes SQL et interagir avec la bdd

#Ce code regroupe une liste d'apprenants depuis la bdd MySQL.
bdd_apprenants = []  # création liste qui récupère les noms des apprenants de la bdd
curseur = connexion.cursor()   # créer un nouvel objet de curseur à partir de la connexion à la bdd
curseur.execute("SELECT nom FROM apprenants")  # exécute requête SQL pour récupérer les noms depuis la table apprenants
for ligne in curseur.fetchall():  # la boucle parcourt toutes les lignes de résultats retournées par la requête
    bdd_apprenants.append(ligne[0])  # Ajoute le nom de chaque apprenant à la liste bdd_apprenants. 
#La valeur ligne[0] correspond à la première colonne (dans ce cas, la colonne "nom") de la ligne de résultat. 
#une fois boucle terminée, la liste bdd_apprenants contient tous les noms


# Fonction de randomisation et répartition
def regrouper_apprenants(apprenants):    # créé fonction qui regroupe apprenants
    random.shuffle(apprenants)           # randomise la liste des apprenants
    binomes = []                         # créé liste vide qui sera remplie par les binômes après
    if len(apprenants) % 2 != 0:         # vérifie si le nombre d'apprenants est impair 
        binomes.append((apprenants.pop(), None))    # si le nombre d'apprenants est impair, un None est ajouté à un binôme
    while len(apprenants) > 1:                   # tant qu'il reste au moins 2 apprenants dans la liste
        binomes.append((apprenants.pop(), apprenants.pop())) # ajoute un binôme avec 2 apprenants
        # le .pop permet de retirer l'élément désigné de la liste et d'envoyer sa valeur (il faut le répéter pour enlever les 2 apprenants)
    return binomes       # retourne la liste 'binomes'


binomes = regrouper_apprenants(bdd_apprenants) # Appelle fonction regrouper_apprenants.
#Les binômes formés sont assignés à la variable 'binomes'


for i, binome in enumerate(binomes):         # la boucle for cherche l'indice (i) et la valeur de chaque 'binome'
    print(f"Binôme {i+1}: {binome[0]} et {binome[1]}")      # Affiche le numéro du binôme et le nom des 2 
                                                    #apprenants sélectionnés. Rajoute 1 au numéro à chaque itération


# Fermeture de la connexion à la base de données
connexion.close()



# pas nécessaire de fermer 'mydb', car c'est un alias de la variable 'connexion'