from django.shortcuts import render, redirect
 
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
 
from store.models.products import Products
from store.models.orders import Order
 
 
class CheckOut(View):
    def post(self, request):
        try:
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            customer_id = request.session.get('customer')
            cart = request.session.get('cart', {})
            
            customer = Customer.objects.get(id=customer_id)
            products = Products.get_products_by_id(list(cart.keys()))

            for product in products:
                quantity = cart.get(str(product.id), 0)
                order = Order(customer=customer,
                              product=product,
                              price=product.price,
                              address=address,
                              phone=phone,
                              quantity=quantity)
                order.save()

            request.session['cart'] = {}

            return redirect('cart')

        except Exception as e:
            # Handle exceptions (ex: database errors) and log them
            print(f"Error during checkout: {str(e)}")
            return redirect('cart')  # Redirect to cart or another appropriate page
    