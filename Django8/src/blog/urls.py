
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns=[
    path('',index.as_view(), name='index'),
    path('<int:post_id>/', detail, name='detail'),
    path('search/', searchP, name='searchP')
    ]







