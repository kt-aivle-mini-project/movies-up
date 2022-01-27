from django.urls import path,include
from . import views
from .views import MovieList,MovieTag,MovieSearch,MovieDetailList

app_name = 'movies'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('list/<int:movie_id>', views.movie_detail_list, name = 'list'),
    path('select/',views.select,name = 'select'),
    path('select/movieList',views.list,name = 'movieList'),
    path('movie_list/',MovieList.as_view(),name = 'movie_list'),
    path('select/<str:genre_tag>',MovieTag.as_view(),name = 'movie_tag'),
    path('search/<str:query>',MovieSearch.as_view(),name = 'movie_search'),
    path('post_detail/', include('post_detail.urls')),
]
