from .grille import Grille
from .joueur import Joueur

class Partie:
    def __init__(self):
        self.grille = Grille()
        self.joueurs = [Joueur("Joueur 1", "X"), Joueur("Joueur 2", "O")]
        self.joueur_courant = 0

    def jouer(self):
        while True:
            self.grille.afficher()
            joueur = self.joueurs[self.joueur_courant]
            ligne, colonne = joueur.obtenir_coup()
            if self.grille.placer_symbole(ligne, colonne, joueur.symbole):
                if self.grille.verifier_gagnant(joueur.symbole):
                    self.grille.afficher()
                    print(f"{joueur.nom} a gagné !")
                    break
                if self.grille.est_pleine():
                    self.grille.afficher()
                    print("Match nul !")
                    break
                self.joueur_courant = 1 - self.joueur_courant
            else:
                print("Case déjà occupée, essayez à nouveau.")
