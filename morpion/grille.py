class Grille:
    def __init__(self):
        self.grille = [[' ' for _ in range(3)] for _ in range(3)]

    def afficher(self):
        for ligne in self.grille:
            print('|'.join(ligne))
            print('-' * 5)

    def placer_symbole(self, ligne, colonne, symbole):
        if self.grille[ligne][colonne] == ' ':
            self.grille[ligne][colonne] = symbole
            return True
        return False

    def est_pleine(self):
        return all(case != ' ' for ligne in self.grille for case in ligne)

    def verifier_gagnant(self, symbole):
        for i in range(3):
            if all(self.grille[i][j] == symbole for j in range(3)) or \
               all(self.grille[j][i] == symbole for j in range(3)):
                return True
        if all(self.grille[i][i] == symbole for i in range(3)) or \
           all(self.grille[i][2 - i] == symbole for i in range(3)):
            return True
        return False
