from tkinter import EW
from unicodedata import category, name
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Movie
from post_detail.models import PostTable
from django.core.paginator import Paginator
from django.views.decorators.clickjacking import xframe_options_exempt

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


@xframe_options_exempt
def list(request, movie_id):
    now_page = request.GET.get('page', 1)
    print("now_page :" ,now_page )
    datas = PostTable.objects.order_by('-post_id')
    p = Paginator(datas, 10)
    # p = Paginator(datas, 1) # 테스트용 임시코드


    # 요청파라미터는 문자열이기 때문에 int로 형변환
    now_page = int(now_page)
    posts = p.page(now_page)

    # 이전 페이지가 있는지
    has_previous = posts.has_previous()

    # 다음 페이지가 있는지
    has_next = posts.has_next()

    # 페이지 네비게이션 - 공식(10개씩 끊기): (현재페이지 -1) // 10 * 10 + 1
    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    print(posts)
    context = {
        'posts' : posts,
        'page_range' : range(start_page, end_page + 1),
        'has_previous' : has_previous,
        'has_next' : has_next
    }
    return render(request,'main/detail_list.html', context)



