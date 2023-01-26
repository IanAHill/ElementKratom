from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('productpage/', views.product_page, name="product_page"),
    path('kratom-overview/', views.kratom_overview, name="kratom-overview"),

]