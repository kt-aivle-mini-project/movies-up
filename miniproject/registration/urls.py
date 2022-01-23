from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/id_check', views.id_check),
    path('signup/', views.form_model, name='form_model'),
]
