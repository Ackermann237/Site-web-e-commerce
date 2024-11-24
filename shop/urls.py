from django.urls import path
from shop.views import index, detail, checkout,confirmation

urlpatterns = [
    path('', index, name='home'),  # Vue de l'accueil
    path('<int:myid>/', detail, name='detail'),  # Vue des détails d'un produit
    path ('checkout/', checkout, name="checkout"),
  path('confirmation/', confirmation, name='confirmation'),


]
