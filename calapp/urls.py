from django.urls import path
from .import views

#Create urls
urlpatterns = [
    path('',views.calculator, name='calculator'),
    path('intslug/<int:a>/<int:b>/', views.intslug , name="intslug"),
    path('strslug/<str:x>/<str:y>/', views.strslug , name="strslug"),
    path('justslug/<slug:x>/<slug:y>/<slug:z>/', views.justslug , name="justslug"),
]