from django.shortcuts import render, redirect
from .models import UserTable
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        error_message = ''
        
        user = authenticate(request, username=user_id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('../../')
        else:
            error_message = '아이디와 비밀번호가 일치하지 않습니다.'
            return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html')

# 아이디 중복체크
def id_check(request):
    user_id = request.GET.get('user_id')
    result = 'fail'
    try:
        check_result =  User.objects.get(username=user_id)
    except:
        check_result = None
    if check_result is None:
        result = 'possible'

    return JsonResponse({ 'result': result })

# 회원가입 폼
from django.contrib.auth.models import User  # User model 연결 
@csrf_exempt
def form_model(request):
    form = SignUpForm(request.POST)

    # POST method일 경우
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')

        # password 일치 시
        if password == password_check:
            try:
                if User.objects.get(username=user_id):
                    message = '이미 존재하는 아이디입니다.'
                    return render(request, 'registration/signup.html', { 'form': form, 'user_id_check': message})
            except:
            # 회원가입 성공
                User.objects.create_user(username=user_id, password=password)    # import한 User 객체의 username, password
                print('gg')
                user = UserTable(user_id=user_id, password=password, user_name=user_name, email=email)
                user.save()

                return redirect('../login')
        else:
            message = '비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
            return render(request, 'registration/signup.html', { 'form': form, 'password_check': message })

    # GET method일 경우
    return render(request, 'registration/signup.html')