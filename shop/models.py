from django.db import models

# Définition de la catégorie
class Category(models.Model):
    name = models.CharField(max_length=200)  # Nom de la catégorie
    date_added = models.DateTimeField(auto_now=True)  # Date de création/mise à jour

    class Meta:
        ordering = ['-date_added']  # Trier les catégories par date décroissante

    def __str__(self):
        return self.name  # Représentation en chaîne de caractères


# Définition des produits
class Product(models.Model):
    title = models.CharField(max_length=200)  # Titre du produit
    price = models.FloatField()  # Prix du produit
    description = models.TextField()  # Description du produit
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Lien avec la catégorie
    image = models.CharField(max_length=5000)  # URL ou chemin de l'image
    date_added = models.DateTimeField(auto_now=True)  # Date de création/mise à jour

    class Meta:
        ordering = ['-date_added']  # Trier les produits par date décroissante

    def __str__(self):
        return self.title  # Représentation en chaîne de caractères


class Commande(models.Model):
    items = models.CharField(max_length=300)
    nom = models.CharField(max_length=255)
    total = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']
