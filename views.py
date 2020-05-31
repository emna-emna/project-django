from django.shortcuts import render, get_object_or_404, redirect
from .models import Catégorie, Produit
from cart.forms import CartAddProductForm


def product_list(request, catégorie_libellé=None):
    catégorie = None
    catégories = Catégorie.objects.all()
    produits = Produit.objects.filter(disponible=True,)

    if catégorie_libellé:
        catégorie = get_object_or_404(Catégorie, libellé=catégorie_libellé)
        produits = produits.filter(catégorie=catégorie)
    context = {
        'catégorie': catégorie,
        'catégories': catégories,
        'produits': produits

    }
    return render(request, 'home.html', context)


def product_detail(request, id, libellé):
    produit = get_object_or_404(Produit, id=id, libellé=libellé, disponible=True)
    cart_product_form = CartAddProductForm()
    context = {

        'produit': produit,
        'cart_product_form': cart_product_form
    }

    return render(request, 'produit.html', context)


def search(request,):
    query = request.GET.get('query')
    if not query:
        produits = Produit.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        produits = Produit.objects.filter(nom__icontains=query)
    if not produits.exists():
        produits = produits.filter(nom=query)
    nom = "Résultats pour la requête %s"%query
    context = {
        'produits': produits,
        'nom': nom
    }
    return render(request, 'search.html', context)
