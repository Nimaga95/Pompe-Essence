# Etape 1

print("Configuration de la pompe à essence ....")
prix_essence_ordinaire = float(input("Prix de l'essence ordinaire ($/L) : "))
prix_essence_diesel = float(input("Prix de l'essence diesel ($/L): "))
prix_essence_super = (1.1 * prix_essence_ordinaire)
code_promo = input("Le code secret du jour est : ")

print("*" * 8)

# Etape 2

print("Une automobile arrive.")
capacite_reservoir = float(input("Le nombre de litre  total de son reservoir est : "))
contenu_reservoir = float(input("et il en contient actuellemnt : "))

if contenu_reservoir < capacite_reservoir:
    print("*" * 10, "Affichage sur la pompe", "*" * 10)
else:
    print("Erreur : Le nombre de litre d'essence contenu dans le reservoir doit être inférieur à sa capacité")

# Etape 3

print("Veuillez sélectionner le type d'essence parmi :")
print("- [O]rdinaire : ", "{:.2f}".format(prix_essence_ordinaire), "$ / litre")
print("- [D]iesel : ", "{:.2f}".format(prix_essence_diesel), "$ / litre")
print("- [S]uper : ", "{:.2f}".format(prix_essence_super), "$ / litre")

choix_essence = (input("Votre choix d'essence (O, S ou D) : ")).lower()

# On crée une variable prix_essence dans laquelle on viendra stocker le prix de l'essence en fonction du choix d'essence

prix_essence = 0

if choix_essence == "o":
    prix_essence = prix_essence_ordinaire
elif choix_essence == "d":
    prix_essence = prix_essence_diesel
elif choix_essence == "s":
    prix_essence = prix_essence_super
else:
    print("Erreur : Vous devez choisir entre (O, D ou S)")

# Etape 4 : On suppose que montant_saisi = 0 pour commencer pour avoir la variable montant_saisi dans la mémoire
# qui viendra garder le montant démandé par le client si choix_remplissage = M

montant_saisi = 0

choix_remplissage = input("Souhaitez vous faire le plein (P) ou choisir un montant fixe (M) ? : ").lower()

if choix_remplissage == "p":
    print("Remplissage !")
elif choix_remplissage == "m":
    montant_saisi = float(input("Veuillez inscire le montant souhaité : "))
    print("Remplissage !")
else:
    print("Erreur : Vous devez choisir entre (M ou P)")

# Etape 5 : Création de la Boucle While pour le remplissage litre par litre
# creation de deux variables montant_a_payer et reste_reservoir, on suppose qu'elles sont à zéro pour commencer
# on viendra stocker dans ses variables les contenus du rerservoir  et le montant dû après chaque remplissage.
# On crée aussi la variable ordre_priorite (un boléen) qui va jouer l'arbitre dans des
# cas speciaux (montant demandé proche d'atteindre la limite avant le plein ou reservoir plein avant montant demandé)
# et enfin la variable remplissage (un boléen) qui va gérer notre remplissage

montant_a_payer = 0
reste_reservoir = 0
ordre_priorite = True
remplissage = True

while remplissage:
    reponse_client = input("Appuyer sur entrée pour continuer à remplir (A pour arrêter). ")
    if reponse_client == "":
        if choix_remplissage == "p":
            if capacite_reservoir - contenu_reservoir >= 1:
                contenu_reservoir = contenu_reservoir + 1
                montant_a_payer = montant_a_payer + prix_essence
                print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir), "litres sur",
                      "{:.2f}".format(capacite_reservoir))
                print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
                remplissage = True
                if capacite_reservoir - contenu_reservoir == 0:
                    print("Terminé !")
                    remplissage = False
            elif capacite_reservoir - contenu_reservoir < 1 != 0:
                reste_reservoir = capacite_reservoir - contenu_reservoir
                contenu_reservoir = contenu_reservoir + reste_reservoir
                montant_a_payer = montant_a_payer + prix_essence * reste_reservoir
                print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir), "litres sur",
                      "{:.2f}".format(capacite_reservoir))
                print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
                print("Terminé !")
                remplissage = False
        elif choix_remplissage == "m":
            if (capacite_reservoir - contenu_reservoir) / 1 <= (montant_saisi - montant_a_payer) / prix_essence:
                ordre_priorite = False
                if capacite_reservoir - contenu_reservoir >= 1:
                    contenu_reservoir = contenu_reservoir + 1
                    montant_a_payer = montant_a_payer + prix_essence
                    print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir), "litres sur",
                          "{:.2f}".format(capacite_reservoir))
                    print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
                    remplissage = True
                    if capacite_reservoir - contenu_reservoir == 0:
                        print("Terminé !")
                        remplissage = False
                elif capacite_reservoir - contenu_reservoir < 1 != 0:
                    reste_reservoir = capacite_reservoir - contenu_reservoir
                    contenu_reservoir = contenu_reservoir + reste_reservoir
                    montant_a_payer = montant_a_payer + prix_essence * reste_reservoir
                    print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir), "litres sur",
                          "{:.2f}".format(capacite_reservoir))
                    print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
                    print("Terminé !")
                    remplissage = False
            else:
                ordre_priorite = True
                if montant_a_payer + prix_essence <= montant_saisi:
                    contenu_reservoir = contenu_reservoir + 1
                    montant_a_payer = montant_a_payer + prix_essence
                    print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir),
                          "litres sur", "{:.2f}".format(capacite_reservoir))
                    print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
                    remplissage = True
                    if montant_a_payer - montant_saisi == 0:
                        remplissage = False
                elif montant_a_payer + prix_essence > montant_saisi:
                    contenu_reservoir = contenu_reservoir + (montant_saisi - montant_a_payer) / prix_essence
                    montant_a_payer = montant_a_payer + (montant_saisi - montant_a_payer)
                    print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir),
                          "litres sur", "{:.2f}".format(capacite_reservoir))
                    print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
                    print("Terminé !")
                    remplissage = False
    elif reponse_client.lower() == "a":
        print("État du reservoir d'essence : ", "{:.2f}".format(contenu_reservoir),
              "litres sur", "{:.2f}".format(capacite_reservoir))
        print("Coût (jusqu'à maintenant) : ", "{:.2f}".format(montant_a_payer), "$")
        print("Terminé !")
        remplissage = False
print("-" * 55)

# Etape 7 : Code promotionnel

validation_code_promo = input("Si vous connaissez le code promotionnel RABAIS+, entrez-le maitenant pour obtenir 30% "
                              "de rabais: ")
if validation_code_promo == code_promo:
    print("Code valide.")
    print("-" * 55)
    montant_final = montant_a_payer * 0.7
    print("Le montant final est : ", "{:.2f}".format(montant_final), "$")
else:
    print("Code non valide.")
    print("-" * 55)
    print("Le montant final est :", "{:.2f}".format(montant_a_payer), "$")
print("Faites bonne route !")
