class Vehicule:
    def __init__(self, marque, modele, immatriculation):
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation
        self.utilise = False

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"

class Camion(Vehicule):
    def __init__(self, marque, modele, immatriculation, capacite):
        super().__init__(marque, modele, immatriculation)
        self.capacite = capacite

    def __str__(self):
        return f"Camion - {super().__str__()} - Capacité: {self.capacite} t"

class Moto(Vehicule):
    def __init__(self, marque, modele, immatriculation, vitesse):
        super().__init__(marque, modele, immatriculation)
        self.vitesse = vitesse

    def __str__(self):
        return f"Moto - {super().__str__()} - Vitesse: {self.vitesse} km/h"
