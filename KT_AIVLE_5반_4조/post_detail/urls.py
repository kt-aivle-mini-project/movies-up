from django.urls import path
from . import views

app_name = 'post_detail'
urlpatterns = [
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('post/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('post/recommend/<int:post_id>', views.post_recommend, name='post_recommend'),
    path('post/detail/comment/delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    
    path('post_list/',views.post_list, name='post_list'),
    path('post_list/post_new/', views.post_new, name='post_new'),
    path('post_list/edit/<int:post_id>', views.post_edit, name='post_edit'),
]
