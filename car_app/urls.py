from django.urls import path
from .views import PhoneListApiView,PhoneCreateApiView,PhoneEditApiView,PhoneDeleteApiView, PhoneDetailApiView, PhoneMixedApiView



urlpatterns=[
    path('phone/',PhoneListApiView.as_view(),name='cars'),
    path('phone/create/',PhoneCreateApiView.as_view(),name='cars_create'),
    path('phone/edit/<int:pk>/',PhoneEditApiView.as_view(),name='edit'),
    path('phone/delete/<int:pk>/',PhoneDeleteApiView.as_view(),name='car-delete'),
    path('phone/<int:pk>/', PhoneDetailApiView.as_view(), name='car_detail'),
    path('phone/mix/<int:pk>', PhoneMixedApiView.as_view(), name='car_mixed'),
]