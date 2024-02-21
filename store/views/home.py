from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Products
from store.models.category import Category
from django.views import View

class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if cart:
            quantity = cart.get(product, 0)
            if remove:
                if quantity <= 1:
                    cart.pop(product)
                else:
                    cart[product] = quantity - 1
            else:
                cart[product] = quantity + 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.path}')

def store(request):
    cart = request.session.get('cart', {})
    if not cart:
        request.session['cart'] = {}

    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')

    if category_id:
        products = Products.get_all_products_by_categoryid(category_id)
    else:
        products = Products.get_all_products()

    data = {'products': products, 'categories': categories}
    print('you are : ', request.session.get('email'))

    return render(request, 'index.html', data)