from tkinter import EW
from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie
from post_detail.models import PostTable

class MovieList(ListView):
    model = Movie
    #context_object_name = ''
    #template_name = ''

class MovieSearch(ListView):
    model = Movie

    def get_queryset(self):
        query = self.request.Get.get('q')
        
        if query:
            object_list = self.model.filter(movie_title__icontains = query)
        else :
            object_list = self.model.objects.none()
        return object_list

class MovieTag(ListView):
    model = Movie

    def get_queryset(self):
        self.genre_tag = self.kwargs['genre_tag']
        return Movie.objects.filter(genre_tag = self.genre_tag)

    def get_context_data(self, **kwargs) :
        context = super(MovieTag,self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(genre_tag = self.genre_tag).filter(status = "TR")
        context['most_commented'] = Movie.objects.filter(genre_tag = self.genre_tag).filter(status = "MC")
        context['recently_added'] = Movie.objects.filter(genre_tag = self.genre_tag).filter(status = "RA")
        return context

# 영화별 후기 게시판
def movie_detail_list(request, movie_id):
    posts  = PostTable.objects.filter(movie_id=movie_id)
    movie = Movie.objects.get(movie_id=movie_id)
    contents = {'posts':posts, 'movie':movie}
    return render(request, 'main/detail_list_test.html', contents)

class MovieDetailList(ListView):
    model = PostTable
    template_name ="main/detail_list_test.html"

    def get_queryset(self):
        self.movie_id = self.kwargs['movie_id']
        return PostTable.objects.filter(movie_id = self.movie_id)

    def get_context_data(self, **kwargs) :
        context = super(MovieDetailList,self).get_context_data(**kwargs)
        context['movie_id'] = PostTable.movie_id
        return context

def index(request):
    return render(request,'main/index.html')

def select(request):
    return render(request,'main/select.html')