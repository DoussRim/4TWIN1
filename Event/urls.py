from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('i/',views.index),
    path('index/<str:param>',views.index_param),
    path('Affiche/',Affiche,name='Aff'),
    path('Liste/',AfficheGeneric.as_view()),
    path('Detail/<str:title>',Detail,name="D"),
    path('DG/<int:pk>',DetailGeneric.as_view(),name="DD"),
    path('Ajout/',Add,name="Add"),
    path('Add/',Ajout.as_view(),name='Ajout')  
]
