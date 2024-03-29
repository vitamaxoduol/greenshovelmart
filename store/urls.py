from django.contrib import admin
from django.urls import path
from store.views.home import Index, store
from store.views.search import search
from store.views.signup import Signup
from store.views.login  import Login, logout
from store.views.cart import Cart
from store.views.checkout import CheckOut
from store.views.orders import OrderView
from store.views.thank_you import ThankYouView
from store.middlewares.auth import auth_middleware



urlpatterns = [
    path('', Index.as_view(),  name='homepage'),
    path('store', store, name='store'),
    
    path('search/', search, name='search'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name = 'logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
     path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]

