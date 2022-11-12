from django.urls import path
from . import views

urlpatterns = [
    path('add/<package_id>/', views.add_to_basket, name='add_to_basket'),
]
