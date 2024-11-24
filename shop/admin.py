from django.contrib import admin
from .models import Category, Product,Commande


admin.site.site_header = "AMOUGOU's Digital Marketplace"
admin.site.site_title = "AMOUGOU shop"
admin.site.index_title = "Manageur"
# Configuration de l'affichage de Category dans l'administration
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')  # Colonnes affichées dans la liste des catégories

# Configuration de l'affichage de Product dans l'administration
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')  # Colonnes affichées dans la liste des produits
    search_fields = ('title',)
    list_editable = ('price',)
class AdminCommande(admin.ModelAdmin):
    list_display = ('items','nom', 'email','address','ville','pays','total','date_commande')

# Enregistrement des modèles avec leurs configurations d'administration
admin.site.register(Category, AdminCategorie)  # Associe Category avec AdminCategorie
admin.site.register(Product, AdminProduct)  # Associe Product avec AdminProduct
admin.site.register(Commande, AdminCommande)