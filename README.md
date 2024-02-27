# Greenshovelmart
The scope of the project is be limited to some functions of the e-commerce website. It is display products, and customers can select catalogs and select products and can remove products from their cart specifying the quantity of each item. Selected items is be collected in a cart. At checkout, the item on the card is be presented as an order. Customers can pay for the items in the cart to complete an order. This project has a great future scope. The project also provides security with the use of login ID and passwords, so that no unauthorized users can access your account. The only authorized person who has the appropriate access authority can access the software.

## Features

- **Product Catalog:** Browse and search for various products.
- **Shopping Cart:** Add products to your cart and proceed to checkout.
- **User Authentication:** Signup, login, and manage your user account.
- **Order History:** View your order history and track past purchases.
- **Responsive Design:** Access the application seamlessly on different devices.


## Project Setup
1. Create python3.11 enevironment for project  and then 
2. Install Django: Next,I will install the Django module from the terminal.I will use Vs code to do this task. One can also use cmd on windows to install the module by running python -m pip install django command
3. Create Django Project: When I execute django-admin startproject command, then it will create a Django project inside the normal project which I already have created here. `django-admin startproject greenshovel`.
4. Create Django app: When I execute django-admin startapp command, then it will create a Django app of the `greensholemart` inside the normal project which I already have created here. `django-admin startproject store`.

Other modules installations:
1. `python -m pip install django`
2. `python -m pip install Pillow`
3. `pip freeze > requirements.txt` - Install the required dependencies.
4. `python manage.py makemigrations` - Making database migrations.
5. `python manage.py migrate` - Apply database migrations.
6. `python manage.py runserver` - Developement of server


- The application should now be accessible at `http://127.0.0.1:8000/`.

## Technologie Used
1. Python
2. Django framework
3. Django-templates


## Models
1. Category
2. Customer
3. Products
4. Orders
5. Cart

## Authors
Vitamax Oduol

## License
This project is licensed under the MIT License - see the LICENSE file for details.
