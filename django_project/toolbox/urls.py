

from django.urls import path

from . import views

app_name = 'toolbox'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
]
