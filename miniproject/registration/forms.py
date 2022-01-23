from django import forms
from .models import UserTable
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserTable

        # 관리대상(화면에 출력 & 유효성 검사) cf) id 속성은 PK 이므로 사용하지 않음
        fields = ['user_id', 'password', 'user_name']