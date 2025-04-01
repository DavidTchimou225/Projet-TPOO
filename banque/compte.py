from abc import ABC, abstractmethod

class SoldeInsuffisantException(Exception):
    pass

class LimiteRetraitDepasseeException(Exception):
    pass

class Compte(ABC):
    def __init__(self, numero_compte, solde=0):
        self.numero_compte = numero_compte
        self.solde = solde

    @abstractmethod
    def retirer(self, montant):
        pass

    def deposer(self, montant):
        self.solde += montant

    def transferer(self, autre_compte, montant):
        if self.retirer(montant):
            autre_compte.deposer(montant)
            return True
        return False

class CompteBronze(Compte):
    LIMITE_RETRAIT = 500000

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
        if montant > self.LIMITE_RETRAIT:
            raise LimiteRetraitDepasseeException("Limite de retrait dépassée.")
        self.solde -= montant
        return True

class CompteOr(Compte):
    LIMITE_RETRAIT = 1000000

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
        if montant > self.LIMITE_RETRAIT:
            raise LimiteRetraitDepasseeException("Limite de retrait dépassée.")
        self.solde -= montant
        return True

class CompteAffaires(Compte):
    LIMITE_RETRAIT = 20000000

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour effectuer le retrait.")
        if montant > self.LIMITE_RETRAIT:
            raise LimiteRetraitDepasseeException("Limite de retrait dépassée.")
        self.solde -= montant
        return True
