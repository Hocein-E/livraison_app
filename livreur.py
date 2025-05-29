class Livreur:
    def __init__(self, nom):
        self.nom = nom
        self.vehicule = None
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)
        commande.statut = "en cours"

    def effectuer_livraison(self):
        details = ""
        for cmd in self.commandes:
            cmd.statut = "livrée"
            details += f"- {cmd}\n"
        self.commandes = []
        return details or "Aucune commande à livrer"

    @staticmethod
    def verifier_nom(nom):
        return nom.isalpha()

    def __str__(self):
        veh = self.vehicule.immatriculation if self.vehicule else "Aucun véhicule"
        return f"{self.nom} - Véhicule: {veh} - Commandes: {len(self.commandes)}"
