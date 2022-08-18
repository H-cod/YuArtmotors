from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('details', views.CarDetailListView.as_view(), name='car-details'),
    path('detail/<int:pk>', views.CarDetailDetailView.as_view(), name='detail-detail'),
    path('car-list/', views.CarListView.as_view(), name='car-list'),
    path('car-detail/<int:pk>', views.CarDetailView.as_view(), name='car-detail')
]