from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
# Create your views here.
#회원가입
def signup(request):
    if request.method == "GET":
        form = UserForm()
        return render(request,'user/signup.html', {'form': form})
    elif request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #패스워드와 패스워드체크가 동일한 값인지 확인
            #form.cleaned_data[키값] 으로 해당 이름으로 저장된 값을 추출
            #단, is_valid()함수를 쓴 뒤에 사용 가능
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                #회원 생성
                new_user = User.objects.create_user( form.cleaned_data['username'],
                                                     form.cleaned_data['email'],
                                                     form.cleaned_data['password'] )
                #login(request,user 객체) : 해당요청을 가진 클라이언트가 
                #user객체로 로그인하는 작업을 함 
                login(request,new_user) 
                return HttpResponseRedirect( reverse('index'  )  )
            else: #password와 passwordcheck가 동일하지 않는 경우
                return render(request, 'user/signup.html', {'form':form,
                            'error': '비밀번호가 일치하지않습니다.'})
        else: #유효하지않은 값이 입력된 경우
            return render(request, 'user/signup.html', {'form':form,
                            'error':'유효하지않는 값이 입력됬습니다.'})    
            
def signin(request):
    if request.method =="GET":
        form = LoginForm()
        return render(request, 'user/signin.html',{'form':form})
    elif request.method=="POST":
        form = LoginForm(request.POST)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        #authenticate(username,password) : User 모델클래스에 해당ID와
        #Password를 가진 객체를 찾아 반환. 단, 객체가 없는 경우 None반환
        obj = authenticate(username=id, password=pw)
        
        if obj is not None:
            login(request, obj)
            return HttpResponseRedirect( reverse('index'))
        else:
            return render(request, 'user/signin.html', {'form':form,
                                'error': '아이디 또는 비밀번호가 틀렸습니다.'})
from django.contrib.auth import logout

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
        
        
        
        
        
        
        
        
           
            
            
            
            
            
            
            
            
            