from banque.banque import Banque
from banque.compte import CompteBronze, CompteOr
from morpion.partie import Partie

def main():
    # Exemple d'utilisation de la banque
    banque = Banque()
    compte_bronze = CompteBronze("123456", 1000000)
    compte_or = CompteOr("654321", 2000000)

    try:
        compte_bronze.retirer(600000)  # Devrait lever une exception
    except Exception as e:
        print(e)

    compte_bronze.deposer(500000)
    print(compte_bronze.solde)

    compte_or.transferer(compte_bronze, 300000)
    print(compte_bronze.solde)
    print(compte_or.solde)

    # Exemple d'utilisation du jeu de morpion
    partie = Partie()
    partie.jouer()

if __name__ == "__main__":
    main()
