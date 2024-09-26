from django.urls import path
from . import views

#syncs the urls

urlpatterns = [
    path('bills/', views.view_bills, name='view_bills'),
    path('bills/create/', views.create_bill, name='create_bill'),
    path('bills/<int:bill_id>/update/', views.update_bill, name='update_bill'),
    path('bills/<int:bill_id>/delete/', views.delete_bill, name='delete_bill'),
]