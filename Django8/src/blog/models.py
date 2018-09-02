from django.db import models

#글 종류
class PostType(models.Model):
    name = models.CharField('구분',max_length=50)
    def __str__(self):
        return self.name
from django.conf import settings
#글
class Post(models.Model):
    type = models.ForeignKey(PostType,on_delete=models.CASCADE)
    headline = models.CharField('제목',max_length=200)
    content = models.TextField('내용',null=True,blank=True)
    #auto_now_add = True : 객체가 생성되는 시점의 날짜/시간 정보를 기본값으로
    #사용
    pub_date = models.DateField('작성일',auto_now_add=True)
    #User 모델클래스를 사용할 때 
    #settings.AUTH_USER_MODEL 또는 User 모델클래스로 사용가능
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

#이미지
class Image(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField('이미지파일',upload_to='images/%Y/%m/%d')
    def delete(self, using=None, keep_parents=False):
        #image 변수에 저장된 경로의 파일을 지우는 작업
        #why? Image객체가 지워질때 image경로의 파일이 지워지지않으므로
        #객체가 삭제되는 delete함수 내에 이미지파일이 삭제되는 코드를 삽입
        self.image.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)
#파일
class File(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    file = models.FileField('파일', upload_to='files/%Y/%m/%d')
    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)













