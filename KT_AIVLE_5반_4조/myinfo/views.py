from re import U
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import UserTable
from .forms import SignUpForm


# 마이페이지(프로필 정보 조회)
@csrf_exempt
def myinfo(request):
    current_user_id = request.session['user_id_key']
    current = UserTable.objects.get(pk = current_user_id)
    context = { 'user_id':current.user_id,'password':current.password, 'email':current.email, 'user_name':current.user_name }
    return render(request, 'myinfo/info.html', context)


# 마이페이지 수정
@csrf_exempt
def myinfo_edit(request):
    current_user_id = request.session['user_id_key']
    before_info = UserTable.objects.get(pk = current_user_id)
    before_info2 = User.objects.get(username = current_user_id)
  
    if request.method == "POST":
        rewrite_pw = request.POST['new_password']
        rewrite_email = request.POST['new_email']
        
        before_info.password = rewrite_pw
        before_info.email = rewrite_email
        before_info.save()
        before_info2.set_password(rewrite_pw)
        before_info2.save()
        return redirect('/')

    current = UserTable.objects.get(pk = current_user_id)
    context = { 'user_id':current.user_id, 'password':current.password, 'email':current.email, 'user_name':current.user_name }
    return render(request, 'myinfo/info_edit.html', context)

# 회원탈퇴
def member_del(request):
    current_user_id = request.session['user_id_key']
    data1 = UserTable.objects.get(pk = current_user_id)
    data2 = User.objects.get(username = current_user_id)
    data1.delete()
    data2.delete()
    logout(request)
    return redirect('/')

# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        error_message = ''
        
        user = authenticate(request, username=user_id, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['user_id_key'] = UserTable.objects.get(user_id=user_id, password=password).user_id
            return redirect('../../')
        else:
            error_message = '아이디와 비밀번호가 일치하지 않습니다.'
            return render(request, 'myinfo/login.html', {'error_message': error_message})

    return render(request, 'myinfo/login.html')


# 회원가입 폼
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
                    return render(request, 'myinfo/signup.html', { 'form': form, 'user_id_check': message})
            except:
            # 회원가입 성공
                User.objects.create_user(username=user_id, password=password)    # import한 User 객체의 username, password
                user = UserTable(user_id=user_id, password=password, user_name=user_name, email=email)
                user.save()

                return redirect('../login')
        else:
            message = '비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
            return render(request, 'myinfo/signup.html', { 'form': form, 'password_check': message })

    # GET method일 경우
    return render(request, 'myinfo/signup.html')

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


