from django import forms
from .models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password', 'user_name', 'email'] # id 속성은 PK 이므로 사용하지 않음
        
        labels = { # fields에 명시된 속성만 사용
            'user_id': '아이디',
            'password': '비밀번호',
            'email': '이메일',
            'user_name': '이름'
        }
