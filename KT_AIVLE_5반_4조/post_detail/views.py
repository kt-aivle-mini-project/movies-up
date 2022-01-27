from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import *
from myinfo.models import *
from .models import *
from .forms import *

app_name='post_detail'

# 영화 후기 상세 view
@csrf_exempt
def post_detail(request, post_id):
    post = PostTable.objects.get(pk=post_id)
    
    # 댓글 작성 예외처리
    try:
        comments = CommentTable.objects.filter(post_table=post_id)
    except:
        comments = None
    

    if request.method == "POST":
        form = CommentForm(request.POST)
            
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = UserTable.objects.get(user_id=request.user.username)
            comment.post_table = PostTable.objects.get(pk=post_id)
            comment.content = request.POST['content']
            comment.create_date = timezone.now()
            comment.save()
        else:
            return render(request, 'post_detail/post_detail_test.html', {'post':post, 'comments':comments})        
        
    return render(request, 'post_detail/post_detail_test.html', {'post':post, 'comments':comments})

# 영화 후기 삭제 view
@csrf_exempt
def post_delete(request, post_id):
    post = get_object_or_404(PostTable, pk=post_id)
    post.delete()
    return render(request, 'post_detail:post_list')

# 영화 후기 추천 view
@csrf_exempt
def post_recommend(request, post_id):
    post = get_object_or_404(PostTable, pk=post_id)
    user = get_object_or_404(UserTable, pk=request.user)
    
    if user in post.recommender.all():
        post.recommender.remove(user)
        post.save()
    else:
        post.recommender.add(user)
        post.save()
    
    return redirect('post_detail:post_detail', post_id=post.post_id)

# 영화 후기 댓글 삭제 view
def comment_delete(request, comment_id):
    comment = get_object_or_404(CommentTable, pk=comment_id)
    comment.delete()
    return redirect('post_detail:post_detail', post_id=comment.post_table.post_id)

# 작성자 게시물 리스트 페이지
def my_post_list(request):
    posts = PostTable.objects.filter(user_name=request.user.username)
    return render(request, 'post_detail/my_post_list.html',{'posts':posts})

# 게시물 작성 페이지
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)       
        if form.is_valid():
            post = form.save(commit=False)
            movie_id = request.POST.getlist('movie_id')[0]
            post.user_name = UserTable.objects.get(user_id=request.user.username)
            post.movie_id = Movie.objects.get(movie_id = movie_id)
            post.save()
            return redirect('post_detail:post_detail',post_id=post.pk)
        else:
            return render(request, 'post_detail/post_new.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'post_detail/post_new.html',{'form':form})

# 게시물 수정 페이지
def post_edit(request, post_id):
    post = get_object_or_404(PostTable,pk=post_id)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = UserTable.objects.get(user_id=request.user.username)
            post.save()
            return redirect('post_detail:post_detail', post_id=post.post_id)
    else:
        form = EditForm(instance=post)
        # form = EditForm(request.POST, request.FILES, instance=post)
    return render(request, 'post_detail/post_edit.html', {'form':form, "post":post})