from django.shortcuts import render
from store.models.products import Products

def search(request):
    query = request.GET.get('query', '')
    products = Products.objects.filter(name__icontains=query)
    categories = []  # Assuming you want to display categories in the search results

    data = {'products': products, 'categories': categories, 'query': query}
    return render(request, 'search.html', data)