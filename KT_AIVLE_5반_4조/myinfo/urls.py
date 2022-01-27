from django.urls import path
from . import views

app_name = 'myinfo'
urlpatterns = [
    
    path('myinfo/', views.myinfo, name='myinfo'),
    path('myinfo/edit', views.myinfo_edit, name='myinfo_edit'),
    path('myinfo/edit/del', views.member_del, name='member_del'),
    path('login/', views.login, name='login'),
    path('signup/id_check', views.id_check),
    path('signup/', views.form_model, name='form_model'),
    path('logout/', views.logout_view, name='logout'),

]