from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/',views.submit_form,name='submit_form'),
    path('django_form/', views.DjangoForm, name='django_form'),
    path('student_form/', views.PasswordValidation, name='student_form'),
]
