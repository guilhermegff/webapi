from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('establishments/<int:pk>/', views.EstablishmentDetail.as_view(), name="establishment_detail"),
    path('establishments/', views.EstablishmentList.as_view(), name="establishment_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

