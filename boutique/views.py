from django.shortcuts import render, get_object_or_404, redirect
from .models import Catégorie, Produit
from cart.forms import CartAddProductForm
from .filters import ProductFilter
from django.db.models import Q
from django.db.models.query import QuerySet


def product_list(request, catégorie_libellé=None):
    catégorie = None
    catégories = Catégorie.objects.all()
    produits = Produit.objects.filter(disponible=True, )

    if catégorie_libellé:
        catégorie = get_object_or_404(Catégorie, libellé=catégorie_libellé)
        produits = produits.filter(catégorie=catégorie)
    myFilter = ProductFilter(request.GET, queryset=produits)
    produits = myFilter.qs

    context = {

        'catégorie': catégorie,
        'catégories': catégories,
        'produits': produits,
        'myFilter' : myFilter
    }

    return render(request, 'home.html', context)


def product_detail(request, id, libellé):
    produit = get_object_or_404(Produit, id=id, libellé=libellé, disponible=True)
    cart_product_form = CartAddProductForm()
    context = {

        'produit': produit,
        'cart_product_form': cart_product_form,

    }

    return render(request, 'produit.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        produits = Produit.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        produits = Produit.objects.filter(nom__icontains=query)
    if not produit.exists():
        Produits = Produit.filter(Produits_nom_icontains=query)
    nom = "Résultats pour la requête %s" % query
    context = {
        'nom': nom
    }
    return render(request, 'search.html', context)

""""
def queryset(query=None):
    queryset = []
    queries = split("")
    for q in queries:
        Produits = product_list.objects.filter(
            Q(nom__icontains=q)
        )
        for prod in produits:
            queryset.append(prod)
    return List(set(queryset))
"""
