from django import forms
from .models import *
from main.models import Movie

class PostTableForm(forms.ModelForm):
    class Meta:
        model = PostTable

        fields = ['post_title', 'post_image', 'post_contents']

        labels = {
            'post_title' : '제목',
            'post_image' : '이미지',
            'post_contest' : '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentTable
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class PostForm(forms.ModelForm):
    movie_id_list = forms.ModelChoiceField(queryset=Movie.objects.all(),
    empty_label='Select movie id', required=False)
    # user_id_list = forms.ModelChoiceField(queryset=UserTable.objects.all(),
    # empty_label='Select user id', required=False)

    class Meta:
        model = PostTable
        fields = ('post_title','post_contents','post_image')
        labels = {
            'post_title' : '제목',
            'post_contents' : '내용',
            'post_image' : '이미지',
            # 'movie_id' : '영화 아이디',
            # 'user_id' : '작성자',
        }
        # exclude = ('movie_id', 'user_id',)

class EditForm(forms.ModelForm):
    class Meta:
        model = PostTable
        fields = ('post_title','post_contents','post_image')
        labels = {
            'post_title' : '제목',
            'post_contents' : '내용',
            'post_image' : '이미지',
        }
