from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Commande
from django.core.paginator import Paginator

# Vue pour afficher les produits
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name:
        product_object = Product.objects.filter(title__icontains=item_name)

    # Pagination
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object': product_object})

# Vue pour afficher la confirmation de commande
def confirmation(request):
   
   info = Commande.objects.all()[:1]
   for item in info:
       nom = item.nom
       return render(request, 'shop/confirmation.html',{'name':nom})




# Vue pour afficher les détails d'un produit spécifique
def detail(request, myid):
    product_object = get_object_or_404(Product, id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})

# Vue pour gérer le processus de commande (checkout)
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')

        # Enregistrer la commande
        com = Commande(
            items=items,
            total=total,
            nom=nom,
            email=email,
            address=address,
            ville=ville,
            pays=pays,
            zipcode=zipcode
        )
        com.save()

        # Enregistrer l'ID de commande dans la session
        request.session['commande_id'] = com.id

        return redirect('confirmation')

    return render(request, 'shop/checkout.html')
