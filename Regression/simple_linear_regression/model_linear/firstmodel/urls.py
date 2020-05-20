from django.contrib import admin
from django.urls import path
from firstmodel import views

urlpatterns = [
    path('', views.salary_ten,name='firstmodel'),
    path('predict_chances/', views.predict_chances,name='predict_chances')
]