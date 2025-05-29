class Commande:
    def __init__(self, id, destination, poids):
        self.id = id
        self.destination = destination
        self.poids = poids
        self.statut = "en attente"

    @staticmethod
    def valider_poids(poids):
        try:
            poids = float(poids)
            return 0 < poids <= 100
        except:
            return False

    def __str__(self):
        return f"{self.id} - {self.destination} - {self.poids} kg - {self.statut}"
