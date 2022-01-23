from django.urls import path
from . import views

app_name = 'post_detail'
urlpatterns = [
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('post/modify/<int:post_id>', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('post/recommend/<int:post_id>', views.post_recommend, name='post_recommend'),

    # path('<int:post_id>/<int:recommneder>', views.post_recommend, name='post_recommend'),
    # path('post/modify/<int:post.post_id>/', views.post_modify, name='post_modify'),
]
