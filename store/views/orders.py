from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.products import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware


class OrderView(View):
    def get(self, request):
        try:
            customer = request.session.get('customer')
            if customer:
                orders = Order.get_orders_by_customer(customer)
                print(orders)
                return render(request, 'orders.html', {'orders': orders})
            else:
                # Redirect or provide an error message for cases when the customer is not found
                return redirect('homepage')  
        except Exception as e:
            # Handle unexpected errors (e.g., database issues) and log the error
            print(f"Error fetching orders: {str(e)}")
            # Redirect or provide an error message to the user
            return redirect('error_page')