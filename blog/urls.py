from django.urls import path
from .models import anime_info
from . import views


urlpatterns = [
    path('',views.anime, name='anime'),
    path('<str:name>/',views.info, name='info'),
    path('search',views.search, name='search')
]
