"""Django8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from vote.views import * #vote/view.py 에 있는 모든 함수/클래스 추가
urlpatterns = [
    path('admin/', admin.site.urls),#127.0.0.1:8000/admin/
    path('', index, name = 'index' ),#127.0.0.1:8000/
    #URL 등록 시 파이썬 코드에서 URL을 외워서 사용하지 않고,
    #별칭을 이용해서 사용할 수 있도록 name 매개변수에 문자열을 대입
    path('<int:question_id>/', detail, name = 'detail' ),
    #path('admin/',index),
    #URL 추가 http://127.0.0.1:8000 주소로 접근시 vote 어플리케이션의
    #view인 index 함수를 호출 하도록 등록
    path('result/<int:question_id>/',result, name='result'),
    path('vote/',vote,name='vote'),
    path('registerQuestion/', registerQ, name='registerQ'),
    path('registerChoice/', registerC, name='registerC'),
    path('delete/<int:question_id>/',deleteQ,name='deleteQ'),
    path('deleteC/<int:choice_id>/',deleteC, name='deleteC'),
    path('updateQ/<int:question_id>/',updateQ,name="updateQ"),
    path('updateC/<int:choice_id>/',updateC, name='updateC'),
    #127.0.0.1/login/ URL 주소로 요청이 되면 view함수 호출 처리는
    #customlogin 폴더에있는 urls.py에서 처리하도록 등록
    path('login/', include('customlogin.urls')),
    path('auth/', include('social_django.urls',namespace ='social'  ) ),
    path('blog/', include('blog.urls') )
]
#파일 관리 모듈 : Pillow
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







