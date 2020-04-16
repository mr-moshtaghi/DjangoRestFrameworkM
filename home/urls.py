from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
	path('one/', views.one),
	path('persons/', views.persons),
]