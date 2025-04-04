
class ClientUtilisateur:
    def __init__(self, nom, adresse, telephone, cnic, login, mot_de_passe):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.cnic = cnic
        self.login = login
        self.mot_de_passe = mot_de_passe
        self.comptes = []

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

#Agrégation
class ClientEntreprise:
    def __init__(self, nom_entreprise, adresse, numero_fiscal, login, mot_de_passe):
        self.nom_entreprise = nom_entreprise
        self.adresse = adresse
        self.numero_fiscal = numero_fiscal
        self.login = login
        self.mot_de_passe = mot_de_passe
        self.comptes = []

    def ajouter_compte(self, compte):
        self.comptes.append(compte)
