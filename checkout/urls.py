from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('add/<package_id>/', views.add_to_basket, name='add_to_basket'),
]