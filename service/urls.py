from django.urls import path
from service import views

urlpatterns = [
    path('', views.ServiceView.as_view(), name='services'),
    path('contact/', views.ContactView.as_view(), name='contact')
]