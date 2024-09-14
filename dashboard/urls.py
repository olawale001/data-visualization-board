from django.urls import path
from . import views

urlpatterns = [
    path('api/sales-data/', views.sales_data, name='sales_data'),
    path('api/sales-summary/', views.sales_summary, name='sales_summary'),
    path('', views.dashboard_view, name='dashboard_view'),
]
