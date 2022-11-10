from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_packages, name='packages'),
    path('<package_id>', views.package_detail, name='package_detail'),
    path('add/', views.add_package, name='add_package'),
    path('edit/<int:package_id>/', views.edit_package, name='edit_package'),
]