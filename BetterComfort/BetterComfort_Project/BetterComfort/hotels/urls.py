from tempfile import template
from tkinter.font import names
from django.urls import path, include, register_converter
from django.contrib.auth import views as auth_views
from . import views,converters
from .custom_filters import register

register_converter(converters.FloatConverter, 'float')

urlpatterns = [
 path('', views.home,name='home'),
 path('login/', auth_views.LoginView.as_view(template_name='hotels/login.html'), name='login'),
 path('logout/', views.custom_logout, name='logout'),
 path('register/', views.register, name='register'),
 path('about/', views.about,name='about'),
 path('search/', views.search_hotels, name='search_hotels'),
 path('details/<str:lat>/<str:lon>/<str:name>/', views.hotel_details, name='hotel_details'),
 path("favorites", views.favorites_list, name="favorites_list"),
 path("save-favorite/", views.save_favorite, name="save_favorite"),
 path("delete-favorite/<int:favorite_id>/", views.delete_favorite, name="delete_favorite"),
 path('hotel/<float:lat>/<float:lon>/<str:name>/', views.hotel_details, name='hotel_details'),
 path("error/", views.error_page, name="error_page"),
]