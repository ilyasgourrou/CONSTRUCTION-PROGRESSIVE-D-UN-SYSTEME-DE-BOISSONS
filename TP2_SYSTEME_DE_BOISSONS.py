# Partie 1 & 2 : Structure de base et boissons
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Classe abstraite Boisson
class Boisson(ABC):

    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    # Partie 4  
    def __add__(self, other):
        return BoissonComposee(self, other)

# Boissons concretes
class Cafe(Boisson):
    def cout(self):
        return 2.0
    def description(self):
        return "Cafe simple"

class The(Boisson):
    def cout(self):
        return 1.5
    def description(self):
        return "The"

# Nouvelle boisson : Jus Orange
class JusOrange(Boisson):
    def cout(self):
        return 3.0
    def description(self):
        return "Jus d'orange "

# Nouvelle boisson : Soda
class Soda(Boisson):
    def cout(self):
        return 2.5
    def description(self):
        return "Soda"

# Partie 3 : Ajout d'ingredients 
class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson

class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
    def description(self):
        return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2
    def description(self):
        return self._boisson.description() + ", Sucre"

#  ajout Caramel
class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.7
    def description(self):
        return self._boisson.description() + ", Caramel"

# Partie 4 : Combinaison de boissons
class BoissonComposee(Boisson):
    def __init__(self, boisson1, boisson2):
        self.boisson1 = boisson1
        self.boisson2 = boisson2
    def cout(self):
        return self.boisson1.cout() + self.boisson2.cout()
    def description(self):
        return self.boisson1.description() + " + " + self.boisson2.description()

# Partie 5 : Representation d'un client
@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

# Partie 7 : Gestion des commandes
class Commande:
    def __init__(self, client: Client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson: Boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher_contenu(self):
        desc = ", ".join(b.description() for b in self.boissons)
        print(f"Commande : {desc}")
        print(f"Prix : {self.prix_total():.2f}€")

# Types de commandes
class CommandeSurPlace(Commande):
    def afficher_contenu(self):
        print("**** Commande sur place ***")
        super().afficher_contenu()

class CommandeEmporter(Commande):
    def afficher_contenu(self):
        print("**** Commande à emporter ****")
        super().afficher_contenu()

# Programme de fidelite
class Fidelite:
    def ajouter_points(self, client: Client, montant):
        points = int(montant)  
        client.points_fidelite += points

# Heritage multiple : commande avec fidelite
class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        total = self.prix_total()
        self.ajouter_points(self.client, total)

# Exemple 
if __name__ == "__main__":
    # Creation d'un client
    client1 = Client("ilyas", 1)

    # Creation des boissons avec les nouvelles boissons
    boisson = Cafe()
    boisson = Lait(boisson)
    boisson = Sucre(boisson)
    
    boisson2 = The()
    boisson2 = Caramel(boisson2)
    
    #  nouvelles boissons
    jus_orange = JusOrange()
    soda = Soda()
    
    # Combinaisons avec les nouvelles boissons
    menu1 = boisson + boisson2
    menu2 = jus_orange + soda
    menu3 = jus_orange + Caramel(The())  

    # Création d'une commande avec plusieurs boissons
    commande = CommandeFidele(client1)
    commande.ajouter_boisson(menu1)
    commande.ajouter_boisson(menu2)
    commande.ajouter_boisson(menu3)
    
    print("\n**** COMMANDE COMPLÈTE ****")
    commande.afficher_contenu()

    # Validation commande -> ajout points fidélité
    commande.valider_commande()
    print(f"Points fidélité de {client1.nom} : {client1.points_fidelite}")
    
    # Test pour des nouvelles boissons
    print("\n**** TESTS INDIVIDUELS (des nouvelles boissons) ****")
    print(f"Jus Orange seul : {JusOrange().description()} - {JusOrange().cout()}€")
    print(f"Soda seul : {Soda().description()} - {Soda().cout()}€")
    print(f"Jus Orange avec Caramel : {Caramel(JusOrange()).description()} - {Caramel(JusOrange()).cout()}€")