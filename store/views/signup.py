from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        try:
            customer.validate_fields()
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        except ValueError as e:
            error_message = str(e)
            data = {'error': error_message, 'values': postData}
            return render(request, 'signup.html', data)