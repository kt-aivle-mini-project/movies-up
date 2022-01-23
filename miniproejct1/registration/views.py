from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # response_data
        error_message = ""
        
        if user_id and password:
            # 일치하면 세션에 저장, 불일치하면 예외처리
            try:
                user = User.objects.get(user_id=user_id, password=password)
                request.session['user'] = {
                    'user_id': user.user_id,
                    'password': user.password,
                    'user_name': user.user_name,
                    'email': user.email
                }
                # print(request.session['user']['email']) # 세션저장 확인코드
            except User.DoesNotExist as e:
                error_message = '아이디와 비밀번호가 일치하지 않습니다.'
                return render(request, 'registration/login.html', {'error_message': error_message})

        # 로그인 성공
        return redirect('/post_detail')

    return render(request, 'registration/login.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        print(request.POST)
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        user = User(user_id=user_id, password=password, user_name=user_name, email=email)
        user.save()
        return redirect('../')
    return render(request, 'registration/signup.html')

