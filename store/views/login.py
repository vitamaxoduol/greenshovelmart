from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from store.models.customer import Customer
from django.views import View

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None

        try:
            customer = get_object_or_404(Customer, email=email)
            if customer and check_password(password, customer.password):
                request.session['customer'] = customer.id

                if Login.return_url:
                    return redirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Invalid credentials'
        except Customer.DoesNotExist:
            error_message = 'User not found. Please check your email.'
        except Exception as e:
            # Handle unexpected exceptions (e.g., database issues) and log the error
            print(f"Error during login: {str(e)}")
            error_message = 'An unexpected error occurred. Please try again.'

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    try:
        request.session.clear()
    except Exception as e:
        # Handle unexpected exceptions (ex: session issues) and log the error
        print(f"Error during logout: {str(e)}")
    
    return redirect('login')