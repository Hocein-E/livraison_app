class Depot:
    def __init__(self):
        self.vehicules_disponibles = []
        self.livreurs_disponibles = []
        self.commandes = []

    def ajouter_vehicule(self, vehicule):
        self.vehicules_disponibles.append(vehicule)

    def ajouter_livreur(self, livreur):
        self.livreurs_disponibles.append(livreur)

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def attribuer_vehicule(self, livreur, vehicule):
        if vehicule.utilise or livreur.vehicule:
            return False
        livreur.vehicule = vehicule
        vehicule.utilise = True
        return True
