from django import forms
from .models import PostTable

class PostTableForm(forms.ModelForm):
    class Meta:
        model = PostTable

        fields = ['post_title', 'post_image', 'post_contents']

        labels = {
            'post_title' : '제목',
            'post_image' : '이미지',
            'post_contest' : '내용',
        }
