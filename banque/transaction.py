class Transaction:
    def __init__(self, date, client_id, montant, type_transaction, compte_destinataire=None):
        self.date = date
        self.client_id = client_id
        self.montant = montant
        self.type_transaction = type_transaction
        self.compte_destinataire = compte_destinataire
