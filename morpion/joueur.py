class Joueur:
    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

    def obtenir_coup(self):
        ligne = int(input(f"{self.nom}, entrez la ligne (0, 1, 2): "))
        colonne = int(input(f"{self.nom}, entrez la colonne (0, 1, 2): "))
        return ligne, colonne
