from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from .models import PostTable
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import PostTableForm
from django.contrib import messages

app_name='post_detail'

def post_detail(request, post_id):
    post = PostTable.objects.get(pk=post_id)
    return render(request, 'post_detail/post_detail.html', {'post':post})

def post_modify(request, post_id):
    post = get_object_or_404(PostTable, pk=post_id)
    if request.method == "POST":
        form = PostTableForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()
            post.save()
            return redirect('../../' + str(post.post_id))
    else:
        form = PostTableForm(instance=post)
    context = {'form': form, 'post':post}
    return render(request, 'post_detail/post_form.html', context)

def post_delete(request, post_id):
    post = get_object_or_404(PostTable, pk=post_id)
    post.delete()
    return redirect('/post_detail')

@require_POST
def post_recommend(request, post_id):
    post = get_object_or_404(PostTable, pk=post_id)

    if request.user == post.user_name:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        post.recommender.add(request.user)
    return redirect('post_detail:post_detail', post_id=post.post_id)