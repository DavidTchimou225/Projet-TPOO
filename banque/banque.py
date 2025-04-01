class Banque:
    def __init__(self):
        self.clients_utilisateurs = []
        self.clients_entreprises = []
        self.employes = []
        self.transactions = []

    def ajouter_client_utilisateur(self, client):
        self.clients_utilisateurs.append(client)

    def ajouter_client_entreprise(self, client):
        self.clients_entreprises.append(client)

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def ajouter_transaction(self, transaction):
        self.transactions.append(transaction)
