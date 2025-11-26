from django.urls import path
from .views import CarListApiView, CarEditApiView, CarDeleteApiView, CarMixedApiView, CarDetailApiView

urlpatterns = [
    path('', CarListApiView.as_view(), name='cars'),
    path('cars/', CarListApiView.as_view(), name='cars'),
    path('cars/edit/<int:pk>/', CarEditApiView.as_view(), name='edit'),
    path('cars/delete/<int:pk>/', CarDeleteApiView.as_view(), name='car_delete'),
    path('cars/<int:pk>/', CarDetailApiView.as_view(), name='car_detail'),
    path('cars/mix/<int:pk>/',CarMixedApiView.as_view(),name='car_mixed')

]