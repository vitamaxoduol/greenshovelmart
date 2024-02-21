from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.products import Products

class Cart(View):
    def get(self, request):
        try:
            cart = request.session.get('cart', {})
            ids = list(cart.keys())
            products = Products.get_products_by_id(ids)
            print(products)
            return render(request, 'cart.html', {'products': products})
        except Exception as e:
            # Handle unexpected errors (e.g., database issues) and log the error
            print(f"Error fetching products from the cart: {str(e)}")
            # Redirect or provide an error message to the user
            return redirect('error_page')