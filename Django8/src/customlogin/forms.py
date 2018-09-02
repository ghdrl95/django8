'''
Created on 2018. 8. 26.

@author: kgitbank404
'''
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
#회원가입에 사용할 입력양식
class UserForm(ModelForm):
    #UserForm(instance=obj)
    #print(kwargs) -> {'instance' : obj }
    def __init__(self,*args, **kwargs):
        #ModelForm.__init__(*args,**kwargs)
        super().__init__(*args,**kwargs)
        #객체.fields[키값] : 해당 폼 클래스에서 설정한 fields, 변수에
        #입력되는 설정값들을 수정,읽기 할 수 있음
        #객체.fields[키값].label : <label>태그에 들어갈 문구를 저장한 변수
        self.fields['password_check'].label = "패스워드 확인"
    
    #모델클래스와 유사하게 XXXField 클래스의 객체를 변수에 저장해 새로운
    #<input> 태그를 생성할 수 있음 43
    password_check = forms.CharField(max_length=200,
                                      widget=forms.PasswordInput() )
    class Meta:
        model = User
        widgets={
            'password' : forms.PasswordInput(),
            'email' : forms.EmailInput()
            }
        fields=['username','password','email']
#로그인에 사용할 입력양식 
class LoginForm(ModelForm):
    class Meta:
        model = User
        #widgets : 각 변수에 입력 스타일을 설정할 때 사용
        #키 : 변수명   값 : XXXInput 클래스 객체
        widgets = {'password' : forms.PasswordInput() }
        fields =['username','password']








