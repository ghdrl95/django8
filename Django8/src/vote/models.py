from django.db import models
from django.contrib.auth.models import User
#모델클래스 정의시 models.py에 있는 Model 클래스를 상속받음
class Question(models.Model):
    #저장할 속성을 models.클래스명()으로 객체 생성후 변수에 대입
    #models.CharField : 글자수 제한을 두는 문자열을 저장할 때 사용
    #models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField('질문 문구',max_length=200)
    #models.DateTimeField() : 날짜+시간 정보를 저장할 때 사용
    pub_date = models.DateTimeField('작성일')
    #각 속성에 null변수와 blank 변수를 True 설정하면 값이 비어있어도 
    #객체가 생성되도록 설정
    def __str__(self):
        return self.question_text 
    
    
class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    #models.IntegerField() : 정수값을 저장할 때 사용
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #models.ForeignKey : 다른 모델클래스와 연결고리를 만들 때 사용
    #이 때 1:n 관계를 가짐
    #on_delete : 연결지은 모델클래스의 객체가 삭제될 경우 자신도 삭제될것인지
    #            명시하는 매개변수 
    def __str__(self):
        return self.choice_text
    
    
    
    
    
    
    
    
    
    
    